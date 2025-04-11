# app/config.py
import os

CHAT_HISTORY_PATH = os.getenv("CHAT_HISTORY_PATH", "chat_histories")
MILVUS_DB_URI = os.getenv("MILVUS_DB_URI")

