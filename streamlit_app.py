import streamlit as st
from langchain.llms import OpenAI

st.title('🦜🔗 Quickstart App')

openai_api_key = "sk-proj-1LH6p4ZoVbyGSjxrkww9T3BlbkFJN9V0YQU7FdzielolJ3vr"

def generate_response(input_text):
  llm = OpenAI(temperature=0.7, openai_api_key="sk-proj-1LH6p4ZoVbyGSjxrkww9T3BlbkFJN9V0YQU7FdzielolJ3vr")
  st.info(llm(input_text))

with st.form('my_form'):
  text = st.text_area('Enter text:', 'What are the three key pieces of advice for learning how to code?')
  submitted = st.form_submit_button('Submit')
  if submitted and openai_api_key.startswith('sk-'):
    generate_response(text)
