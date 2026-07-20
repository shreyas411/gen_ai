from app.chat import chat_with_ollama as chat
from rich.console import Console
console = Console()


def main() -> None:
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        prompt = chat(user_input) 
        
        response = prompt.response

        console.print(f"[bold blue]User:[/bold blue] {user_input}")
        console.print(f"[bold green]Assistant:[/bold green] {response}")

if __name__ == "__main__":
    main()