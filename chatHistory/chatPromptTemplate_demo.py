from langchain_ollama import ChatOllama
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

llm = ChatOllama(model = "mistral:7b")
prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a Agile Coach. Answer any question related to Agile process"),
        ("human", "{question}")
    ]
)

st.title("Agile Coach")
question = st.text_input("Ask a question about Agile")

chain = prompt_template | llm

if question:
    response = chain.invoke({"question": question})
    st.write(response.content)