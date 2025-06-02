import os
import streamlit as st
from summarize import load_llm, summarize_text

st.set_page_config(page_title="Clinical Notes Summarizer", page_icon="🩺", layout="centered")
st.title("🩺 LLM-Based Clinical Notes Summarizer (Offline)")
st.markdown("Summarize clinical notes using local AI — no API or internet required.")

FILE_PATH = "./documents/example_notes.txt"
MODEL_PATH = "./models/ggml-gpt4all-j-v1.3-groovy.bin"

# Input
input_text = st.text_area("Paste your clinical notes below:", height=250)

if st.button("Summarize"):
    if input_text.strip() == "":
        st.warning("Please paste some text to summarize.")
    elif not os.path.exists(MODEL_PATH):
        st.error("❌ LLM model not found. Download the GPT4All model and place it in `models/`.")
    else:
        with st.spinner("Generating summary..."):
            llm = load_llm(MODEL_PATH)
            summary = summarize_text(input_text, llm)
            st.success("Summary generated:")
            st.markdown(f"📝 **Summary:**\n\n{summary}")
