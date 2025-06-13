from transformers import AutoModelForCausalLM, AutoTokenizer
from fastapi import FastAPI, Request
import torch
import settings

# CHANGE THIS TO YOUR MODEL FOLDER
mistral_model = AutoModelForCausalLM.from_pretrained(settings.mistral_path, torch_dtype=torch.float16, local_files_only=True)
mistral_tokenizer = AutoTokenizer.from_pretrained(settings.mistral_path, local_files_only=True)
