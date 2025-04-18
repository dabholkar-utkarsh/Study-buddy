import os
from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS
from langchain_community.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA

load_dotenv()
from langchain_openai import OpenAIEmbeddings
embeddings = OpenAIEmbeddings()

STORE_PATH = "faiss_store"

def load_retriever(store_path: str = STORE_PATH, k: int = 3):
    """
    Load (or re-load) your FAISS store and wrap it as a retriever.
    """
    if not os.path.exists(store_path):
        raise ValueError(f"No index found at {store_path}. Run DB_pipline first.")
    return FAISS.load_local(
        store_path,
        embeddings,
        allow_dangerous_deserialization=True  # <- add this
    ).as_retriever(search_kwargs={"k": k})

def make_qa_chain(model_name="gpt-3.5-turbo", temperature=0, k=3):
    """
    Build and return a RetrievalQA chain ready to answer queries.
    """
    retriever = load_retriever(k=k)
    llm = ChatOpenAI(model_name=model_name, temperature=temperature)
    return RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=True,
        chain_type="stuff"
    )

if __name__ == "__main__":
    qa = make_qa_chain()
    question = input("Ask your study buddy: ")
    result = qa(question)
    print("\nAnswer:\n", result["result"], "\n")
    print("Sources:")
    for doc in result["source_documents"]:
        print("-", doc.metadata.get("source"), "…")
    