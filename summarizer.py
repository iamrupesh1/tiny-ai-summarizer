import os
import requests
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()

API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
headers = {"Authorization": f"Bearer {os.getenv('HF_API_KEY')}"}

def summarize(text):
    """Send text to Hugging Face model and return summary."""
    payload = {"inputs": text}
    response = requests.post(API_URL, headers=headers, json=payload)
    data = response.json()

    # Debug: if something goes wrong
    if isinstance(data, dict) and "error" in data:
        return f"⚠️ Something went wrong: {data['error']}"
    elif isinstance(data, list) and "summary_text" in data[0]:
        return data[0]["summary_text"]
    else:
        return f"⚠️ Unexpected response: {data}"

if __name__ == "__main__":
    print("📝 AI Text Summarizer")
    print("Paste your article below (end with an empty line):\n")

    # Read multi-line input
    lines = []
    while True:
        line = input()
        if line.strip() == "":
            break
        lines.append(line)

    article = "\n".join(lines)
    print("\n--- Original Article ---")
    print(article)

    print("\n--- Summary ---")
    summary = summarize(article)
    print(summary)
