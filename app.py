import streamlit as st
from chatbot import Chatbot

st.set_page_config(page_title="GUVI Multilingual Chatbot", page_icon="🤖", layout="centered")

@st.cache_resource(show_spinner=False)
def get_bot():
    return Chatbot()

def main():
    st.title("🤖 GUVI Multilingual Chatbot")
    st.caption("Type in English or your native language. I’ll translate, answer, and translate back.")

    user_input = st.text_input("Your question:")
    if st.button("Ask") and user_input.strip():
        bot = get_bot()
        with st.spinner("Thinking..."):
            try:
                reply = bot.get_response(user_input.strip())
            except Exception as e:
                reply = f"Oops, something went wrong: {e}"
        st.markdown(f"**Answer:** {reply}")

if __name__ == "__main__":
    main()
