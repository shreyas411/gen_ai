import os 

API_URL = os.getenv("OLLAMA_API_URL", "http://localhost:11434/api/generate")
MODEL = os.getenv("OLLAMA_MODEL", "qwen3")
