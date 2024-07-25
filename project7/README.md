# master-ai-certification-course

# CSV Analysis App

## Overview

This project is a web application built using Streamlit that allows users to upload a CSV file and perform various analyses based on their queries. The application leverages the LangChain framework and a Hugging Face language model to process the data and provide insights.

## Features

- Upload a CSV file.
- Enter a query to perform analysis on the uploaded data.
- Receive responses and observations based on the query.

## Technologies Used

- **Streamlit**: For building the interactive web application.
- **LangChain**: To create and manage agents for processing data and queries.
- **Hugging Face**: Provides the language model endpoint for natural language processing.
- **Pandas**: For data manipulation and analysis.

## Setup

### Prerequisites

- Python 3.7 or later
- Streamlit
- LangChain
- Hugging Face library
- Pandas
- Python-dotenv (for environment variables)

### Installation

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/your-username/your-repo.git
    cd your-repo
    ```

2. **Create a Virtual Environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set Up Environment Variables:**

    Create a `.env` file in the root directory of the project and add the necessary environment variables. For example:

    ```env
    HUGGINGFACE_API_KEY=your_huggingface_api_key
    ```

5. **Run the Application:**

    ```bash
    streamlit run your_script.py
    ```

## Usage

1. **Navigate to the Application:**

    Open your web browser and go to `http://localhost:8501` (or the URL where Streamlit is running).

2. **Upload a CSV File:**

    Use the file uploader to select and upload your CSV file.

3. **Enter a Query:**

    Type your query in the text area provided. The query should be related to the data you uploaded.

4. **Generate Response:**

    Click the "Generate Response" button to receive the analysis results and observations.

## Code Structure

- `your_script.py`: The main script for running the Streamlit application.
- `utils.py`: Contains the `query_agent` function that interacts with LangChain and Hugging Face to process queries and data.
- `.env`: Stores environment variables for API keys and other configuration settings.
- `requirements.txt`: Lists all the required Python packages for the project.

![Screenshot 2024-07-24 084128](https://github.com/user-attachments/assets/837b6da5-0acc-40ea-b11b-2ed104b0540d)

![Screenshot 2024-07-24 084108](https://github.com/user-attachments/assets/054ad9e8-25fa-42f0-b61f-781baa26e8ee)


## Troubleshooting

- **If the application fails to start:**
  - Ensure all dependencies are installed correctly.
  - Check for any missing or incorrect environment variables.

- **If you encounter issues with query processing:**
  - Verify that the CSV file is correctly formatted.
  - Ensure that the query is compatible with the model and data.

## Contributing

Feel free to fork the repository and submit pull requests. Contributions to improve the functionality or fix issues are welcome.
