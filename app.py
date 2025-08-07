import streamlit as st
from chatbot import Chatbot

st.set_page_config(page_title="GUVI Chatbot", page_icon="🤖")
st.title("🤖 GUVI Multilingual Chatbot")
st.markdown("Ask me anything related to GUVI in **Tamil, Hindi, Telugu, or English**!")

chatbot = Chatbot()

user_input = st.text_input("Enter your question:")

if user_input:
    with st.spinner("Thinking..."):
        response = chatbot.get_response(user_input)
    st.success(response)
