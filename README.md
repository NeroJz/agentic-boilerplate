# Agentic Boilerplate
The repo contains boilerplate template to kick start the Agentic works or R&D

## Prequisites
The project uses uv to manage the dependencies.
* *uv:* (https://docs.astral.sh/uv/) 

OR, if you opt to install the components manually, make sure the following is installed:
* *python:* Python 3.11
* *Package Manager:* pip (usually included with Python)

## Installation
Choose one of the following based on the installation you follow from Prequisites.
```uv
cd agentic-boilerplate
uv venv

source .venv/bin/activate
uv pip install
```

``` python
python -m venv
source .venv/bin/activate
pip install
```

## Usage
The repo contains template.ipnb which is a boilerplate template that you can duplicate to kick start the R&D work.

Make sure create .env and setup all the environment variables like API_KEY, MODEL and etc.

Make sure the following is configured in .env:
* *OPENAI_API_KEY*: Openai API key
* *MODEL*: Openai Model

* *AZURE_OPENAI_ENDPOINT* : Endpoint of the model deployed in azure
* *AZURE_OPENAI_DEPLOYMENT_NAME*: Deployment name in azure
* *AZURE_OPENAI_API_VERSION*: API version in azure
* *AZURE_OPENAI_API_KEY*: API key deployed in azure
* *AZURE_OPENAI_MODEL*: Model deployed in azure

* *AZ_PBI_AUTHENTICATIONMODE*: PowerBI service principal authentication mode
* *AZ_PBI_AUTHORITYURL*: PowerBI service principal authority URL
* *AZ_PBI_SCOPEBASE*: PowerBI service principal scope
* *AZ_PBI_POWERBIAPIURL*: PowerBI service principal api url
* *AZ_PBI_CLIENTID*: PowerBI service principal client id
* *AZ_PBI_WORKSPACEID*: PowerBI service workspace id
* *AZ_PBI_PBIUSERNAME*: PowerBI service principal username
* *AZ_PBI_PBIPASSWORD*: PowerBI service principal password
* *AZ_PBI_CLIENTSECRET*: PowerBI service principal client secret
* *AZ_PBI_TENANTID*: PowerBI service tenant id
* *AZ_DATASET_ID*: PowerBI service dataset id

The OPENAI_API_KEY is a key created from your Openai account and the MODEL is the LLM model that you want to test.

