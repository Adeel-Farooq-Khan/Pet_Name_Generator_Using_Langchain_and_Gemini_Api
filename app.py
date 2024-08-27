import os
import streamlit as st
from langchain import LLMChain
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from dotenv import load_dotenv

load_dotenv()


api_key = os.getenv("GOOGLE_API_KEY")

def generate_pet_names(name, color):

    prompt_template = PromptTemplate(
        input_variables=["name", "color"],
        template="Based on the name '{name}' and the color '{color}', suggest 5 creative pet names:"
    )


    llm = OpenAI(api_key=api_key, model="gpt-3.5-turbo")  # Adjust model as necessary


    chain = LLMChain(llm=llm, prompt=prompt_template)


    response = chain.run({"name": name, "color": color})


    pet_names = response.strip().split('\n')

    return pet_names[:5]

st.title("Pet Name Generator")
st.write("Generate creative pet names based on a given name and color!")


name = st.text_input("Enter the pet's name:")
color = st.text_input("Enter the pet's color:")

if st.button("Generate Names"):
    if name and color:
        names = generate_pet_names(name, color)
        st.write("Here are 5 suggested pet names:")
        for i, pet_name in enumerate(names, 1):
            st.write(f"{i}. {pet_name}")
    else:
        st.write("Please provide both a name and a color.")
