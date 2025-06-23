import os
from openai import AzureOpenAI
from openlayer.lib import trace_openai

azure_client = trace_openai(
    AzureOpenAI(
        api_key=os.environ["AZURE_OPENAI_KEY"],
        api_version=os.environ["AZURE_OPENAI_API_VERSION"],
        azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
    )
)

completion = azure_client.chat.completions.create(
    model=os.environ["AZURE_OPENAI_DEPLOYMENT_NAME"],
    messages=[
        {"role": "user", "content": "How are you doing today?"},
    ],
)