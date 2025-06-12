from fastapi import FastAPI, Request
from pydantic import BaseModel
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import uvicorn

# Load the model
model_path = "E:/projects/TechNova/TNSF/PythonProject/ChatBot/model"  # CHANGE THIS TO YOUR MODEL FOLDER
model = AutoModelForCausalLM.from_pretrained(model_path, torch_dtype=torch.float16, local_files_only=True)
tokenizer = AutoTokenizer.from_pretrained(model_path, local_files_only=True)

# Init FastAPI app
app = FastAPI()

# Input schema
class PromptRequest(BaseModel):
    prompt: str
    max_new_tokens: int = 50

@app.post("/generate")
async def generate_text(request: PromptRequest):
    inputs = tokenizer(request.prompt, return_tensors="pt")
    outputs = model.generate(**inputs, max_new_tokens=request.max_new_tokens)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return {"response": response}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=False)