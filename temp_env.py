import requests
import os
from dotenv import load_dotenv # type: ignore

load_dotenv()

url = "https://api.x.ai/v1/models"

headers = {
    "Authorization": f"Bearer {os.getenv('GROK_API_KEY')}"
}

response = requests.get(url, headers=headers)

print(response.status_code)
print(response.text)