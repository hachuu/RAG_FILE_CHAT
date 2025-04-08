# frontend/app.py
import streamlit as st
from rag.loader import load_file, split_text
from rag.vector_store import create_vector_store, load_vector_store
from rag.qa_engine import build_qa_chain
import os
from dotenv import load_dotenv

load_dotenv()
st.set_page_config(page_title="📚 문서 기반 챗봇", layout="wide")

st.title("📂 문서 업로드 → AI 질문응답")

uploaded_file = st.file_uploader("xlsx, csv, PDF 또는 TXT 파일 업로드", type=["pdf", "txt", "xlsx", "csv"])
question = st.text_input("궁금한 내용을 입력하세요")

if uploaded_file:
    # 파일 저장
    save_path = f"data/uploads/{uploaded_file.name}"
    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success("✅ 파일 업로드 완료")

    # 벡터 생성
    with st.spinner("📚 벡터 생성 중..."):
        text = load_file(save_path)
        docs = split_text(text)
        vectorstore = create_vector_store(docs)
        st.success("✅ 벡터 저장 완료!")

    # 질문 응답 가능
    if question:
        with st.spinner("🤖 답변 생성 중..."):
            qa = build_qa_chain(vectorstore)
            answer = qa.run(question)
            st.markdown(f"### 💬 답변: \n\n{answer}")
