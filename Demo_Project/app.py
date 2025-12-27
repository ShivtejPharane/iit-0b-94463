from langchain_openai import OpenAI
from langchain_community.document_loaders import PyPDFLoader,DirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.vectorstores import VectorStoreRetriever
from langchain.embeddings import init_embeddings
from langchain_classic.chains.retrieval_qa.base import RetrievalQA
from langchain.chat_models import init_chat_model
import os
from langchain.agents import create_agent
from langchain_classic.chains.question_answering import load_qa_chain


PDF_PATH = r"E:\Internship\Git_hub_repo\iit-0b-94463\Day08\Resumes"
FAISS_DB_PATH = "faiss_resume_db"


loader = DirectoryLoader(
     path="E:\Internship\Git_hub_repo\iit-0b-94463\Day08\Resumes",
     glob="**/*.pdf",
     loader_cls=PyPDFLoader
    )
documents = loader.load()
docs = documents

def add_new_resumes(folder_path):
    loader = DirectoryLoader(
        path=folder_path,
        glob="**/*.pdf",
        loader_cls=PyPDFLoader
    )
    new_docs = loader.load()

    vector_store.add_documents(new_docs)
    vector_store.save_local(FAISS_DB_PATH)

    print("✅ New resumes added successfully")

    
llm = init_chat_model(
    model="google/gemma-3n-e4b",
    model_provider="openai",
    base_url="http://127.0.0.1:1234/v1",
    api_key = "dummy"
)


embed_model = init_embeddings(
    model="text-embedding-nomic-embed-text-v1.5",
    provider="openai",
    base_url = "http://127.0.0.1:1234/v1",
    api_key = "dummy",
    check_embedding_ctx_length = False
)


if os.path.exists(FAISS_DB_PATH):
    print("Loading existing FAISS database...")
    vector_store = FAISS.load_local(
        FAISS_DB_PATH,
        embed_model,
        allow_dangerous_deserialization=True
    )
else:
    print("Creating new FAISS database...")
    vector_store = FAISS.from_documents(documents, embed_model)
    vector_store.save_local(FAISS_DB_PATH)
    print("FAISS database saved locally")


q = input("Enter the Query : ")
results_query = vector_store.similarity_search(q, k=5)
resume_text = "\n\n".join([doc.page_content for doc in results_query])


agent = create_agent(
    model=llm,
    tools=[],
    system_prompt=f"""
You are an HR recruiter.
Below are candidate resumes:{resume_text}
Select the best candidates based on this requirement:{q}
Explain clearly why you selected them.
"""
)


answer = agent.invoke({
    "messages": [
        {"role": "user", "content": "give only top resumes with their names "}
    ]
})
print(answer["messages"][-1].content)

