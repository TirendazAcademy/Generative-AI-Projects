from dotenv import load_dotenv 
from openai import OpenAI
import streamlit as st

load_dotenv()
client = OpenAI()

def get_openai_response(question):
    completion = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages = [
            {"role":"system", "content":"You are a helpful assistant"},
            {"role":"user", "content": question},
        ],
        max_tokens = 200,
    )
    return completion.choices[0].message.content 

# print(get_openai_response("hello"))

st.set_page_config(page_title = "Text-Generation Demo")
st.header("Text-Generation with OpenAI API")

input_text = st.text_input("Ask me anything: ",key = "input")
submit_button = st.button("Get the answer")

if submit_button:
    st.subheader("Thinking...")
    with st.spinner("Analyzing the question..."):
        response = get_openai_response(input_text)
    st.subheader("The answer is: ")
    st.success(response)
    st.markdown("*Voila!*")    
