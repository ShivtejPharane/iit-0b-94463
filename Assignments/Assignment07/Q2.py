# Input city name from user.
# Get current weather from weather API.
# Ask LLM to explain the weather in English.
from langchain.chat_models import init_chat_model   
import streamlit as st
import requests
from dotenv import load_dotenv
import os
load_dotenv()
llm = init_chat_model(
    model="google/gemma-3n-e4b",
    model_provider="openai",
    base_url = "http://192.168.1.109:1234/v1",
    api_key = "dummy"
)
def Weather():
    city = st.text_input("Enter the City ")
    if st.button("Get weather"):
        llm_msg = f'''
        From the city {city}
        Give the weather in simple points
        '''
        result = llm.invoke(llm_msg)
        st.write(result.content)
        print(result.content)
#main

if "login" not in st.session_state:
    st.session_state.login = False

st.title("Login")

if not st.session_state.login:
    user = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if user == password and user != "":
            st.session_state.login = True
            st.success("You are logged in ")
        else:
            st.error("Invalid username or password")

else:
    st.title("Welcome to Weather App ")
    Weather()

