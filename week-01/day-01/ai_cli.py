import requests;
from rich.console import Console

API_URL = "http://localhost:11434/api/generate"
MODEL = "qwen3"

def chat_with_ollama(prompt):
    response = requests.post(
        API_URL,
        json={
            "model": MODEL,
            "stream": False,
            "prompt": prompt
        }
    )
    data = response.json()

    if response.status_code != 200:
        raise Exception(f"Error: {data.get('error', 'Unknown error')}")

    return data["response"]

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        break
    response = chat_with_ollama(user_input)
    console = Console()
    console.print(f"[bold green]Ollama:[/bold green] {response}")