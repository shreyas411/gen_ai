import requests

response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "qwen3",
        "prompt": "Say hello to a new GenAI developer.",
        "stream": False,
    },
)

print(response.json()["response"])