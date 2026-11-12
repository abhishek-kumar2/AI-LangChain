from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
import streamlit as st
from langchain_core.globals import set_debug
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser

set_debug(True)

llm_gemma = ChatOllama(model = "gemma3:1b")
llm_mistral = ChatOllama(model = "mistral:7b", format="json")

title_prompt = PromptTemplate(
    input_variables=["topic"],
    template="""
        You are an experienced speech writter.
        You need to craft an impactful title for a speech on the following topic: {topic}
        Answer exactly with one title.
    """
)

speech_prompt = PromptTemplate(
    input_variables=["title", "emotion"],
    template="""
        You need to write a powerful {emotion} speech of 350 words for the following title: {title}
        Return ONLY a valid JSON object with exactly 2 keys: "title" and "speech", filled with the respective values.
        Do not include any text outside the JSON object.
    """
)

title_chain = title_prompt | llm_gemma | StrOutputParser() | (lambda title: (st.write(title), title)[1])
speech_chain = speech_prompt | llm_mistral | JsonOutputParser()

sequential_chain = title_chain | (lambda title: {"title": title, "emotion": emotion}) | speech_chain

st.title("Speech Generator")

topic = st.text_input("Enter a topic for your speech")
emotion = st.text_input("Enter an emotion for your speech")

if topic and emotion:
    speech = sequential_chain.invoke({"topic": topic})
    # st.write(speech.content)
    st.write(speech)
    st.title(speech["title"])
    st.write(speech["speech"])