import requests

response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "qwen3",
        "stream": False,
        "prompt": "Say hello to a new GenAI developer."
    }
)

data = response.json()
print(data["response"])