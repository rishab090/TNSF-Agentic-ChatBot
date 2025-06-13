from llama_cpp import Llama
from chunk import search_similar_docs
from model import PromptRequest
import settings

llm = Llama(settings.mistral_path)


def build_prompt(chunks, query: PromptRequest):
    context = "\n".join(chunks)
    return f"Context:\n{context}\n\nQuestion:\n{query.prompt}\n\nAnswer:"

def chatbot_pipeline(user_prompt: PromptRequest):
    docs = search_similar_docs(user_prompt)  
    llm_prompt = build_prompt(docs, user_prompt)
    return llm(llm_prompt, max_tokens=user_prompt.max_new_tokens, temperature=0.7)


def chatbot_chat(user_prompt: PromptRequest):
    llm_prompt = f"Question:\n{user_prompt.prompt}\n\nAnswer:"
    return llm(llm_prompt, max_tokens=user_prompt.max_new_tokens, temperature=0.7)

