# core/schemas.py
from typing_extensions import TypedDict

class InputChat(TypedDict):
    """Input for the chat endpoint."""
    human_input: str
