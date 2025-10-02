import requests
import streamlit as st

# Hugging Face API URL
API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"

# Use API key from Streamlit secrets
headers = {"Authorization": f"Bearer {st.secrets['HF_API_KEY']}"}

def summarize(text):
    """Send text to Hugging Face model and return summary."""
    payload = {"inputs": text}
    response = requests.post(API_URL, headers=headers, json=payload)
    data = response.json()

    # Handle errors
    if isinstance(data, dict) and "error" in data:
        return f"Something went wrong: {data['error']}"
    elif isinstance(data, list) and "summary_text" in data[0]:
        return data[0]["summary_text"]
    else:
        return f"Unexpected response: {data}"

# Streamlit UI
st.title("📝 AI Text Summarizer")
st.write("Paste your article below and get a 2-3 sentence summary:")

article = st.text_area("Enter Article Text", height=200)

if st.button("Summarize"):
    if article.strip() == "":
        st.warning("Please enter some text to summarize.")
    else:
        with st.spinner("Summarizing..."):
            summary = summarize(article)
        st.subheader("Summary:")
        st.write(summary)
