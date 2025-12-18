import os
import requests
import json
from dotenv import load_dotenv
import streamlit as st 
load_dotenv()

def Online_model():
    api_key = os.getenv("api_key")
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    req_data = {
            "model" : "llama-3.3-70b-versatile",
            "messages" : [
                {"role" : "user","content" : user_prompt}
               ]
        }
    response = requests.post(url,json = req_data,headers=headers)
    resp = response.json()
    #st.write(resp)
    st.write(resp["choices"][0]["message"]["content"])        

def Offline_model():
            api_key = "dummy-key"
            url = "http://192.168.1.109:1234/v1/chat/completions"
            headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
            }
            req_data = {
                "model" : "google/gemma-3n-e4b",
                "messages" : [
                    {"role" : "user","content" : user_prompt}
                ]
             }
            response = requests.post(url,data = json.dumps(req_data),headers=headers)
            resp = response.json()
            st.write(resp["choices"][0]["message"]["content"])
st.title("Chat GPT")

with st.sidebar:
    st.header("Settings")
    st.write("Choose the model")
    choices = st.radio("Models",["Online Model","Offline Model"])
    user_prompt = st.chat_input("Ask Anything")
if choices == "Online Model":
    Online_model()
else :
    Offline_model()
