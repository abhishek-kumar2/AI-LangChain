# import os
# from langchain_ollama import ChatOpenAI
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage

# OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
# llm = ChatOPenAI(model = "gpt-4o-mini", api_key=OPENAI_API_KEY)
llm = ChatOllama(model = "gemma3:4b")

prompt_template = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{question}")
])

chat_history = []

chain = prompt_template | llm

print("Welcome to the Personal AI Chat Bot!")

while True:
    question = input("Enter your question (or type 'exit' to quit): ")
    if question.lower() == 'exit':
        print("Exiting the chat. Goodbye!")
        break

    if question:
        # Create a prompt with the current chat history and the new question
        prompt = prompt_template.format_prompt(chat_history=chat_history, question=question)

        # Invoke the model with the prompt
        response = llm.invoke(prompt.to_messages())

        # Extract response metadata
        metadata = response.response_metadata
        model = metadata.get("model", "Unknown")

        # Get the AI's answer
        answer = response.content

        # Print the answer and model information
        print(f"AI ({model}): {answer}")
        print("-" * 50)  # Separator for readability
        print("-" * 50)  # Separator for readability

        # Update chat history with the new interaction
        chat_history.append(HumanMessage(content=question))
        chat_history.append(AIMessage(content=answer))