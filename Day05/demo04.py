
from langchain.chat_models import init_chat_model
import os
from dotenv import load_dotenv
load_dotenv()
llm = init_chat_model(
    model = "llama-3.3-70b-versatile",
    model_provider = "openai",
    base_url = "https://api.groq.com/openai/v1",
    api_key = os.getenv("api_key")
)
conversation = [
    {"role" : "system","content":"You are healpful assistent."}
]
print("This model has the Context length is 5")
while True:
    user_input = input("You: ")
    if user_input == "exit":
        break
    #print("conversation : ",conversation)
    user_msg = {'role':'user','content':user_input}
    #print("user message : ",user_msg)
    conversation.append(user_msg)
    llm_output = llm.invoke(conversation[-5:])
    print("Ai : ",llm_output.content)
    llm_msg = {'role':'assistant','content':llm_output.content}
    #print("llm message ",llm_msg)
    conversation.append(llm_msg)