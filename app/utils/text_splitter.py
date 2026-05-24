from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


def split_pdf(path: str = "data/sample.pdf"):
    loader = PyPDFLoader(path)
    documents = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50,
    )

    return text_splitter.split_documents(documents)


if __name__ == "__main__":
    chunks = split_pdf()

    print(f"Total chunks created: {len(chunks)} \n")

    print("First chunk content: \n")
    print(chunks[0].page_content)
    print("\n\nSecond chunk content: \n")
    print(chunks[1].page_content)
    print("\n\nLast chunk content: \n")
    print(chunks[-1].page_content)  