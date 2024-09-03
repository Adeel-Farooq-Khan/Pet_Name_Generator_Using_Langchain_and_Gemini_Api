## 🚀 Features

- Generate unique and creative pet names based on user input.
- Simple and interactive web interface built with Streamlit.
- Powered by LangChain and Gemini LLM for natural language generation.

## 🛠️ Tech Stack

- **Streamlit**: Python library for creating interactive web apps.
- **LangChain**: Framework for building applications with large language models (LLMs).
- **Google Gemini API**: LLM for creative text generation.

## 📚 Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/yourusername/pet-name-generator.git
    cd pet-name-generator
    ```

2. **Create a virtual environment** (recommended):

    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. **Install the required dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up the environment variables**:

    Create a `.env` file in the root directory and add your Google API key:

    ```plaintext
    GOOGLE_API_KEY=your_google_api_key
    ```

5. **Run the Streamlit app**:

    ```bash
    streamlit run app.py
    ```

6. **Open your browser** and go to `http://localhost:8501` to see the app in action!

## ⚙️ How It Works

1. The user enters the pet's name and color in the Streamlit interface.
2. The app sends this data to the LangChain LLM using the Gemini API to generate creative pet names.
3. The generated names are displayed in the app for the user.

## 🐞 Troubleshooting

- If you encounter deprecation warnings or errors related to the `GooglePalm` class in LangChain, try updating the library or using an alternative LLM class. Check the [LangChain documentation](https://langchain.com/docs/) for more details.


## 🙌 Acknowledgments

- Thanks to the developers of [LangChain](https://langchain.com) and [Streamlit](https://streamlit.io).
- Inspired by my passion for AI and love for pets!
