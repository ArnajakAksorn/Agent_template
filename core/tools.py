from langchain_core.tools import tool
from pymilvus import connections
from langchain_milvus import Milvus

from core.model import embedding_large
from core.config import MILVUS_DB_URI

connections.connect(
    alias="default",
    uri=MILVUS_DB_URI,  # your IP and port
)

vectorstore = Milvus(
    embedding_function=embedding_large,
    collection_name="ScienceG7_9_andHealth_G11",
    connection_args={
        "uri": MILVUS_DB_URI,
        "user": "",
        "password": "",
        "secure": False,
    }
)
retriever = vectorstore.as_retriever()

@tool
def search_science(query: str, k: int = 3) -> str:
    """
    Search for the most relevant documents in the Science Book.
    
    Args:
        query (str): The query string to search for.
        k (int): The number of top results to return.
        
    Returns:
        str: The content of the most relevant document.
    """
    docs = retriever.get_relevant_documents(query)
    return docs