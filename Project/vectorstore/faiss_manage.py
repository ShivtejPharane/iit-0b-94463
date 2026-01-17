import os
from langchain_community.vectorstores import FAISS

class FaissManager:

    def __init__(self, db_path, embed_model):
        self.db_path = db_path
        self.embed_model = embed_model
        self.vector_store = None

    def load_or_create(self, documents=None):
        if os.path.exists(self.db_path):
            self.vector_store = FAISS.load_local(
                self.db_path,
                self.embed_model,
                allow_dangerous_deserialization=True
            )
        else:
            self.vector_store = FAISS.from_documents(documents, self.embed_model)
            self.vector_store.save_local(self.db_path)

        return self.vector_store

    def search(self, query, k=5):
        return self.vector_store.similarity_search(query, k=k)


    def add_documents(self, documents):
        self.vector_store.add_documents(documents)
        self.vector_store.save_local(self.db_path)

    def delete_and_rebuild(self, documents):
        self.vector_store = FAISS.from_documents(documents, self.embed_model)
        self.vector_store.save_local(self.db_path)
