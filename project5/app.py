import streamlit as st
import json
from streamlit_chat import message  # Ensure this custom module is available
# from langchain_huggingface import HuggingFaceEndpoint
from langchain_community.llms import HuggingFaceHub

# Initialize session state variables if they don't exist
if 'conversation' not in st.session_state:
    st.session_state['conversation'] = None
if 'messages' not in st.session_state:
    st.session_state['messages'] = []

# Initialize the summarization model
llm = HuggingFaceHub(
    repo_id="google/pegasus-cnn_dailymail",
    model_kwargs={
        "max_length": 1024,
        "temperature": 0.9,
        "max_new_tokens": 1024
    }
)

# Initialize the chat model
llms = HuggingFaceHub(
    repo_id="HuggingFaceH4/zephyr-7b-alpha",
    model_kwargs={
        "temperature": 0.7,
        "max_length": 65,
        "max_new_tokens": 512,
        "top_p": 0.9,
        "stop_sequence": ["\n"],
        "return_full_text": False
    }
)

st.set_page_config(page_title="Chat GPT Clone", page_icon=":robot_face:")
st.markdown("<h1 style='text-align: center;'>How can I assist you? </h1>", unsafe_allow_html=True)

st.sidebar.title("😎")
summarise_button = st.sidebar.button("Summarise the conversation", key="summarise")

if summarise_button and st.session_state['messages']:
    conversation_str = json.dumps(st.session_state['messages'], indent=4)
    summary = llm.invoke(conversation_str)
    summary = summary.replace('<n>', "\n")
    st.session_state['conversation'] = summary
    st.sidebar.write("Nice chatting with you:\n\n")
    st.sidebar.write(st.session_state['conversation'])

container = st.container()

with container:
    with st.form(key='my_form'):
        user_input = st.text_area("Chat Here:", key='input', height=100)
        submit_button = st.form_submit_button(label='Send')

        if submit_button:
            model_response = llms.invoke(user_input)
            combined_response = user_input + "\n" + model_response  # Ensure correct combination
            st.session_state['messages'].append(combined_response)
            st.write("The Answer:\n\n" + combined_response)