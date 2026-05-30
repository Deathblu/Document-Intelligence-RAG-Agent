# 🤖 Document Intelligence RAG Agent

AI-powered document understanding and conversational retrieval system built using **LangChain**, **ChromaDB**, **FastAPI**, **Streamlit**, and **Groq LLMs**.

---

# 📌 Overview

Document Intelligence RAG Agent allows users to:

- Upload PDF documents
- Perform semantic search on document content
- Ask natural language questions
- Retrieve context-aware AI-generated answers

The system uses a **Retrieval-Augmented Generation (RAG)** pipeline to combine vector search with Large Language Models for accurate responses.

---

# 🚀 Features

✅ PDF Upload & Processing
✅ Semantic Document Search
✅ Conversational AI Q&A
✅ Vector Embeddings using Sentence Transformers
✅ ChromaDB Vector Store
✅ FastAPI Backend
✅ Streamlit Interactive UI
✅ Groq LLM Integration
✅ Modern Glassmorphism UI
✅ Dark-Themed AI Interface

---

# 🛠️ Tech Stack

| Technology            | Purpose                    |
| --------------------- | -------------------------- |
| Python                | Core programming language  |
| LangChain             | RAG pipeline orchestration |
| ChromaDB              | Vector database            |
| Sentence Transformers | Embedding generation       |
| FastAPI               | Backend API                |
| Streamlit             | Frontend UI                |
| Groq API              | LLM inference              |
| PyPDF                 | PDF text extraction        |

---

# 🧠 RAG Architecture

```text
PDF Upload
    ↓
Text Extraction
    ↓
Chunking
    ↓
Embeddings Generation
    ↓
ChromaDB Vector Storage
    ↓
Similarity Search
    ↓
Relevant Context Retrieval
    ↓
LLM Response Generation
```

---

# 📂 Project Structure

```text
rag-agent/
│
├── app/
│   ├── services/
│   ├── utils/
│   ├── uploads/
│
├── frontend/
│   └── frontend.py
│
├── .streamlit/
│   └── config.toml
│
├── requirements.txt
│
└── README.md
```

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone <YOUR_GITHUB_REPO_URL>
cd rag-agent
```

---

## 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate environment:

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_api_key_here
```

---

# ▶️ Run Backend

```bash
uvicorn app.main:app --reload
```

Backend runs on:

```text
http://127.0.0.1:8000
```

---

# ▶️ Run Frontend

```bash
streamlit run frontend/frontend.py
```

Frontend runs on:

```text
http://localhost:8501
```

---

# 📸 Application Preview

## Main Interface

> Add your screenshot here

```text
README_images/app_preview.png
```

Example Markdown after adding screenshot:

```md
![App Preview](README_images/app_preview.png)
```

---

# 💡 Example Workflow

1. Upload PDF document
2. System extracts and indexes content
3. Ask questions in chat
4. AI retrieves relevant chunks
5. LLM generates contextual answer

---

# 📈 Future Improvements

- Multi-document support
- Conversation memory
- Authentication system
- Cloud deployment
- Source citation highlighting
- OCR support for scanned PDFs
- Hybrid search (BM25 + Vector)

---

# 🧪 Sample Queries

```text
Summarize this document
What are the key findings?
Explain the methodology section
What technologies are discussed?
```

---

# 👨‍💻 Author

Built by Anurag Wanwe

---

# 📄 License

This project is for educational and portfolio purposes.
