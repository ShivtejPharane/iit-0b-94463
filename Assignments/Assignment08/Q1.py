
from langchain.chat_models import init_chat_model
from langchain.agents import create_agent
from langchain.tools import tool
from dotenv import load_dotenv
from langchain.agents.middleware import wrap_model_call
import os
import json
import requests
import pandas as pd
load_dotenv() # by default read env from .env file

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
def file_reader(path):
    """
    This is File Reader to read any csv file and doing the operations on it .

    param expression : str input which is path of file
    returns expression result as str
    """
    try:
        df = pd.read_csv(path)
        return df
    except:
        return "Error : connot solve the problem"

@tool
def calculator(expression):
    """
    This calculator function solves any arithmetic expression containing all constant values.
    It supports basic arithmetic operators +, -, *, /, and parenthesis. 
    
    :param expression: str input arithmetic expression
    :returns expression result as str
    """
    try:
        result = eval(expression)
        return str(result)
    except:
        return "Error: Cannot solve expression"

@tool
def get_weather(city):
    """
    This get_weather() function gets the current weather of given city.
    If weather cannot be found, it returns 'Error'.
    This function doesn't return historic or general weather of the city.

    :param city: str input - city name
    :returns current weather in json format or 'Error'    
    """
    try:
        api_key = os.getenv("OPENWEATHER_API_KEY")
        url = f"https://api.openweathermap.org/data/2.5/weather?appid={api_key}&units=metric&q={city}"
        response = requests.get(url)
        weather = response.json()
        return json.dumps(weather)
    except:
        return "Error"

# create model
llm = init_chat_model(
    model = "google/gemma-3-4b",
    model_provider = "openai",
    base_url = "http://127.0.0.1:1234/v1",
    api_key = "non-needed"
)

# create agent
agent = create_agent(
            model=llm, 
            tools=[
                calculator,
                get_weather,file_reader
            ],
            middleware=[model_logging,limit_model_context],
            system_prompt="You are a helpful assistant. Answer in short."
        )

while True:
    # take user input
    user_input = input("You: ")
    if user_input == "exit":
        break
    # invoke the agent with user input
    result = agent.invoke({
        "messages": [
            {"role": "user", "content": user_input}
        ]
    })
    llm_output = result["messages"][-1]
    print("AI: ", llm_output.content)
    print("\n\n", result["messages"])