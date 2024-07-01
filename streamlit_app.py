import streamlit as st
import openai

openai.api_key = st.secrets["openai"]["api_key"]

st.title("Nour AI!🤖")
st.set_page_config(
    layout="wide"
)
