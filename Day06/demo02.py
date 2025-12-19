from langchain.chat_models import init_chat_model
from langchain.agents import create_agent
from langchain.tools import tool

@tool
def calculator(expressaion):
    """
    This calculator function solves any arithmetic expression containing all constant values.
    It supports basic arithmetic operators +, -, *, /, and parenthesis. 
    
    :param expression: str input arithmetic expression
    :returns expression result as str
    """
    try:
        result = eval(expressaion)
        return str(result)
    except:
        return "Error"
llm = init_chat_model(
    model = "google/gemma-3-4b",
    model_provider="openai",
    base_url = "http://192.168.43.239:1234/v1",
    api_key = "dummy"
)

agent = create_agent(
    model = llm,
    tools = [calculator],
    system_prompt = "You are a helpful assistent answer in short"
)
while True:
    user_input = input("You : ")
    if user_input == 'exit':
        break
    result = agent.invoke({"messages":[
        {"role":"user","content":user_input}
    ]
    })
    ai_msg = result["messages"][-1]
    print('AI : ',ai_msg.content)
    conversation = result["messages"]