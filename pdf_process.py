from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema.document import Document

def load_all_pdfs(pdf_paths):
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    all_chunks = []

    for path in pdf_paths:
        loader = PyPDFLoader(path)
        docs = loader.load()
        # Add vendor metadata
        for doc in docs:
            doc.metadata["source"] = path
            doc.metadata["vendor"] = get_vendor_from_filename(path)
        chunks = splitter.split_documents(docs)
        all_chunks.extend(chunks)
    
    return all_chunks
