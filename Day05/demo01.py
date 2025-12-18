from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
load_dotenv()
api_key = os.getenv("api_key")
print(api_key)
llm = ChatGroq(model="openai/gpt-oss-120b", api_key=api_key)
user_input = input("you :")
result = llm.stream(user_input)
for c in result:
    print(c.content,end ="")

result = llm.invoke(user_input)
print("\nAI :",result.content)