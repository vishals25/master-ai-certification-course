import streamlit as st
from dotenv import load_dotenv
from utils import query_agent

# Load environment variables from a .env file
load_dotenv()

# Streamlit UI elements
st.title("Let's do some analysis on your CSV")
st.header("Please upload your CSV file here:")

# Capture the CSV file
data = st.file_uploader("Upload CSV file", type="csv")

# Capture the user's query
query = st.text_area("Enter your query")

# Button to generate response
button = st.button("Generate Response")

if button and data and query:
    # Get Response from the agent
    answer = query_agent(data, query)
    st.write(answer)
elif button:
    st.warning("Please upload a CSV file and enter a query before generating a response.")
