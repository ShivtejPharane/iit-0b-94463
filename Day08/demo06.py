from langchain_openai import OpenAI
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.vectorstores import VectorStoreRetriever
from langchain_classic.chains.retrieval_qa.base import RetrievalQA
import os
from langchain.embeddings import init_embeddings
loader = TextLoader(r"E:\Internship\Git_hub_repo\iit-0b-94463\Day08\cricket.txt")
documents = loader.load()
text_splitter = RecursiveCharacterTextSplitter(chunk_size = 100,chunk_overlap = 20,separators=["\n\n","\n"," "])
docs = text_splitter.split_documents(documents)
#print(docs[0])
llm = init_embeddings(
    model="google/gemma-3n-e4b",
    provider="openai",
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
library = FAISS.from_documents(docs,embed_model)
print(type(library))
q = input("Enter the Query : ")
results = library.similarity_search(q,k=3)
#print(library.similarity_search(input("Enter the Query : "))[0].page_content)
for i in results:
    docs_scores = library.similarity_search_with_score(q)
    print(i.page_content,"\n\n")
print(docs_scores[0])
library.save_local("demo06")
demo06_saved = FAISS.load_local("demo06",embed_model)
# retriver = library.as_retriever()
# qa = RetrievalQA.from_chain_type(llm,chain_type="stuff",retriver=retriver)
# result = qa.invoke("if answer is not proper give me like dont know")
# print(results)

