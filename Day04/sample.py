import os
import requests
import json
import time
from dotenv import load_dotenv
import streamlit as st

# ------------------ CONFIG ------------------
st.set_page_config(page_title="Chat GPT", layout="wide")

load_dotenv()
api_key = "dummy-key"

url = "http://192.168.43.239:1234/v1/chat/completions"
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

# ------------------ FUNCTIONS ------------------
def call_model(model_name, user_prompt):
    req_data = {
        "model": model_name,
        "messages": [
            {"role": "user", "content": user_prompt}
        ]
    }

    start = time.perf_counter()
    response = requests.post(url, json=req_data, headers=headers)
    end = time.perf_counter()

    st.caption(f"⏱ Time taken: {end - start:.2f} seconds")

    if response.status_code == 200:
        resp = response.json()
        return resp["choices"][0]["message"]["content"]
    else:
        return f"Error: {response.status_code}"

# ------------------ UI ------------------
st.title("💬 Chat GPT")

with st.sidebar:
    st.header("⚙ Settings")
    model_choice = st.radio(
        "Choose Model",
        ["Online Model", "Offline Model"]
    )

# Chat input (ONE input, no loop)
user_prompt = st.text_input("Ask anything:")

if user_prompt:
    if user_prompt.lower() == "exit":
        st.stop()

    if model_choice == "Online Model":
        model = "llama-3.3-70b-versatile"
    else:
        model = "google/gemma-3n-e4b"

    with st.spinner("Thinking..."):
        reply = call_model(model, user_prompt)
        st.write(reply)
