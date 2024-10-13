import numpy as np
import pandas as pd
import json
import pickle
import openai
import os
from crewai import Agent, Task, Process, Crew
from langchain_community.tools import DuckDuckGoSearchResults
from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings
from langchain.chains.summarize import load_summarize_chain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain import PromptTemplate
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import chroma
from langchain.document_loaders import TextLoader
from langchain.tools import tool
from langchain_community.tools.tavily_search import TavilySearchResults

from dotenv import load_dotenv
import base64
import glob
import os

import openai

from openai import OpenAI

load_dotenv()

# the chat generation model 
openaigpt4 = ChatOpenAI(model='gpt-4o', 
                        temperature=0.2, 
                        api_key=os.getenv('openapi_key'))

os.environ['TAVILY_API_KEY']=os.getenv('tavilyapi_key')

SearchTools = TavilySearchResults(k=3)
