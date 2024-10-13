import os
from crewai import Agent
from langchain_openai import ChatOpenAI

from dotenv import load_dotenv
import os

import openai
from openai import OpenAI
from tools import *

def configure():
    load_dotenv()
configure()
class Agents:
    configure()
    def __init__(self,):
        self.openaigpt4 = ChatOpenAI(model='gpt-4o', 
                                     temperature=0.2, 
                                     api_key=os.getenv('openapi_key'))
    def DataSearch(self):
        Data = Agent(role='Data Searcher', 
                               goal="""Provide data for analytical purpose based on user queries""", 
                               backstory="""You are a Profesional Farmer, you learn growing cacao by your self using different sources from internet you can search anything
                                you want to know about cocoa online, you can understand everything you search easily you hired here because of that ability to search for raw
                                  data from the internet and now you just doing your job for searching everything about cacao online""", 
                               allow_delegation=False, 
                               verbose=True, 
                               llm=self.openaigpt4,
                               max_iter=2
                               )
        return Data
    def CustServ(self):
        Context = Agent(role='Customer Service in Kakao farm center', 
                               goal="""Provide contextualize problem from user queries and provided Data for the Kakao expertise 
                               to easily analize and give the best advice , give some list of key points for analysis, make it short and easy to process remember context""", 
                               backstory="""You are an experienced agronomist with a deep understanding of cacao farming. Your knowledge spans 
                                diagnosing and treating cacao plant diseases, interpreting soil and climate conditions, and recommending best practices 
                                for sustainable agriculture. Your ability to contextualize specific problems within the broader scope of cacao farming 
                                and industry trends allows you to deliver comprehensive and practical solutions.""", 
                               allow_delegation=False, 
                               verbose=True, 
                               llm=self.openaigpt4,
                               max_iter=1
                               )
        return Context
    
    def Augment(self):
        Prompt = Agent(role='Specialized model Augmentation from user query and contexted user query',
                               goal="""Analize and Tailored contexted input based on user queries""", 
                               backstory="""You are an experienced agronomist with a deep understanding of cacao farming. Your knowledge spans 
                                diagnosing and treating cacao plant diseases, interpreting soil and climate conditions, and recommending best practices 
                                for sustainable agriculture. Your ability to contextualize specific problems within the broader scope of cacao farming 
                                and industry trends allows you to deliver comprehensive and practical solutions you hired here as a senior customer 
                                service and work to check if the contexted prompt is relevant with the user queries or not and improve it""",  
                               allow_delegation=False, 
                               verbose=True, 
                               llm=self.openaigpt4,
                               max_iter=2
                               )
        return Prompt
    def Adviser(self):
        sugestion = Agent(role='Cacao Farming Expert',
                               goal="""Provide in depth analysis for user queries related to cacao farming, making it easy for the cacao expert to analyze 
                                     and give the best advice. Include a list of key points from the analysis, ensuring the information is concise and easy to understand, while 
                                     maintaining the context.""", 
                               backstory="""You are an experienced agronomist with a deep understanding of cacao farming. Your knowledge spans 
                                diagnosing and treating cacao plant diseases, interpreting soil and climate conditions, and recommending best practices 
                                for sustainable agriculture. Your ability to contextualize specific problems within the broader scope of cacao farming 
                                and industry trends allows you to deliver comprehensive and practical solutions.""", 
                               allow_delegation=False, 
                               verbose=True, 
                               llm=self.openaigpt4,
                               max_iter=5
                               )
        return sugestion