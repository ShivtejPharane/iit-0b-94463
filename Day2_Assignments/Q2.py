import requests
import os
from dotenv import load_dotenv
import streamlit as st

def weather_app():
    st.header(" Weather Information")

    city = st.selectbox(
        "Choose the city",
        ["Pune", "Mumbai", "Nashik", "Ashta"]
    )

    load_dotenv()
    api_key = os.getenv("api_key")

    if not api_key:
        st.error("API key not found. Check your .env file.")
        return

    url = f"https://api.openweathermap.org/data/2.5/weather?appid={api_key}&units=metric&q={city}"
    response = requests.get(url)
    weather = response.json()

    if response.status_code == 200:
        st.success(f"Weather in {city}")
        st.write(f" Temperature: {weather['main']['temp']} °C")
        st.write(f" Humidity: {weather['main']['humidity']} %")
        st.write(f" Wind Speed: {weather['wind']['speed']} m/s")
    else:
        st.error(weather.get("message", "Something went wrong"))


if "logged_in" not in st.session_state:
    st.session_state.logged_in = False


st.title("Login Page")

username = st.text_input("Username", key="username")
password = st.text_input("Password", type="password", key="password")

if st.button("Login", key="login_btn"):
    if username == password:
        st.success("Login successful ")
    else:
        st.error("Invalid credentials ")
