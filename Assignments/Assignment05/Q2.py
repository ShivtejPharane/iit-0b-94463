import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")
url = "https://api.groq.com/openai/v1/chat/completions"
headers  = {
    "Authorization" : f"Bearer {api_key}",
    "Content-Type" : "application/json"
}
user_prompt = input("Ask Any Thing :")
req_data = {
    "model" : "llama-3.3-70b-versatile",
    "messages" : [
        {"role" : "user","content" : user_prompt}
    ],
}
response = requests.post(url,data=req_data)
print(response.json())
