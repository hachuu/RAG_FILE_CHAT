# rag/loader.py
import os
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
import pandas as pd

def load_file(file_path):
    ext = os.path.splitext(file_path)[-1].lower()
    if ext == ".pdf":
        reader = PdfReader(file_path)
        text = "\n".join([page.extract_text() or "" for page in reader.pages])
    elif ext == ".txt":
        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()
    elif ext == ".xlsx":
        df = pd.read_excel(file_path)
        text = "\n".join(df.astype(str).values.flatten())
    elif ext == ".csv":
        import pandas as pd
        df = pd.read_csv(file_path)
        text = "\n".join(df.astype(str).values.flatten())
    else:
        raise ValueError("Unsupported file type")
    return text

def split_text(text):
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    return splitter.create_documents([text])
