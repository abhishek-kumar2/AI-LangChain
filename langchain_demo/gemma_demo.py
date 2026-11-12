import os
# from langchain_ollama import ChatOpenAI
from langchain_ollama import ChatOllama

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
# llm = ChatOllama(model = "gpt-4o", api_key = OPENAI_API_KEY)
llm = ChatOllama(model = "gemma3:1b")

question = input("Enter the question: => ")
response = llm.invoke(question)
print(response.content)