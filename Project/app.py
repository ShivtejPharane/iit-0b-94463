import streamlit as st
from config import *
from loaders.loader_txt import load_txt_documents
from vectorstore.faiss_manage import FaissManager
from llm.llm import load_llm, load_embeddings
from rag.rag import build_context, ask_llm , build_chat_history

st.set_page_config(page_title="Sunbeam Chatbot", layout="wide")
st.title("Sunbeam Institute Chatbot")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

llm = load_llm()
embed_model = load_embeddings()

documents = load_txt_documents(DATA_PATH)

faiss_manager = FaissManager(FAISS_DB_PATH, embed_model)
vector_store = faiss_manager.load_or_create(documents)

query = st.chat_input("Ask about Sunbeam...")

if query:
    st.session_state.chat_history.append(
        {"role": "user", "content": query}
    )

    results = faiss_manager.search(query, k=5)
    context = build_context(results)

    history_text = build_chat_history(st.session_state.chat_history)

    answer = ask_llm(llm, context, query)

    st.session_state.chat_history.append(
        {"role": "assistant", "content": answer}
    )

for msg in st.session_state.chat_history:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])
