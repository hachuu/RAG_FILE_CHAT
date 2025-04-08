# 모델 설명 : RAG (Retrieval-Augmented Generation)
## RAG (Retrieval-Augmented Generation) 모델은 대량의 비정형 데이터에서 정보를 검색하고, 이를 바탕으로 질문에 대한 답변을 생성하는 모델입니다.

## ✅ 목표 기능 요약
### 1. 📂 파일 업로드 (PDF, TXT)
### 2. 📄 텍스트 추출 & chunk 나누기
### 3. 🧠 벡터화 (embedding)
### 4. 💾 벡터 저장 (FAISS)
### 5. ❓ 질문 입력 → 검색 + LLM 응답
### 6. 📱 Streamlit UI로 전부 연결

## 📁 전체 구조 설계
```bash
rag_file_chat/
├── frontend/
│   └── app.py                  ← 📱 Streamlit UI
├── rag/
│   ├── loader.py               ← 📄 PDF, TXT 읽기 + chunk
│   ├── vector_store.py         ← 🧠 벡터화 + 저장/로드
│   └── qa_engine.py            ← ❓ 질문 → 응답
├── data/
│   ├── uploads/                ← 📂 업로드된 원본 파일
│   └── vectors/                ← 💾 벡터 저장소
├── .env                        ← 🔐 API 키
└── requirements.txt
```

## 실행 방법
```bash
$env:PYTHONPATH="."; streamlit run frontend/app.py   # Windows PowerShell
```