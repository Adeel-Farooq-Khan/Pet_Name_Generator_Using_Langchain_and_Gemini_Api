import streamlit as st
from langchain import LLMChain
from langchain.llms import OpenAI  # Assuming Gemini uses OpenAI-compatible API


# Function to generate pet names
def generate_pet_names(name, color):
    # Define the prompt template
    prompt = (
        f"Based on the name '{name}' and the color '{color}', suggest 5 creative pet names: "
    )

    # Initialize the LLM with the Gemini API
    llm = OpenAI(api_key="your_gemini_api_key", model="gpt-3.5-turbo")  # Adjust the model if necessary

    # Create a LangChain instance with the prompt
    chain = LLMChain(llm=llm, prompt_template=prompt)

    # Run the LLM to get the response
    response = chain.run()

    # Assuming the response is a string with names separated by newlines
    pet_names = response.split('\n')

    return pet_names[:5]  # Return only 5 names


# Streamlit app
st.title("Pet Name Generator")
st.write("Generate creative pet names based on a given name and color!")

# User inputs
name = st.text_input("Enter the pet's name:")
color = st.text_input("Enter the pet's color:")

# Generate names on button click
if st.button("Generate Names"):
    if name and color:
        names = generate_pet_names(name, color)
        st.write("Here are 5 suggested pet names:")
        for i, pet_name in enumerate(names, 1):
            st.write(f"{i}. {pet_name}")
    else:
        st.write("Please provide both a name and a color.")
