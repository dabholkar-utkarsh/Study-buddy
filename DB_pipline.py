import os
import io
import PyPDF2
import openai
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFLoader

# Load environment variables from .env file
load_dotenv()

# Initialize the embedding model using API key from .env
embeddings = OpenAIEmbeddings()  # It will automatically use OPENAI_API_KEY from environment

# --- Step 1: Load and Process PDF ---

def process_pdf(file_path):
    """
    Given a path to a PDF file, load the file and extract its documents.
    """
    loader = PyPDFLoader(file_path)
    documents = loader.load()
    return documents

# --- Step 2: Clean and Chunk the Text ---

def split_documents(documents):
    """
    Split documents into smaller chunks with optional overlap.
    """
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,      # Adjust chunk size as needed
        chunk_overlap=100     # Overlap to help preserve context
    )
    docs = text_splitter.split_documents(documents)
    return docs

# --- Step 3: Create FAISS Vector Store ---

def create_faiss_store(docs, store_path="faiss_store"):
    """
    Create a FAISS vector store from document chunks.
    """
    # Set up your embeddings model
    embeddings = OpenAIEmbeddings()
    
    # Initialize or create the FAISS index
    vector_store = FAISS.from_documents(docs, embeddings)
    
    # Save the vector store locally
    vector_store.save_local(store_path)
    return vector_store

# --- Step 4: Assemble the Pipeline ---

def process_and_store_pdf(file_path):
    """
    End-to-end processing of a PDF: extract, split, embed, and store in FAISS.
    """
    # Load the PDF file and extract its contents
    documents = process_pdf(file_path)
    
    # Split the documents into chunks
    docs = split_documents(documents)
    
    # Create and store embeddings in FAISS vector store
    vector_store = create_faiss_store(docs)
    return vector_store

# --- Step 5: Example Usage and Testing ---

if __name__ == "__main__":
    pdf_file_path = "AI_Engineering.pdf"  # Replace with the actual PDF file path
    vector_store = process_and_store_pdf(pdf_file_path)
    
    # Now, test the vector store with a query
    query = "talk about key concepts on the book"
    results = vector_store.similarity_search(query, k=3)
    
    print("Top 3 search results:")
    for i, res in enumerate(results):
        print(f"Result {i+1}:")
        print(res.page_content)
        print("-" * 80)
