from dataclasses import dataclass

@dataclass
class ChatResponse:
    model: str
    response: str
    success: bool