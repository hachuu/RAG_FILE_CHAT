# rag/qa_engine.py
from langchain.chains import ConversationalRetrievalChain
from langchain_community.chat_models import ChatOpenAI

def build_qa_chain(vectorstore, memory=None):
    llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

    if memory:
        qa_chain = ConversationalRetrievalChain.from_llm(
            llm=llm,
            retriever=vectorstore.as_retriever(),
            memory=memory,
            return_source_documents=False
        )
    else:
        from langchain.chains import RetrievalQA  # fallback용
        qa_chain = RetrievalQA.from_chain_type(
            llm=llm,
            retriever=vectorstore.as_retriever()
        )

    return qa_chain
