from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatMessagePromptTemplate

template = (
    "requires a promt engineered text"
)

model = OllamaLLM(model = "llama3")

def parse_with_ollama(dom_chunks, parse_description):
    pass