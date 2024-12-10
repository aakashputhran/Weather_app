import streamlit as st
from datetime import datetime

# App configuration
st.set_page_config(
    page_title="Browser-Based Chat App",
    page_icon="💬",
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

# Title
st.title("💬 Browser-Based Chat App")

# Session state for storing messages
if "messages" not in st.session_state:
    st.session_state.messages = []

# Input field
with st.container():
    user_input = st.text_input("Type your message:", "", placeholder="Say something...")
    if user_input:
        st.session_state.messages.append(("user", user_input))

# Chat history
st.markdown('<div class="chat-container">', unsafe_allow_html=True)
for sender, msg in st.session_state.messages:
    if sender == "user":
        st.markdown(f'<div class="user-message">{msg}</div>', unsafe_allow_html=True)
    else:
        response = f"I see you said: {msg}"  # Replace with your chatbot logic
        st.markdown(f'<div class="bot-message">{response}</div>', unsafe_allow_html=True)
        st.session_state.messages.append(("bot", response))
st.markdown('</div>', unsafe_allow_html=True)
