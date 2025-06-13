
from chromadb import PersistentClient
import pdfplumber
from sentence_transformers import SentenceTransformer
from model import PromptRequest
import settings


embed_model = SentenceTransformer(settings.e5_large_v2_path)
client = PersistentClient(path=settings.chroma_db_path)
collection = client.get_or_create_collection(name="manual_chunks")


def load_and_chunk_pdf(path, chunk_size=500):
    with pdfplumber.open(path) as pdf:
        text = "\n".join(page.extract_text() or "" for page in pdf.pages)

    # Simple chunking
    return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]


def embed_text(text):
    return embed_model.encode(text, normalize_embeddings=True)


def index_pdf():
    chunks = load_and_chunk_pdf(settings.pdf_file_path, chunk_size=500)
    texts = ["passage: " + chunk for chunk in chunks]
    embeddings = embed_model.encode(texts, normalize_embeddings=True, batch_size=16)
    for i, (chunk, emb) in enumerate(zip(chunks, embeddings)):
        collection.add(documents=[chunk], embeddings=[emb.tolist()], ids=[f"doc_{i}"])



def search_similar_docs(query: PromptRequest, k=3):
    q_embedding = embed_text("query: " + query.prompt)
    results = collection.query(query_embeddings=[q_embedding.tolist()], n_results=k)
    return results['documents'][0]
