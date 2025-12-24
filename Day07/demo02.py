from langchain_openai import OpenAIEmbeddings
import numpy as np

def cosine_similarity(a,b):
    return np.dot(a,b)/(np.linalg.norm(a) * np.linalg.norm(b))

embed_model = OpenAIEmbeddings(
    model = "text-embedding-nomic-embed-text-v1.5",
    base_url="http://192.168.1.105:1234/v1",
    api_key="dummy",
    check_embedding_ctx_length=False
)
sentences = [
    "I love football.",
    "Soccer is my favorite sports.",
    "Messi talks spanish."
]
embedings = embed_model.embed_documents(sentences)
print("1 and 2 : ",cosine_similarity(embedings[0],embedings[1]))
print("2 and 3 : ",cosine_similarity(embedings[1],embedings[2]))
print("3 and 1 : ",cosine_similarity(embedings[2],embedings[0]))