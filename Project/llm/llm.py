from langchain.chat_models import init_chat_model
from langchain.embeddings import init_embeddings
from config import *

def load_llm():
    return init_chat_model(
        model=LLM_MODEL,
        model_provider="openai",
        base_url=BASE_URL,
        api_key=API_KEY
    )

def load_embeddings():
    return init_embeddings(
        model=EMBED_MODEL,
        provider="openai",
        base_url=BASE_URL,
        api_key=API_KEY,
        check_embedding_ctx_length=False
    )
