import os
from pathlib import Path
from dotenv import load_dotenv
from pypdf import PdfReader
import chromadb
from chromadb.utils import embedding_functions

embedding_function = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"
)

print("OPENAI:", os.getenv("OPENAI_API_KEY"))
print("CHROMA:", os.getenv("CHROMA_OPENAI_API_KEY"))

CHROMA_PATH = "vectorstore"
COLLECTION_NAME = "documentos_estudio"





def extract_text_from_pdf(pdf_path: str) -> str:
    reader = PdfReader(pdf_path)
    text = ""

    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"

    return text


def split_text(text: str, chunk_size: int = 800, overlap: int = 150) -> list[str]:
    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)
        start += chunk_size - overlap

    return chunks


def get_collection():
    client = chromadb.PersistentClient(path=CHROMA_PATH)

    collection = client.get_or_create_collection(
        name=COLLECTION_NAME,
        embedding_function=embedding_function
    )

    return collection


def index_pdf(pdf_path: str):
    collection = get_collection()

    text = extract_text_from_pdf(pdf_path)
    chunks = split_text(text)

    ids = []
    metadatas = []

    filename = os.path.basename(pdf_path)

    for i, chunk in enumerate(chunks):
        ids.append(f"{filename}_{i}")
        metadatas.append({
            "source": filename,
            "chunk": i
        })

    collection.add(
        documents=chunks,
        ids=ids,
        metadatas=metadatas
    )

    return len(chunks)


def search_context(question: str, k: int = 4):
    collection = get_collection()

    results = collection.query(
        query_texts=[question],
        n_results=k
    )

    documents = results["documents"][0]
    metadatas = results["metadatas"][0]

    context = "\n\n".join(documents)

    sources = [
        f"{metadata['source']} - fragmento {metadata['chunk']}"
        for metadata in metadatas
    ]

    return context, sources