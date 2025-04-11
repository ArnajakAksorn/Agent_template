# app/adapters/chat_history/file_history.py
from pathlib import Path
from langchain_community.chat_message_histories import FileChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from typing import Callable, Union

def _is_valid_identifier(value: str) -> bool:
    import re
    valid_characters = re.compile(r"^[a-zA-Z0-9-_]+$")
    return bool(valid_characters.match(value))

def create_session_factory(
    base_dir: Union[str, Path],
) -> Callable[[str, str], BaseChatMessageHistory]:
    base_dir = Path(base_dir) if isinstance(base_dir, str) else base_dir
    base_dir.mkdir(parents=True, exist_ok=True)

    def get_chat_history(user_id: str, conversation_id: str) -> FileChatMessageHistory:
        if not _is_valid_identifier(user_id) or not _is_valid_identifier(conversation_id):
            raise ValueError("Invalid user_id or conversation_id format")
        user_dir = base_dir / user_id
        user_dir.mkdir(parents=True, exist_ok=True)
        file_path = user_dir / f"{conversation_id}.json"
        return FileChatMessageHistory(str(file_path))

    return get_chat_history
