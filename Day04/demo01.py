import os
import requests
import json
import time
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("api_key")
print(api_key)
url = "https://api.groq.com/openai/v1/chat/completions"
headers = {
    "Authorization" : f"Bearer {api_key}",
    "Content-Type" : "application/json"
    }
while True :
    user_prompt = input("SEarch : ")
    if user_prompt=="exit":
        break
    req_data = {
        "model" : "llama-3.3-70b-versatile",
        "messages" : [
            {"role" : "user","content" : user_prompt}
        ]
    }
    time1 = time.perf_counter()
    response = requests.post(url,data = req_data,headers=headers)
    time2 = time.perf_counter()
    print(f"time is {(time2 - time1)}")
    print(response)
