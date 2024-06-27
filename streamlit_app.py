import streamlit as st
from langchain.llms import OpenAI

st.title('🦜🔗 Quickstart App')

openai_api_key = st.sidebar.text_input('sk-proj-1LH6p4ZoVbyGSjxrkww9T3BlbkFJN9V0YQU7FdzielolJ3vr')

def generate_response(input_text):
  self.llm = OpenAI()  # Replace with your OpenAI API key
  llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
  st.info(llm(input_text))

with st.form('my_form'):
  text = st.text_area('Enter text:', 'What are the three key pieces of advice for learning how to code?')
  submitted = st.form_submit_button('Submit')
  if not openai_api_key.startswith('sk-'):
    st.warning('Please enter your OpenAI API key!', icon='⚠')
  if submitted and openai_api_key.startswith('sk-'):
    generate_response(text)

import streamlit as st
import requests
from langchain.chains import LLMChain
from langchain.llms import OpenAI

# chat_agent.py
class SimpleChatAgent(LLMChain):
    def __init__(self):
        self.llm = OpenAI(api_key="sk-proj-1LH6p4ZoVbyGSjxrkww9T3BlbkFJN9V0YQU7FdzielolJ3vr")  # Replace with your OpenAI API key

    def run(self, input_text):
        response = self.llm(input_text)
        return response

# Initialize LangChain
lc = LLMChain()
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
