# Restaurant Helper App

## Overview

The **Restaurant Helper** is a Streamlit web application designed to assist users in generating restaurant names and menu options based on selected cuisines. It leverages a language model powered by OpenAI's GPT-3.5 for natural language processing and creativity.

## Features

- **Cuisine Selection**: Users can choose from a variety of cuisines, including Indian, Italian, Mexican, Chinese, Arabic, American, and Continental.

- **Dynamic Suggestions**: Upon selecting a cuisine, the app dynamically generates and displays a suggested restaurant name and menu options using a custom-built language model.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/restaurant-helper-app.git
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```

## Usage

1. Open the Streamlit app in your web browser.

2. Use the sidebar to select a cuisine from the available options.

3. The app will generate and display a suggested restaurant name and menu based on the chosen cuisine.

## Customization

- **Language Model**: The app utilizes OpenAI's GPT-3.5. You can experiment with different language models or adjust parameters for temperature and other settings in the `myModel.py` file.

## Project Structure

- **app.py**: The main Streamlit application script.
- **myModel.py**: Contains the custom language model and functions for generating restaurant names and menus.
- **myKey.py**: Placeholder file for storing the OpenAI API key (not included in the repository).

## Dependencies

- Streamlit
- langchain
- OpenAI GPT-3.5

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- [Streamlit](https://www.streamlit.io/)
- [OpenAI](https://www.openai.com/)

Feel free to explore, modify, and enhance the **Restaurant Helper App** to suit your needs!
