from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.runnables import ConfigurableFieldSpec

from core.config import CHAT_HISTORY_PATH
from core.adapters.chat_history.file_history import create_session_factory
from core.schemas import InputChat 
from core.agents import pirate_chain

def wrap_chain_with_history(chain) -> RunnableWithMessageHistory:
    return RunnableWithMessageHistory(
        chain,
        create_session_factory(CHAT_HISTORY_PATH),
        input_messages_key="human_input",
        history_messages_key="history",
        history_factory_config=[
            ConfigurableFieldSpec(
                id="user_id",
                annotation=str,
                name="User ID",
                description="Unique identifier for the user.",
                default="",
                is_shared=True,
            ),
            ConfigurableFieldSpec(
                id="conversation_id",
                annotation=str,
                name="Conversation ID",
                description="Unique identifier for the conversation.",
                default="",
                is_shared=True,
            ),
        ],
    ).with_types(input_type=InputChat)


pirate_chain_with_history = wrap_chain_with_history(pirate_chain)
