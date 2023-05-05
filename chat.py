import streamlit as st
from streamlit_chat import message as st_message


from langchain.document_loaders import TextLoader
from langchain.indexes import VectorstoreIndexCreator
from auth import API_KEY
import os


#message history
if "query" not in st.session_state:
    st.session_state.query = []

if "response" not in st.session_state:
    st.session_state.response = []

os.environ['OPENAI_API_KEY'] = API_KEY


#testing vectorstore index
loader = TextLoader("data/lemma.txt")
index = VectorstoreIndexCreator().from_loaders([loader])


def update_model():
    index.refresh()


#return response
def get_response(msg):
    #response = qa_document_chain.run(input_document=text_in,question=msg)
    return index.query(msg)


if 'holder' not in st.session_state:
    st.session_state.holder = ''


#clear input box after press enter
def submit():
        
        st.session_state.holder = st.session_state.input
        st.session_state.input = ''
        
        
st.title("UTD ChatBot")
st.text_input("", placeholder= "Ask me question about UTD", key = 'input', on_change = submit)    
user_input = st.session_state.holder

if user_input:
        
    with st.spinner("Generating Response"):
        #st.write(get_response(user_input))
        user_message = user_input
        bot_message = get_response(user_input)

        st.session_state.query.append(user_message)
        st.session_state.response.append(bot_message)

     
if st.session_state.query:
    for i in range(len(st.session_state.query)-1,-1,-1):
        st_message(st.session_state.query[i], is_user = True, key = str(i) + '_user')
        st_message(st.session_state.response[i], is_user = False, key = str(i) + '_bot')