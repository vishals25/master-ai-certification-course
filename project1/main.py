import streamlit as st
import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

install("langchain_community")


from langchain.llms import HuggingFaceEndpoint


def load_answer(question):
    llm=HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.3"
    )

    result=llm.invoke(question)

    return result
    
st.title("Langchain Demo")


def get_text():
    input=st.text_input(label="Enter A question:",placeholder='example: how to make lime juice?',key='new_question')
    return input

user_input=get_text()

submit=st.button("Generate")

if submit and user_input!="":

    st.subheader("Answer:")
    response=load_answer(user_input)
    st.write(response)