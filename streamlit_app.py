import streamlit as st
import requests
# chat_agent.py
from langchain import LangChain, Chain, OpenAI

class SimpleChatAgent(Chain):
    def __init__(self):
        self.llm = OpenAI(api_key="sk-proj-1LH6p4ZoVbyGSjxrkww9T3BlbkFJN9V0YQU7FdzielolJ3vr")  # Replace with your OpenAI API key

    def run(self, input_text):
        response = self.llm(input_text)
        return response

# Initialize LangChain
lc = LangChain()
lc.add_chain("chat_agent", SimpleChatAgent())

st.title("Simple Chat Agent")

# Input from the user
user_input = st.text_input("You:", placeholder="Type your message here...")

# Placeholder for the response
response_placeholder = st.empty()

# Function to get response from your LangChain agent deployed locally
def get_response(user_input):
    url = "http://localhost:8000/chat_agent"  # Change this URL if deployed elsewhere
    response = requests.post(url, json={"input": user_input})
    return response.json()["response"]

# Handling user input
if user_input:
    response = run(user_input)
    response_placeholder.text(f"Chat Agent: {response}")

