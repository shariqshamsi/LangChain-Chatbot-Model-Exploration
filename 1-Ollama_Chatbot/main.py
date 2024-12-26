from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st
import os

from dotenv import load_dotenv

load_dotenv()


# Langchain tracking
os.environ['LANGCHAIN_API_KEY'] = os.getenv('LANGCHAIN_API_KEY')
os.environ['LANGCHAIN_TRACING_V2'] = 'true'
os.environ['LANGCHAIN_PROJECT'] = "Q&A Chatbot with Ollama"


# Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are helpful assistant. PLease respond to the user queries"),
        ("user","Question:{question}")
    ]
)

def generate_response(question,engine,temperature,max_tokens):
    
    llm=Ollama(model=engine)
    output_parser=StrOutputParser()
    chain=prompt|llm|output_parser
    answer=chain.invoke({'question':question})
    return answer

# Title of the app
st.title('Q&A Chatbot with Ollama')

# Drop down to select various Open AI models
engine= st.sidebar.selectbox('Select an Open AI model',['gemma2:2b'])

# Adjust response parameter
temperature = st.sidebar.slider('Temperature', min_value=0.0,max_value=1.0,value=0.7)
max_tokens = st.sidebar.slider('Max Tokens', min_value=50,max_value=300,value=150)


# Main Interface
st.write('Ask any question')
user_input=st.text_input('You:')

if user_input:
    response=generate_response(user_input,engine,temperature,max_tokens)
    st.write(response)
    
else:
    st.write('Please provide the query')
    

