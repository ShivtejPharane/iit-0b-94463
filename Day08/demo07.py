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
#loader = PyPDFLoader(r"E:\sunbeam\IIT-08-B-GenAI\day08\resume-001.pdf")
loader = DirectoryLoader(
                         path="E:\Internship\Git_hub_repo\iit-0b-94463\Day08\Resumes",
                         glob="**/*.pdf",
                         loader_cls=PyPDFLoader
                         )
documents = loader.load()
docs = documents
#text_splitter = RecursiveCharacterTextSplitter(chunk_size =500,chunk_overlap = 50,separators=["\n\n","\n"," "])
#docs = text_splitter.split_documents(documents)
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

vector_store = FAISS.from_documents(docs,embed_model)
q = input("Enter the Query : ")
results_query = vector_store.similarity_search(q,k=5)
agent = create_agent(
    model=llm,
    tools=[],
    system_prompt=f"You are an HR of company ,from {q} "
)
# for resume in results_query:
#     print(resume.page_content,"\n\n")

# retriever = vector_store.as_retriever()
# qa = RetrievalQA.from_chain_type(llm,chain_type="stuff",retriever=retriever)
# answer = qa.invoke("give only top resumes with their names")
# print(answer)
# chain = load_qa_chain(llm, chain_type="stuff")
# answer = chain.run(
#     input_documents=results_query,
#     question="Give only top resumes with their names"
# )
# qa = RetrievalQA.from_chain_type(
#     llm=llm,
#     chain_type="stuff",
#     retriever=vector_store.as_retriever(search_kwargs={"k": 5})
# )

# answer = qa.invoke(
#     "Give only the top web developer resumes with their names"
# )
answer = agent.invoke({
    "messages": [
        {"role": "user", "content": "give only top resumes with their names "}
    ]
})

print(answer["messages"][-1].content)


