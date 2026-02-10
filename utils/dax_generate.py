from .pbi_service import pbiService

class DaxGenerate:
  def __init__(self, client, model, instructions):
    self.client = client
    self.instructions = instructions
    self.model = model

  def _form_prompt(self, user_input):
    content = self.instructions.replace('<MESSAGE>', user_input)
    return content

  def generate(self, user_input):
    try:
      content = self._form_prompt(user_input)
      messages = [
        {
          "role": "user",
          "content": content
        }
      ]

      response = self.client.chat.completions.create(
        model = self.model,
        messages = messages
      )

      return response.choices[0].message.content
    except Exception:
      errorMessage = f"Error on generate the query"
      print(errorMessage)
      return errorMessage
    
  def execute(self, query):
    try:
      result = pbiService.execute(query)
      return result
    except Exception as e:
      errorMessage = f"Error on execute the query: {e}"
      print(e)
      return errorMessage
    
  def check(self, query):
    result = self.execute(query)

    if "results" in result:
      return "passed"
    else:
      messages = []

      details = result['error']['pbi.error']['details']
      for detail in details:
        if (detail['code'] != 'DetailsMessage'): continue
        messages.append(detail['detail']['value'] if detail['detail']['value'] else "")
      
      return '\n'.join(messages) 

  def generate_with_check(self, user_input, max_attempt=2):
    try:
      content = self._form_prompt(user_input)
      attempt = 0

      while attempt < max_attempt:
        try:
          messages = [
            {
              "role": "user",
              "content": content
            }
          ]

          # print(f"{attempt} - message" + ("-" * 80))
          # print(content)

          response = self.client.chat.completions.create(
            model = self.model,
            messages = messages
          )

          query = response.choices[0].message.content

          if attempt == 0:
            query = query + " filtering = 200"

          # print(f"{attempt} - query" + ("-" * 80))
          # print(query)

          result = self.check(query)

          if result == "passed":
            return query
          else:
            print("Could not execute the query. Correcting the existing prompt and query.")
            content = f"""{content}\nThis is syntax error:\n{result}\nUpdate the below DAX query to resolve the issue:\n{query}\nMake sure the update query aligns with the requirements provided in the initial question."""
            attempt += 1

        except Exception as e:
          print(f"Error on correcting the query: {e}")
          attempt += 1

    except Exception as e:
      errorMessage = f"Error on generate_with_check: {e}"
      print(e)
      return errorMessage