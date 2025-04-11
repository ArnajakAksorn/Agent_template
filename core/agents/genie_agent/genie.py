
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import AzureChatOpenAI
from langchain.agents import AgentExecutor, create_react_agent
from langchain import hub

from dotenv import load_dotenv
load_dotenv()  # loads .env file

from .prompt import SYSTEM_PROMPT
from core.model import model_gpt4o
from core.tools import search_science

tools = [search_science]

# _prompt = ChatPromptTemplate.from_messages([
#     ("system", SYSTEM_PROMPT),
#     MessagesPlaceholder(variable_name="history"),
#     ("human", "{human_input}"),
#     MessagesPlaceholder(variable_name="agent_scratchpad"),
# ])

prompt = hub.pull("hwchase17/react")
agent = create_react_agent(model_gpt4o, tools, prompt)
agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    input_variables=["input"]  # <-- can specify
)

print(agent_executor.invoke({"input": "hi"}))


