# 🩺 LLM-Based Clinical Notes Summarizer

A fully offline AI app that summarizes clinical notes using local LLMs like GPT4All. No API keys or internet required.

## 🚀 How to Run

1. **Install dependencies**
pip install -r requirements.txt


2. **Download Models**
- Run: `python download_model.py` (for embeddings)
- Download GPT4All model manually:  
  https://gpt4all.io/models/  
  Place it in `models/` as `ggml-gpt4all-j-v1.3-groovy.bin`

3. **Add Clinical Notes**
- Put your text in `documents/example_notes.txt`
- OR paste it directly into the app

4. **Run the App**
streamlit run app.py

## 🧠 Models Used

- **LLM:** GPT4All (offline)
- **Embeddings (optional):** MiniLM from Sentence Transformers

## 💡 Example Use Case

- Summarizing patient clinical notes
- Creating SOAP format summaries
- Reducing documentation load for healthcare professionals

