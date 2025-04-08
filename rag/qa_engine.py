# rag/qa_engine.py
from langchain.chains import RetrievalQA
from langchain_openai import ChatOpenAI

def build_qa_chain(vectorstore):
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
    llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.3)
    return RetrievalQA.from_chain_type(llm=llm, retriever=retriever, chain_type="stuff")
