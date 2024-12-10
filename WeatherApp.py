
import streamlit as st
import requests

# App configuration
st.set_page_config(
    page_title="Weather App",
    page_icon="☁️",
    layout="wide",
)

# Custom CSS for styling
st.markdown(
    '''
    <style>
    .chat-container {
        max-width: 700px;
        margin: 20px auto;
        padding: 15px;
        border: 1px solid #ddd;
        border-radius: 10px;
        background-color: #f9f9f9;
    }
    .user-message {
        text-align: right;
        color: #fff;
        background-color: #007bff;
        padding: 10px;
        border-radius: 15px;
        margin: 5px 0;
    }
    .bot-message {
        text-align: left;
        color: #000;
        background-color: #e9ecef;
        padding: 10px;
        border-radius: 15px;
        margin: 5px 0;
    }
    </style>
    ''',
    unsafe_allow_html=True,
)

# Function to fetch weather data
def get_weather(city):
    api_key = "your_openweathermap_api_key"  # Replace with your OpenWeatherMap API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            weather = data["weather"][0]["description"].capitalize()
            temp = data["main"]["temp"]
            return f"The weather in {city} is currently {weather} with a temperature of {temp}°C."
        else:
            return f"Sorry, I couldn't find weather information for {city}. Please check the city name."
    except Exception as e:
        return "An error occurred while fetching the weather data."

# Title
st.title("☁️ Browser-Based Weather App")

# Session state for storing messages
if "messages" not in st.session_state:
    st.session_state.messages = []

# Input field
with st.container():
    user_input = st.text_input("Enter a city name:", "", placeholder="E.g., London, New York")
    if user_input:
        st.session_state.messages.append(("user", user_input))
        response = get_weather(user_input)  # Fetch weather data
        st.session_state.messages.append(("bot", response))

# Chat history
st.markdown('<div class="chat-container">', unsafe_allow_html=True)
for sender, msg in st.session_state.messages:
    if sender == "user":
        st.markdown(f'<div class="user-message">{msg}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="bot-message">{msg}</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
