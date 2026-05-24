from dotenv import load_dotenv
import os
from pydantic import SecretStr

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma 
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from langchain_classic.chains import RetrievalQA

load_dotenv()

loader = PyPDFLoader("data/rag_sample_doc.pdf")
docs = loader.load()


text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50,
)

chunks = text_splitter.split_documents(docs)

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

groq_api_key = os.getenv("GROQ_API_KEY")
if groq_api_key is None:
    raise ValueError("Missing GROQ_API_KEY environment variable")

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.7,
    
    api_key=SecretStr(groq_api_key)
)

vector_db = None

def create_vecor_db(pdf_path):
    global vector_db

    loader = PyPDFLoader(pdf_path)
    docs = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50,
    )
    
    chunks = text_splitter.split_documents(docs)

    vector_db = Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        collection_name="pdf_chunks",
        persist_directory="./chroma_db"
    )

    return "Vector database created successfully."

def query_vector_db(query):
    global vector_db
    if vector_db is None:
        raise ValueError("Vector database is not initialized. Call create_vecor_db(pdf_path) first.")

    retriever = vector_db.as_retriever()

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=True
    )

    response = qa_chain.invoke(query)

    return response["result"]   