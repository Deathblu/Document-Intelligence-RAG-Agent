from langchain_community.document_loaders import PyPDFLoader


def load_pdf(path: str = "data/sample.pdf"):
    loader = PyPDFLoader(path)
    return loader.load()


if __name__ == "__main__":
    documents = load_pdf()
    print("\n First Page Content: \n")
    print(documents[0].page_content)

    print("\n Metadata: \n")
    print(documents[0].metadata)