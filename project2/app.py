import streamlit as st
import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

install("langchain_community")
install("huggingface_hub")


from langchain.llms import HuggingFaceHub


def load_answer(question):
    llm = HuggingFaceHub(
    repo_id="huggingfaceh4/zephyr-7b-alpha", 
    model_kwargs={"temperature": 0.5, "max_length": 64,"max_new_tokens":512}
    )

    result=llm.predict(question)

    return result
    
st.title("Langchain Demo Using Chat Model:")


def get_text():
    input=st.text_input(label="Enter A Chat:",placeholder='how are you?',key='new_question')
    return input

user_input=get_text()

submit=st.button("Chat")

if submit and user_input!="":

    st.subheader("Reply:")
    response=load_answer(user_input)
    st.write(response)