---
title: Multilingual GUVI Chatbot
emoji: 🤖
colorFrom: green
colorTo: blue
sdk: streamlit
sdk_version: "1.33.0"
app_file: app.py
pinned: false
---

# Multilingual GUVI Chatbot 🤖🌍

A smart chatbot for answering GUVI-related FAQs in **multiple languages**. This app detects the input language, translates it to English, finds the best matching FAQ answer using semantic search, and optionally translates the answer back to the original language.

### 🧠 Features

- 🔎 **Semantic Search** using `MiniLM`
- 🌍 **Multilingual Translation** using NLLB (No Language Left Behind)
- 🧑‍💻 Trained on real GUVI FAQs
- 💬 Built with **Streamlit**
- ☁️ Runs on CPU in Hugging Face Spaces

### 🚀 How It Works

1. User enters a question (in any supported language).
2. Input is translated to English.
3. App performs semantic similarity with preloaded FAQ embeddings.
4. Returns the best match answer (optionally translated back to user language).

---

### App Link Here :https://huggingface.co/spaces/thiru43/guvi_chatbot

