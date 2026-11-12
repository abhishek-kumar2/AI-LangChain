from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
import streamlit as st
from langchain_core.globals import set_debug

set_debug(False)

llm = ChatOllama(model = "gemma3:1b")

prompt = PromptTemplate(
    template = '''
    Welcome to the {city} travel guide!
    If you're visiting in {month}, here's what you can do:
    1. Must-visit attractions.
    2. Local cuisine to must try.
    3. Useful phrases in {language}.
    4. Tips for traveling on a {budget} budget.

    Enjoy your trip!
    ''',
    input_variables = ["city", "month", "language", "budget"]
)

city = st.text_input("Enter the city")
month = st.text_input("Enter the month")
language = st.text_input("Enter the language")
budget = st.selectbox("Travel Budget", ["Low", "Medium", "High"])

if st.button("Generate travel guide"):
    response = llm.invoke(prompt.format(city=city, month=month, language=language, budget=budget))
    st.write(response.content)      