import requests
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")
city = input("Enter City : ")
url = f"https://api.openweathermap.org/data/2.5/weather?appid={api_key}&units=metric&q={city}"
response = requests.get(url)
weather = requests.get(response)
print(weather)