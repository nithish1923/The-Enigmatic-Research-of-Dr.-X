import chromadb
from chromadb.config import Settings

def get_vector_db():
    client = chromadb.Client(Settings(
        chroma_db_impl='duckdb+parquet',
        persist_directory='./chroma_store'
    ))
    return client
