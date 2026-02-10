import os
from dotenv import load_dotenv
from azure.identity import ClientSecretCredential
import json
import requests

class _PbiService:
  def __init__(self):
    load_dotenv()
    self.AZ_PBI_AUTHENTICATIONMODE=os.getenv('AZ_PBI_AUTHENTICATIONMODE')
    self.AZ_PBI_AUTHORITYURL=os.getenv('AZ_PBI_AUTHORITYURL')
    self.AZ_PBI_SCOPEBASE=os.getenv('AZ_PBI_SCOPEBASE')
    self.AZ_PBI_POWERBIAPIURL=os.getenv('AZ_PBI_POWERBIAPIURL')
    self.AZ_PBI_CLIENTID=os.getenv('AZ_PBI_CLIENTID')
    self.AZ_PBI_WORKSPACEID=os.getenv('AZ_PBI_WORKSPACEID')
    self.AZ_PBI_PBIUSERNAME=os.getenv('AZ_PBI_PBIUSERNAME')
    self.AZ_PBI_PBIPASSWORD=os.getenv('AZ_PBI_PBIPASSWORD')
    self.AZ_PBI_CLIENTSECRET=os.getenv('AZ_PBI_CLIENTSECRET')
    self.AZ_PBI_TENANTID=os.getenv('AZ_PBI_TENANTID')
    self.AZ_DATASET_ID=os.getenv('AZ_DATASET_ID')

  def _get_token(self):
    client_secret_creden = ClientSecretCredential(
      tenant_id=self.AZ_PBI_TENANTID,
      client_id=self.AZ_PBI_CLIENTID,
      client_secret=self.AZ_PBI_CLIENTSECRET
    )
    access_token = client_secret_creden.get_token(self.AZ_PBI_SCOPEBASE)
    # print(f"Access token: { access_token.token }")
    return access_token.token
  
  def execute(self, query):
    token = self._get_token()
    if (token is None): return 'No access token'

    headers = {
      "Authorization": f"Bearer {token}",
      "Content-Type": "application/json"
    }

    url = f"https://api.powerbi.com/v1.0/myorg/groups/{self.AZ_PBI_WORKSPACEID}/datasets/{self.AZ_DATASET_ID}/executeQueries"
    body = {
      "queries": [
        {
          "query": query
        }
      ]
    }

    response = requests.post(url, headers=headers, data=json.dumps(body))
    if response.status_code == 200:
      data = response.json()
      return data
    else:
      error = response.json()
      return error


pbiService = _PbiService()