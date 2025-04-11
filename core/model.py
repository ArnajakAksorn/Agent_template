from langchain_openai import AzureChatOpenAI

model_gpt4o = AzureChatOpenAI(
    azure_deployment='gpt-4o',
    api_version='2024-05-01-preview',
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)
