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
│   └── app.py                  ← 📱 Streamlit UI, 사용자 입력 및 응답 출력
├── rag/
│   ├── loader.py               ← 📄 PDF, TXT 읽기 + chunk 나누기
│   ├── vector_store.py         ← 🧠 텍스트 임베딩 + 벡터 저장/로드
│   └── qa_engine.py            ← ❓ RAG 기반 질문 처리 + 🧾 사용자 질문/응답 기록 관리 (Chat Memory)
├── data/
│   ├── uploads/                ← 📂 업로드된 원본 문서 저장
│   └── vectors/                ← 💾 벡터 DB 저장소
├── .env                        ← 🔐 API 키 등 민감 정보
└── requirements.txt            ← 📦 패키지 의존성 목록
```

## 실행 방법
```bash
$env:PYTHONPATH="."; streamlit run frontend/app.py   # Windows PowerShell
```