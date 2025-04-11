from langchain_openai import AzureChatOpenAI
from langchain_openai import AzureOpenAIEmbeddings

model_gpt4o = AzureChatOpenAI(
    azure_deployment='gpt-4o',
    api_version='2024-05-01-preview',
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)

embedding_large = AzureOpenAIEmbeddings(model='text-embedding-3-large',
                        api_version="2023-05-15",)
