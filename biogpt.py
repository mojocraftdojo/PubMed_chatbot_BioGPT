"""Module to interact with biogpt, accept user input and generate outputs"""

from transformers import pipeline, set_seed
from transformers import BioGptTokenizer, BioGptForCausalLM
import streamlit as st

import random


#set_seed(42)

random_seed = random.randint(1,1000)
random_seed
set_seed(random_seed)


XFORMERS_MORE_DETAILS=1


model = BioGptForCausalLM.from_pretrained("microsoft/biogpt")
tokenizer = BioGptTokenizer.from_pretrained("microsoft/biogpt")
generator = pipeline("text-generation",model=model,tokenizer=tokenizer)

@st.cache_resource
def generate_response(prompt):
    message = generator(
        prompt,
        max_length=200,
        num_return_sequences=1,
        do_sample=True
    )
    return message[0]['generated_text']


def get_text():
    input_text = st.text_input("Your query: ","", key="input")
    return input_text 

