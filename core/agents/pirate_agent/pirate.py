
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import AzureChatOpenAI

from dotenv import load_dotenv
load_dotenv()  # loads .env file

from .prompt import SYSTEM_PROMPT
from core.model import model_gpt4o

# _prompt = ChatPromptTemplate.from_messages(
#     [
#         (
#             "system",
#             SYSTEM_PROMPT,
#         ),
#         MessagesPlaceholder(variable_name="input"),
#         ("human", "{input}"),
#     ]
# )

_prompt = ChatPromptTemplate.from_messages([
    ("system", SYSTEM_PROMPT),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{human_input}"),
])

pirate_chain = _prompt | model_gpt4o

# print(chain.invoke(["hi"]).content)