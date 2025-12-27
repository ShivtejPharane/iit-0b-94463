from langchain.chat_models import init_chat_model
from langchain.agents import create_agent
from langchain.agents.middleware import wrap_model_call
from langchain.tools import tool
import requests
from dotenv import load_dotenv
import json
import os
load_dotenv()
@wrap_model_call
def model_logging(request, handler):
    print("Before model call: ", '-' * 20)
    # print(request)
    response = handler(request)
    print("After model call: ", '-' * 20)
    # print(response)
    response.result[0].content = response.result[0].content.upper()
    return response

@wrap_model_call
def limit_model_context(request, handler):
    print("* Before model call: ", '-' * 20)
    # print(request)
    request.messages = request.messages[-5:]
    response = handler(request)
    print("* After model call: ", '-' * 20)
    # print(response)
    response.result[0].content = response.result[0].content.upper()
    return response
@tool
def get_weather(city):
    """
    This get_weather() function gets the current weather of given city.
    If weather cannot be found, it returns 'Error'.
    This function doesn't return historic or general weather of the city.

    :param city: str input - city name
    :returns current weather in json format or 'Error'    
    """
    print("open weather is called")
    try:
        api_key = os.getenv("api_key")
        print(api_key)
        #city = input("Enter the city : ")
        url = f"https://api.openweathermap.org/data/2.5/weather?appid={api_key}&units=metric&q={city}"
        response = requests.get(url)
        weather = response.json()
        return json.dumps(weather)
    except:
        return "Error"

@tool
def calculator(expressaion):
    """
    This calculator function solves any arithmetic expression containing all constant values.
    It supports basic arithmetic operators +, -, *, /, and parenthesis. 
    
    :param expression: str input arithmetic expression
    :returns expression result as str
    """
    print("called the calculator tool")
    try:
        result = eval(expressaion)
        return str(result)
    except:
        return "Error"


llm = init_chat_model(
    model = "google/gemma-3-4b",
    model_provider="openai",
    base_url = "http://127.0.0.1:1234/v1",
    api_key = "dummy",
    timeout=600,
    max_tokens=128,
    streaming = True
)
conversation = []
agent = create_agent(
    model = llm,
    tools = [calculator,get_weather],
     middleware=[model_logging, limit_model_context],
    system_prompt = "You are a helpful assistent answer in short"
)

while True:
    user_input = input("You : ")
    if user_input == "exit":
        break
    conversation.append({"role":"user","content":user_input})
    result = agent.invoke({"messages":conversation})
    ai_msg = result["messages"][-1]
    print("Ai : ",ai_msg.content)
    conversation = result["messages"]       