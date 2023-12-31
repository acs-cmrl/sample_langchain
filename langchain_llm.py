import os
import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SimpleSequentialChain, SequentialChain

os.environ["OPENAI_API_KEY"] = "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"

st.title("Youtube title and script with ChatGPT")
prompt = st.text_input('Prompt Here')

title_template = PromptTemplate(
    input_variables = ['topic'],
    template = 'write my a youtube video title about {topic}'    
)

script_template = PromptTemplate(
    input_variables = ['title'],
    template = 'write my a youtube video script based on this title TITLE: {title}'    
)

llm = OpenAI(temperature=0.9)
title_chain = LLMChain(llm=llm, prompt=title_template, verbose=True, output_key='title')
script_chain = LLMChain(llm=llm, prompt=script_template, verbose=True, output_key='script')
sequential_chain = SequentialChain(chains=[title_chain, script_chain], input_variables=['topic'], output_variables=['title','script'],verbose=True)

if prompt:
    response = sequential_chain({'topic':prompt})
    st.write(response['title'])
    st.write(response['script'])