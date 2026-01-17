import os
from langchain_community.document_loaders import DirectoryLoader, TextLoader

def load_txt_documents(folder_path):
    loader = DirectoryLoader(
        path=folder_path,
        glob="**/*.txt",
        loader_cls=TextLoader,
        loader_kwargs={"encoding": "utf-8"}
    )

    documents = loader.load()

    for i, doc in enumerate(documents):
        source = doc.metadata["source"]
        file_name = os.path.splitext(os.path.basename(source))[0]

        doc.metadata["file_name"] = file_name
        doc.metadata["doc_id"] = f"{file_name}_{i}"

    return documents
