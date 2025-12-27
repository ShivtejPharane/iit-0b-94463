import streamlit as st
import pandas as pd
import pandasql as ps
from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
from langchain.tools import tool
import os
from dotenv import load_dotenv
load_dotenv()



llm = init_chat_model(
    model = "",
    model_provider="",
    base_url ="",
    api_key = "dummy_key"
)
agent = create_agent(
    model=llm,
    tools=[csv],
    system_prompt=""
)

conversation=[]
while True:
    user_input = input("Ask any thing : ")
    if user_input == "exit":
        break
    