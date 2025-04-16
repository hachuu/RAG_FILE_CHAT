# frontend/app.py

import streamlit as st
from rag.loader import load_file, split_text
from rag.vector_store import create_vector_store
from rag.qa_engine import build_qa_chain
from langchain.memory import ConversationBufferMemory
from dotenv import load_dotenv
import os

load_dotenv()
st.set_page_config(page_title="📚 문서 기반 챗봇", layout="wide")
st.title("📂 문서 업로드 → AI 챗봇")

# 세션 상태 초기화
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "qa" not in st.session_state:
    st.session_state.qa = None
if "vectorstore_created" not in st.session_state:
    st.session_state.vectorstore_created = False
if "memory" not in st.session_state:
    st.session_state.memory = ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True
    )

# 파일 업로드
uploaded_file = st.file_uploader("📎 문서를 업로드하세요 (pdf, txt, xlsx, csv)", type=["pdf", "txt", "xlsx", "csv"])

if uploaded_file and not st.session_state.vectorstore_created:
    save_path = f"data/uploads/{uploaded_file.name}"
    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success("✅ 파일 업로드 완료!")

    # 텍스트 추출 및 벡터화
    with st.spinner("📚 벡터 생성 중..."):
        text = load_file(save_path)
        docs = split_text(text)
        vectorstore = create_vector_store(docs)
        qa = build_qa_chain(vectorstore, st.session_state.memory)
        st.session_state.qa = qa
        st.session_state.vectorstore_created = True
        st.success("✅ 문서 분석 완료! 이제 질문해보세요.")

# 대화 UI
if st.session_state.vectorstore_created:
    with st.form("chat_input_form", clear_on_submit=True):
        user_input = st.text_input("💬 궁금한 내용을 입력하세요", key="input")
        submitted = st.form_submit_button("전송")

        if submitted and user_input:
            with st.spinner("🤖 답변 생성 중..."):
                result = st.session_state.qa({"question": user_input})
                st.session_state.chat_history.append(("user", user_input))
                st.session_state.chat_history.append(("ai", result["answer"]))

    # 채팅 히스토리 출력
    for i, (sender, message) in enumerate(st.session_state.chat_history):
        if sender == "user":
            st.markdown(f"🧑‍💬 **나:** {message}")
        else:
            st.markdown(f"🤖 **AI:** {message}")

    # 🧠 문맥 디버깅용 출력
    with st.expander("🧠 대화 메모리 디버깅 보기"):
        memory = st.session_state.memory
        if memory.buffer:
            for msg in memory.buffer:
                role = "👤 사용자" if msg.type == "human" else "🤖 AI"
                st.markdown(f"**{role}:** {msg.content}")
        else:
            st.info("아직 대화 메모리가 비어 있어요.")
