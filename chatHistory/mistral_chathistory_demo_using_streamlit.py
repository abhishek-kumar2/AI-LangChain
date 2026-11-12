# import os
# from langchain_ollama import ChatOpenAI
from langchain_ollama import ChatOllama
import streamlit as st
from langchain_core.globals import set_debug

set_debug(False)

# OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
llm = ChatOllama(model = "mistral:7b")


st.markdown("""
<style>
.question-box {
    background-color: #F5F5F0 !important;
    color: #222222 !important;
    padding: 15px 20px;
    border-radius: 10px;
    margin-bottom: 12px;
    border: 1px solid #E8E8E0;
}

.answer-box {
    background-color: #FFFFFF !important;
    color: #222222 !important;
    padding: 18px 20px;
    border-radius: 10px;
    margin-bottom: 15px;
    border: 1px solid #EEEEEE;
}

.question-box *,
.answer-box * {
    color: #222222 !important;
}

.section-label {
    font-size: 13px;
    font-weight: 600;
    color: #666666 !important;
    margin-bottom: 8px;
}
</style>
""", unsafe_allow_html=True)



st.header("Persional AI chat bot... :blue[cool] :sunglasses:", divider="gray")

# question = st.text_input("Enter the question: ")
question = st.chat_input("Enter the question: ")

if question:
    response = llm.invoke(question)

    # Extract response metadata
    metadata = response.response_metadata

    model = metadata.get("model", "Unknown")
    total_duration = metadata.get("total_duration", 0)
    total_seconds = total_duration / 1e9
    model_provider = metadata.get("model_provider")
    # st.badge('Model Provider: ' + model_provider + ' | Model: ' + model + ' | Respond seconds: ' + str(f"{total_seconds:.2f}"), color="yellow")
    st.markdown(":red-badge[Model Provider: " + model_provider + "] :orange-badge[Model: " + model + "] :blue-badge[Respond seconds: " + str(f"{total_seconds:.2f}") + "]")
    
    usage_metadata = response.usage_metadata

    input_tokens = usage_metadata.get("input_tokens", 0)
    output_tokens = usage_metadata.get("output_tokens", 0)
    total_tokens = usage_metadata.get("total_tokens", 0)
    # st.badge('Input tokens: ' + str(input_tokens) + ' | Output tokens: ' + str(output_tokens) + ' | Total tokens: ' + str(total_tokens), color="green")
    st.markdown(":gray-badge[Input tokens: " + str(input_tokens) + "] :gray-badge[Output tokens: " + str(output_tokens) + "] :green-badge[Total tokens: " + str(total_tokens) + "]")

    
    # Question section
    st.markdown(f"""
    <div class="question-box">
        <div class="section-label">QUESTION</div>
        {question}
    </div>
    """, unsafe_allow_html=True)

    # Answer section
    st.markdown(f"""
    <div class="answer-box">
        <div class="section-label">ANSWER</div>
        {response.content}
    </div>
    """, unsafe_allow_html=True)

    