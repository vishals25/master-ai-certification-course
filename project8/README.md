# YouTube Script Writing Tool

This is a Streamlit application designed to help you generate YouTube video scripts using the OpenAI API. The app captures user inputs for the video topic, expected video length, and creativity level, and then generates a script based on these inputs.

## Features

- **Styled Buttons**: Custom styling for buttons.
- **Session State Management**: Uses Streamlit's session state to manage the OpenAI API key securely.
- **Sidebar Input**: Capture the OpenAI API key from the user.
- **User Inputs**: Capture video topic, expected video length, and creativity level from the user.
- **Script Generation**: Generates a YouTube video script using the OpenAI API.
- **Display Results**: Displays the generated title, script, and search engine results.

## Installation

To run this application, you need to have Python installed on your machine. Follow the steps below to set up and run the app.

1. Clone this repository:

    ```bash
    git clone https://github.com/your-repo/youtube-script-writing-tool.git
    cd youtube-script-writing-tool
    ```

2. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the Streamlit app:

    ```bash
    streamlit run app.py
    ```

## Usage

1. Open the app in your browser.
2. Enter your OpenAI API key in the sidebar.
3. Provide the topic of your video, expected video length, and set the creativity limit.
4. Click on "Generate Script for me" to get the script.
5. View the generated title, script, and search engine results.

## Screenshots

![alt text](images/2.png)
![alt text](images/1.png)
