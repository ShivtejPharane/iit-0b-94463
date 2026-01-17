def build_context(docs):
    return "\n\n".join(f"SOURCE: {doc.metadata['file_name']}\n{doc.page_content}"for doc in docs)

def ask_llm(llm, context, question):
    prompt = f"""
You are a Sunbeam Institute chatbot.
Answer ONLY using the context below.
If the answer is not present, say "I don't know based on the available data".
Context:
{context}
Question:
{question}
"""
    return llm.invoke(prompt).content

def build_chat_history(chat_history):
    """
    Converts chat history into a formatted string
    suitable for LLM context.
    """
    history_text = ""

    for msg in chat_history:
        role = msg["role"]
        content = msg["content"]

        if role == "user":
            history_text += f"User: {content}\n"
        elif role == "assistant":
            history_text += f"Assistant: {content}\n"

    return history_text.strip()
