import uvicorn
from fastapi import FastAPI
import chatbot
from model import PromptRequest

 # Pre-index the PDF on startup
app = FastAPI()

chatbot = chatbot.Chatbot()

@app.post("/search-pdf")
async def generate_text(request: PromptRequest):
    response = chatbot.generate_text(request)
    return {"response": response}

@app.post("/chat")
async def generate_text(request: PromptRequest):
    response = chatbot.response_chat(request)
    return {"response": response}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=False)