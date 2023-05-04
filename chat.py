import streamlit as st
from streamlit_chat import message as st_message
import time

from langchain import OpenAI
from langchain.chains.question_answering import load_qa_chain
from langchain.chains import AnalyzeDocumentChain
from langchain.document_loaders import TextLoader
from langchain.indexes import VectorstoreIndexCreator

from auth import API_KEY
import openai
import os
import random



#message history
if "history" not in st.session_state:
    st.session_state.history = []

os.environ['OPENAI_API_KEY'] = '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'

with open("data/y1crit.txt") as f:
    text_in = f.read()

#testing vectorstore index
loader = TextLoader("data/lemma.txt")
index = VectorstoreIndexCreator().from_loaders([loader])


llm = OpenAI(temperature=.5)
qa_chain = load_qa_chain(llm, chain_type="map_reduce")
qa_document_chain = AnalyzeDocumentChain(combine_docs_chain=qa_chain)


def update_model():
    #llm = OpenAI(temperature=.5)
    #qa_chain = load_qa_chain(llm, chain_type="map_reduce")
    #qa_document_chain = AnalyzeDocumentChain(combine_docs_chain=qa_chain)
    index.refresh()

def update_model_limited():
    llm = OpenAI(batch_size=5,temperature=.5)
    a_chain = load_qa_chain(llm, chain_type="map_reduce")
    qa_document_chain = AnalyzeDocumentChain(combine_docs_chain=qa_chain)



def get_response(msg):
    #response = qa_document_chain.run(input_document=text_in,question=msg)
    response = index.query(msg)

    user_message = msg
    bot_message = response

    st.session_state.history.append({"message": user_message, "is_user": True})
    st.session_state.history.append({"message": bot_message, "is_user": False})


    #return response

def test(msg):
    user_message = msg
    bot_message = msg[::-1]

    st.session_state.history.append({"message": user_message, "is_user": True})
    st.session_state.history.append({"message": bot_message, "is_user": False})

if 'something' not in st.session_state:
    st.session_state.something = ''

#clear input box after press enter
def submit():
        st.session_state.something = st.session_state.input
        st.session_state.input = ''


def displayResponse(user_input):
    if user_input:
        #st.write(get_response(user_input))
        with st.spinner("Generating Response"):
            st.write(get_response(user_input))
        #get_response(user_input)
        
        #st.write((user_input))


st.title("UTD ChatBot")
user_input = st.text_input("", placeholder= "Ask me question about UTD")    
#user_input = st.session_state.something
st.empty()

if user_input:
    
    #st.write(get_response(user_input))
    with st.spinner("Generating Response"):
        st.write(get_response(user_input))
    #get_response(user_input)
    
    #st.write((user_input))


for chat in st.session_state.history:
    st_message(**chat)