from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

loader = PyPDFLoader("data/rag_sample_doc.pdf")
documents = loader.load()

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50,
)

chunks  = text_splitter.split_documents(documents)

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

vectorsdb = Chroma.from_documents(
    documents=chunks,
    embedding=embedding_model,
    collection_name="sample_collection",
    persist_directory="./chroma_db"
)

print("Vector store created successfully!")

print("TESTING VECTOR STORE...")

query = "What is the main topic of the document?"

results = vectorsdb.similarity_search(query, k=3)

for i, res in enumerate(results):
    print(f"Result {i+1}:")
    print(res.page_content)
    print("-" * 50)