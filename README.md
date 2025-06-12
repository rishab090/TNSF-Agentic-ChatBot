### Steps Involved
1. Choose Model - Mistral
- Mistral - v2 - 7B

2. PDF files from Different Vendors - Manual/Warranty Card/TroubleShooting of equipment issue 
3. Parsing and Creating vector db in chroma.db
4. Embedding 


🧠 Objective
To build an AI-powered chatbot that can:

Ingest and understand various vendor-specific PDF manuals/warranty cards.

Answer user queries or troubleshoot equipment issues based on these documents.

## 🧰 System Components
### 1. PDF Preprocessing
Libraries: PyMuPDF, pdfplumber, or PyPDF2 for extracting text.

OCR (if scanned PDFs): Tesseract OCR via pytesseract.

### 2. Text Chunking & Embedding
Split the extracted text into chunks (e.g., 500–1000 tokens).

Use Embeddings (e.g., from OpenAI, Hugging Face, or sentence-transformers) to convert text to vector form for semantic search.

### 3. Vector Database
Use a vector store like FAISS, Weaviate, Pinecone, or Chroma to store embeddings.

Each chunk can be tagged with metadata (e.g., vendor, model, PDF source).

### 4. Retrieval-Augmented Generation (RAG)
On user query:

Embed the query.

Retrieve the top relevant chunks from the vector DB.

Feed those as context to an LLM (like GPT-4, Mistral, LLaMA, or local models).

### 5. Chatbot Backend
Framework: FastAPI, Flask, or LangChain.

Interface: Web (React/Next.js), Telegram, WhatsApp, or Teams integration.

Session/State management for conversation memory.