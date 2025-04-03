# 🤖 AI-Powered Document Search and Chatbot Developement

A document-based Q&A system that leverages **Mistral AI via Ollama**, **LangChain**, **ChromaDB**, and **Streamlit** to create an interactive assistant capable of understanding and answering questions from uploaded PDF, DOCX, or TXT files.

---

## 📌 Features

- Upload documents and extract text from PDFs, Word files, or plain text
- Store document embeddings in **ChromaDB**
- Use **sentence-transformers** for semantic understanding
- Ask natural language questions via a web UI
- Get AI-powered answers using **Mistral LLM** (running locally via Ollama)
- Built with **FastAPI** for backend and **Streamlit** for the frontend

---

## 🧠 Tech Stack

- **Frontend:** Streamlit
- **Backend:** FastAPI
- **LLM:** Mistral (via Ollama)
- **Vector DB:** ChromaDB
- **Embeddings:** Sentence Transformers (`all-mpnet-base-v2`)
- **Document Parsing:** PyMuPDF, python-docx
- **Libraries:** LangChain, HuggingFace, Requests, Uvicorn

---

## 📁 Project Structure

```
├── app.py              # FastAPI backend for LLM-powered Q&A
├── app_ui.py           # Streamlit frontend for interaction
├── textextracter.py    # Utility to extract, embed, and query documents
├── testmistral.py      # Quick Mistral test via API
├── test_query.py       # Sample API call to backend
├── requirements.txt    # Python dependencies
├── sample_pdf.pdf      # Sample file to test PDF extraction
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/your-repo.git
cd your-repo
```

### 2. Install Requirements

```bash
pip install -r requirements.txt
```

> 📦 Make sure `ollama` is installed and running locally.

### 3. Start Ollama & Pull Mistral

```bash
ollama run mistral
```

### 4. Run FastAPI Server

```bash
uvicorn app:app --reload
```

### 5. Launch Streamlit UI

```bash
streamlit run app_ui.py
```

---

## 🌐 API Endpoints

- `POST /query`  
  **Body:** `{ "query": "Your question here" }`  
  **Returns:** JSON with AI-generated answer

- `GET /`  
  Health check for FastAPI

---

## 🧪 Sample Query

```bash
curl -X POST http://127.0.0.1:8000/query \
     -H "Content-Type: application/json" \
     -d '{"query": "What is Dinakar’s education background?"}'
```

---

## 🧰 Requirements

See `requirements.txt`:
```text
fastapi
ollama
langchain
pymupdf
pypdf
requests
streamlit
chromadb
uvicorn
python_docx
```

## 🏁 Future Enhancements

- Add authentication to secure uploads
- Support more file types (e.g., Excel, HTML)
- Deploy on cloud (AWS/GCP)
- Add chat history for Q&A sessions

---

⭐ Star the repo if you found it useful — contributions welcome!
```
