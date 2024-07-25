import streamlit as st
import os
from langchain.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv
load_dotenv()

st.set_page_config(page_title="Educate Kids", page_icon=":robot:")
st.header("Hey, Ask me something & I will give out similar things")


embeddings=HuggingFaceEmbeddings()

from langchain.document_loaders.csv_loader import CSVLoader
loader = CSVLoader(file_path='mydata.csv', csv_args={
    'delimiter': ',',
    'quotechar': '"',
    'fieldnames': ['Words']
})

data = loader.load()

print(data)

db = FAISS.from_documents(data, embeddings)


def get_text():
    input_text = st.text_input("You: ", key= input)
    return input_text


user_input=get_text()
submit = st.button('Find similar Things')  

if submit:
    
    docs = db.similarity_search(user_input)
    st.subheader("Top Matches:")
    if docs:
        for item in docs[1:]:
            st.write(item.page_content)
    else:
        st.write("No similar things found")


