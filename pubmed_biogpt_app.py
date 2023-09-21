"""Module to create a chatbot interface, accept user input and generate output"""
import streamlit as st
from streamlit_chat import message


st.set_page_config(
    page_title="Biomedical Literature Research Tools"
)
st.header("Biomedical Literature LLM Chatbot")
st.sidebar.header("USAGE INSTRUCTIONS")
st.sidebar.info(
    '''This is a web app that allows you to interact with the 
    BioGPT chatbot trained on large-scale biomedical literature.
    Welcome to try any scientific terms or questions that interest you.
    '''
    )
st.sidebar.info('''Enter a keyword or a short seed question in the text box and press enter
    to receive gap-fill responses.(e.g.The cause of Type 2 diabetes is; TP53 plays a role in) ''')

st.sidebar.info('''BioGPT Exploration mode is turned ON. So new responses will be generated for each query rerun.''')

if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []


model = st.radio(
    "What task would you like to perform?",
    ['PubMed mining and question-answering tool']
    )


if model == 'PubMed mining and question-answering tool':    
    st.text("PubMed is a free, extensive online database of medical and life sciences articles.")
    st.text("Loading... The query box will appear shortly. Please enter your query after that.")
    st.text("Example query: IL-6; TP53 is, Inflammation related genes include; etc")
    from biogpt import *
else:
    import numpy
    

user_input = get_text()

if user_input:
    output = generate_response(user_input)
    st.session_state.past.append(user_input)
    st.session_state.generated.append(output)

if st.session_state['generated']:
    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state["generated"][i], key=str(i))
#        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
