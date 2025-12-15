import requests
import os
from dotenv import load_dotenv
import pandasql as ps
import streamlit as st

def weather_app():
    city = st.selectbox("Choose the city", ["Pune", "Mumbai", "Nashik", "Ashta"])

    load_dotenv()
    api_key = os.getenv("api_key")

    url = f"https://api.openweathermap.org/data/2.5/weather?appid={api_key}&units=metric&q={city}"
    response = requests.get(url)
    weather = response.json()

    # Debug (optional)
    # st.write(weather)

    if response.status_code == 200:
        st.write(f"Temperature is : {weather['main']['temp']} °C")
        st.write(f"Humidity is : {weather['main']['humidity']} %")
        st.write(f"Wind speed is : {weather['wind']['speed']} m/s")
    else:
        st.error(weather.get("message", "Something went wrong"))



#detalis
if "page" not in st.session_state:
    st.session_state.page = False
st.title("Wheather Detection App!")
st.subheader("Login to enter the app ....")
username = st.text_input("Username")
password =st.text_input("Password",type='password')
if st.button("login"):
    if username == password:
        st.session_state.page = True
        st.rerun
if  st.button("login"):
    weather_app()



