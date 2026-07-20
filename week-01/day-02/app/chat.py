import requests
from app.constants import API_URL, MODEL
from app.logging import logger
from app.models import ChatResponse

def chat_with_ollama(prompt: str) -> object:
    """
    send prompt to Ollama API and return the response.

    user: 
        prompt: user input string to send to the Ollama API.

    returns:
        str - The response from the Ollama API.
    """
    try: 
        logger.info("Sending request to ollama...")
        response = requests.post(
            API_URL,
            json={
                "model": MODEL,
                "stream": False,
                "prompt": prompt
            }
        )

        response.raise_for_status()

        data = response.json()

        logger.info("Response received.")

        return ChatResponse(
            model=MODEL,
            response=data['response'],
            success=True
        )
    
    except requests.exceptions.RequestException as error:
        logger.error(error)

        return ChatResponse(
            model=MODEL,
            response="Unable to connect ollama",
            success=False
        )

