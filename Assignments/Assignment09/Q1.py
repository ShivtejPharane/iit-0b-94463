import streamlit as st
import pandas as pd
import pandasql as ps
from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
from langchain.tools import tool
import os
from dotenv import load_dotenv
load_dotenv()
st.title("CSV file SQL solver :")
file = st.file_uploader("Drag the File")    
llm = init_chat_model(
    model = "google/gemma-3n-e4b",
    model_provider="openai",
    base_url = "http://10.45.159.239:1234/v1/",
    api_key = "dummy"
)

csv_agent = create_agent(
    model = llm,
    system_prompt="You are an expert SQL Query solver. Only Query do not give any info",
    tools=[],
    middleware=[]
)
user_input = st.chat_input("You : ")
    
result = csv_agent.invoke({
    "messages": [
        {"role": "user", "content": user_input}
    ]
})
llm_output = result["messages"][-1]
print("AI: ", llm_output.content)
st.write(llm_output.content)
print("\n\n", result["messages"])