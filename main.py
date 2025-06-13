import uvicorn
from fastapi import FastAPI
import chunk
import functions
from model import PromptRequest

 # Pre-index the PDF on startup
app = FastAPI()


@app.post("/search-pdf")
async def generate_text(request: PromptRequest):
    response = functions.chatbot_pipeline(request)
    return {"response": response}

@app.post("/chat")
async def generate_text(request: PromptRequest):
    response = functions.chatbot_chat(request)
    return {"response": response}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=False)