import streamlit as st
import requests
from dotenv import load_dotenv
import os

def Weather():
    city = st.selectbox("City", ["Pune", "Sangli", "Ashta"])

    load_dotenv()
    #api_key = os.getenv("api_key")
    api_key=0
    if not api_key:
        st.error("API key not found")
        return

    url = f"https://api.openweathermap.org/data/2.5/weather?appid={api_key}&units=metric&q={city}"
    response = requests.get(url)
    weather = response.json()

    if response.status_code == 200:
        st.write(f"Temperature : {weather['main']['temp']} °C")
        st.write(f"Humidity : {weather['main']['humidity']} %")
        st.write(f"Wind speed : {weather['wind']['speed']} m/s")
    else:
        st.error(weather.get("message", "Error fetching weather"))
#main

if "login" not in st.session_state:
    st.session_state.login = False

st.title("Login")

if not st.session_state.login:
    user = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if user == password and user != "":
            st.session_state.login = True
            st.success("You are logged in ")
        else:
            st.error("Invalid username or password")

else:
    st.title("Welcome to Weather App ")
    Weather()
