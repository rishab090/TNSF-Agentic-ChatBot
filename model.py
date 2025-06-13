
# Input schema
from pydantic import BaseModel


class PromptRequest(BaseModel):
    prompt: str
    max_new_tokens: int = 50