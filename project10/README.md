# Automatic Ticket Classification Tool

## Overview

This project is a web application built using Streamlit that classifies user-submitted tickets into different departments (HR, IT, and Transport) based on the content of the ticket. The application leverages embeddings and machine learning models to analyze the input and determine the appropriate department for each ticket.

## Features

- Capture user input for ticket classification.
- Classify tickets into HR, IT, or Transport departments.
- Store classified tickets in session state for later use.

## Technologies Used

- **Streamlit**: For building the interactive web application.
- **Pinecone**: For storing and retrieving vector embeddings.
- **LangChain**: To create and manage agents for processing data and queries.
- **Hugging Face**: Provides the language model endpoint for natural language processing.
- **dotenv**: For managing environment variables.
- **Python**: General programming and scripting.

## Setup

### Prerequisites

- Python 3.7 or later
- Streamlit
- Pinecone
- LangChain
- Hugging Face library
- dotenv

## Code Structure

- `your_script.py`: The main script for running the Streamlit application.
- `user_utils.py`: Contains utility functions for creating embeddings, pulling from Pinecone, getting similar documents, and predicting the department.
- `.env`: Stores environment variables for API keys and other configuration settings.
- `requirements.txt`: Lists all the required Python packages for the project.

## Attachments

![alt text](images/74029.png)
![alt text](images/74119.png)
![alt text](images/74133.png)
![alt text](images/74718.png)
![alt text](images/74727.png)
![alt text](images/74744.png)
![alt text](images/74757.png)
