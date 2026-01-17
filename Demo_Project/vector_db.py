from langchain_community.document_loaders import PyPDFLoader,DirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_core.vectorstores import VectorStoreRetriever
from langchain_classic.chains.retrieval_qa.base import RetrievalQA
import os
def add_new_resumes(folder_path):
    loader = DirectoryLoader(
        path=folder_path,
        glob="**/*.pdf",
        loader_cls=PyPDFLoader
    )
    new_docs = loader.load()

    vector_store.add_documents(new_docs)
    vector_store.save_local(FAISS_DB_PATH)

    print("New resumes added successfully")





