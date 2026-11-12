# import os
# from langchain_openai import OpenAIEmbeddings
from langchain_ollama import OllamaEmbeddings

# OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
# llm = OpenAIEmbeddings(api_key=OPENAI_API_KEY)
llm = OllamaEmbeddings(model = "nomic-embed-text")

texts = input("Enter the text to embed: ")
response = llm.embed_query(texts)
print(response)

