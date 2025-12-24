from langchain_community.document_loaders import PyPDFLoader
from langchain.embeddings import init_embeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
embed_model = init_embeddings(
    model="text-embedding-nomic-embed-text-v1.5",
    provider="openai",
    base_url = "http://192.168.1.105:1234/v1",
    api_key = "dummy",
    check_embedding_ctx_length = False
)

def load_pdf_resume(path):
    loader = PyPDFLoader(path)
    docs = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=50,chunk_overlap = 10,separators=["\n\n","\n"," "])
    split_docs = text_splitter.split_documents(docs)
    #
    metadata = {
        "source" : path,
        "page_count" : len(docs)
    }
    return split_docs,metadata

file_path = "E:\sunbeam\IIT-08-B-GenAI\day08\\resume-011.pdf"
resume_text,resume_info = load_pdf_resume(file_path)

resume_embeddings = embed_model.embed_documents([resume_text])
for embedding in resume_embeddings:
    print(f"len = {len(embedding)} --> {embedding[:4]}")
