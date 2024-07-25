# Marketing Tool

## Overview

This is a Streamlit-based web application that generates marketing content using a language model from HuggingFace. The app can create sales copy, tweets, and product descriptions tailored to different age groups, including Kids, Adults, and Senior Citizens.

Chat Model used is - `huggingfaceh4/zephyr-7b-alpha`

## Features

- Generate marketing content based on user input
- Select content type: Sales copy, Tweet, Product description
- Choose target age group: Kid, Adult, Senior Citizen
- Adjustable word limit for the generated content

## Example

- Enter text: "What is a mobile?"
- Select action: "Write a sales copy"
- Select age group: "Kid"
- Adjust word limit: 100 words

Click "Generate" to get a fun and engaging sales copy suitable for kids.

![image](https://github.com/vishals25/master-ai-certification-course/assets/142819017/3eebe3ad-f8d9-4fc5-98ad-129d735abef3)


## Dependencies

- **streamlit:** Web app framework for interactive applications.
- **langchain:** Toolkit for building language model applications.
- **huggingface_hub:** Interface to HuggingFace models.
- **python-dotenv:** Load environment variables from a .env file.
