from llama_cpp import Llama
from pdf_parse import search_similar_docs
from model import PromptRequest
import settings

llm = Llama(settings.mistral_path)


def build_prompt(chunks, query: PromptRequest):
    context = "\n".join(chunks)
    return f"Context:\n{context}\n\nQuestion:\n{query.prompt}\n\nAnswer:"

class Chatbot:
    def __init__(self):
        self.llm = Llama(settings.mistral_path)

    def generate_text(self, user_prompt: PromptRequest):
        docs = search_similar_docs(user_prompt)
        llm_prompt = build_prompt(docs, user_prompt)
        return self.llm(llm_prompt, max_tokens=user_prompt.max_new_tokens, temperature=0.7)

    def response_chat(self, user_prompt: PromptRequest):
        llm_prompt = f"Question:\n{user_prompt.prompt}\n\nAnswer:"
        return self.llm(llm_prompt, max_tokens=user_prompt.max_new_tokens, temperature=0.7)