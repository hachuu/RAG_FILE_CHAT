# rag/vector_store.py
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
import os

def create_vector_store(documents, persist_dir="data/vectors"):
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_documents(documents, embeddings)
    vectorstore.save_local(persist_dir)
    return vectorstore

def load_vector_store(persist_dir="data/vectors"):
    embeddings = OpenAIEmbeddings()
    return FAISS.load_local(persist_dir, embeddings, allow_dangerous_deserialization=True)
