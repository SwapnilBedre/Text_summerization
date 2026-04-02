import requests
import os
from dotenv import load_dotenv # type: ignore

load_dotenv()

GROK_API_KEY = os.getenv("GROK_API_KEY")


def summarize(text: str):
    url = "https://api.x.ai/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {GROK_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
    "model": "grok-1",   # ✅ safest working model
    "messages": [
        {
            "role": "user",
            "content": f"Summarize this text clearly:\n\n{text}"
        }
    ],
    "temperature": 0.3
}

    try:
        response = requests.post(url, headers=headers, json=payload)

        # 🔥 DEBUG (IMPORTANT)
        print("Status Code:", response.status_code)
        print("Response:", response.text)

        response.raise_for_status()

        return response.json()["choices"][0]["message"]["content"]

    except Exception as e:
        print("Error calling Grok API:", e)
        return "Summarization failed"