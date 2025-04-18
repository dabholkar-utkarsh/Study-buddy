import os
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter, CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFLoader
from langchain.schema import Document

# Load environment variables
load_dotenv()

def process_pdf(file_path: str) -> list[Document]:
    """
    Load the PDF and return a list of Documents with page metadata.
    """
    loader = PyPDFLoader(file_path)
    docs: list[Document] = loader.load()  # each doc.metadata["page"] is set
    return docs

def split_documents(documents):
    """
    Split into chunks at chapter boundaries first, then fallback to smaller pieces.
    """
    # 1) Split on "Chapter" headings
    chapter_splitter = RecursiveCharacterTextSplitter(
        separators=["\nChapter", "\nCHAPTER", "\nchapter"],
        chunk_size=1500,
        chunk_overlap=200
    )
    interim_chunks = chapter_splitter.split_documents(documents)

    # 2) If any chunk is still too large, split it down further
    fallback_splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=100
    )
    final_chunks = fallback_splitter.split_documents(interim_chunks)
    return final_chunks

def create_faiss_store(chunks: list[Document], store_path="faiss_store") -> FAISS:
    """
    Embed and index all chunks; metadata (like 'page') is preserved.
    """
    embeddings = OpenAIEmbeddings()
    vector_store = FAISS.from_documents(chunks, embeddings)
    vector_store.save_local(store_path)
    return vector_store

def process_and_store_pdf(file_path: str) -> FAISS:
    docs = process_pdf(file_path)
    chunks = split_documents(docs)
    return create_faiss_store(chunks)

if __name__ == "__main__":
    pdf_file = "AI_Engineering.pdf"
    vs = process_and_store_pdf(pdf_file)

    # Example: only search Chapter 1 (assume Chapter 1 spans pages 1–20)
    query = "what key concepts does Chapter 1 introduce?"
    # Use similarity_search with a metadata filter
    results = vs.similarity_search(
        query,
        k=3,
        filter={"page": {"$gte": 1, "$lte": 20}}
    )

    print("Top 3 Chapter 1 results:")
    for i, doc in enumerate(results, 1):
        print(f"\n— Result {i} (page {doc.metadata['page']}) —")
        print(doc.page_content.strip())
        print("-" * 80)
