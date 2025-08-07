import streamlit as st
from chatbot import Chatbot

# Initialize chatbot
chatbot = Chatbot()

# Page config
st.set_page_config(page_title="Multilingual GUVI Chatbot", layout="centered")

st.title("💬 Multilingual GUVI Chatbot")
st.markdown("Ask me anything about GUVI — in any supported Indian language!")

# Language selection
lang_options = list(chatbot.translator.language_map.keys())
input_lang = st.selectbox("Select your input language", lang_options, index=0)
output_lang = st.selectbox("Select output language", lang_options, index=0)

# User input
user_input = st.text_input("Enter your question:", placeholder="e.g., GUVI क्या करता है?")

# Ask button
if st.button("Ask"):
    if user_input.strip() == "":
        st.warning("Please enter a question.")
    else:
        with st.spinner("Thinking..."):
            response = chatbot.ask(user_input, input_lang=input_lang, output_lang=output_lang)
        st.success("Answer:")
        st.write(response)
