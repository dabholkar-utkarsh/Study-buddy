from langchain_community.vectorstores import FAISS
from langchain_community.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain_openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain.schema import Document
import os

# Initialize embeddings
embeddings = OpenAIEmbeddings()
STORE_PATH = "faiss_store"

def process_pdf(file_path: str) -> list[Document]:
    """Load the PDF and return a list of Documents with page metadata."""
    loader = PyPDFLoader(file_path)
    docs: list[Document] = loader.load()
    return docs

def split_documents(documents):
    """Split into chunks at chapter boundaries first, then fallback to smaller pieces."""
    chapter_splitter = RecursiveCharacterTextSplitter(
        separators=["\nChapter", "\nCHAPTER", "\nchapter"],
        chunk_size=1500,
        chunk_overlap=200
    )
    interim_chunks = chapter_splitter.split_documents(documents)

    fallback_splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=100
    )
    final_chunks = fallback_splitter.split_documents(interim_chunks)
    return final_chunks

def create_faiss_store(chunks: list[Document], store_path="faiss_store") -> FAISS:
    """Embed and index all chunks; metadata (like 'page') is preserved."""
    vector_store = FAISS.from_documents(chunks, embeddings)
    vector_store.save_local(store_path)
    return vector_store

def load_retriever(store_path: str = STORE_PATH, k: int = 3):
    """Load (or re-load) your FAISS store and wrap it as a retriever."""
    if not os.path.exists(store_path):
        raise ValueError(f"No index found at {store_path}. Process a PDF first.")
    return FAISS.load_local(
        store_path,
        embeddings,
        allow_dangerous_deserialization=True
    ).as_retriever(search_kwargs={"k": k})

def make_qa_chain(model_name="gpt-3.5-turbo", temperature=0, k=3):
    """Build and return a RetrievalQA chain ready to answer queries."""
    retriever = load_retriever(k=k)
    llm = ChatOpenAI(model_name=model_name, temperature=temperature)
    return RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=True,
        chain_type="stuff"
    ) 