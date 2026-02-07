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
OPENAI_API_KEY
MODEL

The OPENAI_API_KEY is a key created from your Openai account and the MODEL is the LLM model that you want to test.

