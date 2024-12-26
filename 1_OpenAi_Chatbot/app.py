import streamlit as st
import openai
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

import os
from dotenv import load_dotenv

load_dotenv()


# Langchain tracking
os.environ['LANGCHAIN_API_KEY'] = os.getenv('LANGCHAIN_API_KEY')
os.environ['LANGCHAIN_TRACING_V2'] = 'true'
os.environ['LANGCHAIN_PROJECT'] = "Q&A Chatbot with OpenAi"

# Prompt Template 
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are helpful assistant. PLease respond to the user queries"),
        ("user","Question:{question}")
    ]
)

def generate_response(question,api_key,engine,temperature,max_tokens):
    openai.api_key=api_key
    llm=ChatOpenAI(model=engine, openai_api_key=api_key)
    output_parser=StrOutputParser()
    chain=prompt|llm|output_parser
    answer=chain.invoke({'question':question})
    return answer

# Title of the app
st.title('Q&A Chatbot with Open AI')

# Sidebar for settings
st.sidebar.title('Settings')
api_key= st.sidebar.text_input('Enter your Open API Key', type="password")

# Drop down to select various Open AI models
engine= st.sidebar.selectbox('Select an Open AI model',['gpt-4','gpt-3.5-turbo'])

# Adjust response parameter
temperature = st.sidebar.slider('Temperature', min_value=0.0,max_value=1.0,value=0.7)
max_tokens = st.sidebar.slider('Max Tokens', min_value=50,max_value=300,value=150)


# Main Interface
st.write('Ask any question')
user_input=st.text_input('You:')

if user_input and api_key:
    response=generate_response(user_input,api_key,engine,temperature,max_tokens)
    st.write(response)
    
elif user_input:
    st.warning("Please enter the OPen AI aPi Key in the sider bar")
else:
    st.write('Please provide the query')
    

