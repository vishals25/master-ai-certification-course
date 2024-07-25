# Educate Kids

## Overview

This is a Streamlit-based web application that helps find similar content from a CSV file using embeddings and FAISS for similarity search. The application is designed to assist in educational activities for kids by providing similar topics or concepts based on user queries.

Chat Model used is - `huggingfaceh4/zephyr-7b-alpha`

## Features

- Load data from a CSV file.
- Use HuggingFace embeddings for semantic search.
- Perform similarity search using FAISS.
- Interactive user interface to input queries and get results.

## Example

1. Enter text: "What is photosynthesis?"
2. Click: "Find similar Things"

The app will return the top matches from the CSV file that are similar to the entered query.

![Screenshot 2024-07-09 195400](https://github.com/vishals25/master-ai-certification-course/assets/142819017/567940ae-e216-4f49-97a2-508f3ac6d77e)


## Dependencies

- `streamlit`: Web app framework for interactive applications.
- `langchain`: Toolkit for building language model applications.
- `huggingface_hub`: Interface to HuggingFace models.
- `langchain_community`: Community tools and resources for LangChain.
- `python-dotenv`: Load environment variables from a .env file.
