from langchain.chat_models import init_chat_model
from langchain.agents import create_agent
from langchain.agents.middleware import wrap_model_call
from langchain.tools import tool
import requests
from dotenv import load_dotenv
import json
import os

@tool
def 

llm = init_chat_model(
    model="google/gemma-3-4b",
    model_provider="openai",
    base_url ="",
    api_key="dummy key",
    timeout = 300 
)
conversation = []
agent = create_agent(
    model = llm,
    tools=[],
    system_prompt="You are the Helpful assistent"
)

while True:
    user_input = input("You : ")
    if user_input == "exit":
        break
    conversation.append({"role":"user","content":user_input})
    result = agent.invoke({"messages":conversation})
    ai_msg = result["messages"][-1]
    print("Ai : ",ai_msg.content)
    result = conversation["messages"]