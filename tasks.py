import os
from agents import Agents
from tools import *
from dotenv import load_dotenv

load_dotenv()


# the chat generation model 
openaigpt4 = ChatOpenAI(model='gpt-4o', 
                        temperature=0.2, 
                        api_key=os.getenv('openapi_key'))

class Tasks:
    def __init__(self, Input):
        self.Input = Input

    def SearchDataTask(self):
        CocoaSearchData = Task(
            description = """Research and gather detailed information on {}, specifically related to cacao farming, diseases, or agricultural practices.
                             Use the search_tool to find reliable and relevant data.
                             Ensure accuracy by cross-referencing multiple sources and focus on practical solutions, causes, prevention, and treatment methods. 
                             Incorporate any relevant context or expert advice to provide a comprehensive understanding of the topic.""".format(self.Input), 
            expected_output = """A detailed and well-researched report that includes:
                                 - A clear explanation of the issue or query.
                                 - Causes, symptoms, and effects related to the topic.
                                 - Practical solutions and treatment methods.
                                 - Preventive measures and expert recommendations.
                                 - Citations from credible sources to support the information provided.""",
        agent=Agents().DataSearch(),
        tools=[SearchTools])

        return CocoaSearchData
    
    def ContextUserQuer(self):
        ContextedUserQuer = Task(
            description = """Analyze the data based on the user query = {}.
                             Provide a clear and concise context for the identified problem, focusing on practical implications and actionable insights.
                             Include key points for analysis to assist in expert decision-making.""".format(self.Input), 
            expected_output="""A structured and easy-to-process report that includes:
                                  - A concise summary of the problem or query.
                                  - Key factors contributing to the issue.
                                  - Practical solutions and recommendations.
                                  - Important considerations for further analysis.
                                  - Contextual insights to support the expert's advice and decision-making process.""", 
            agent=Agents().CustServ(),
            )
        return ContextedUserQuer
    
    def AugmentContext(self):
        AugmentedContext = Task(
            description = """Review and adjust the provided context to ensure it accurately addresses the user's query. user query = {}
                             Assess the relevance of the context with respect to the user's query and, if necessary, refine it to better align with the specific needs.
                             Use search_tool if additional information or clarification is needed to enhance the context.""".format(self.Input), 
            expected_output="""A refined and contextually accurate report that includes:
                                - A clear understanding of the user's query.
                                - An evaluation of the current context's relevance and accuracy.
                                - Adjustments or refinements made to improve alignment with the query.
                                - Any additional information sourced to enhance context.""", 
            agent=Agents().Augment()
            )
        return AugmentedContext

    def AnalyseAugContext(self):
        AnalysedAugContext = Task(
            description = """Analyze the verified context related to the user's query and provide an in-depth response that offers practical and actionable advice.
                             Use your expertise in cacao farming to assess the situation described in the context and recommend strategies or solutions that address the key points raised.
                             If needed, use search_tool to gather additional information to support your analysis.""", 
            expected_output="""A detailed analysis report MUST IN BAHASA INDONESIA that includes:
                                  - An in-depth examination of the key points within the context.
                                  - Practical and actionable advice tailored to the user's query.
                                  - Specific recommendations for addressing the issues mentioned in the context.
                                  - Any additional information or strategies sourced from reliable references to enhance the response.
                                  - Refferences used 
                                  YOU MUST USE BAHASA INDONESIA""", 
            agent=Agents().Adviser(),
            tools=[SearchTools])
        return AnalysedAugContext