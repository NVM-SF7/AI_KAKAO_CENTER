import streamlit as st
from crewai import Process, Crew
from agents import *
from tasks import *
from dotenv import load_dotenv   

def Main():

    UserQueries = st.text_input("Ask us anything about cacao farming, care, or management:")
    submit = st.button("Tanyakan !")
    if  submit and UserQueries != "":
        st.write('**Your Query:**')
        st.write(f"> {UserQueries}")
        st.write("Model is processing the answer, please wait...")

        CacaoSupportServiceCrew = Crew(
            agents=[Agents().DataSearch(), Agents().CustServ(), Agents().Augment(), Agents().Adviser()], 
            tasks=[Tasks(UserQueries).SearchDataTask(), Tasks(UserQueries).ContextUserQuer(), Tasks(UserQueries).AugmentContext(), Tasks(UserQueries).AnalyseAugContext()], 
            process=Process.sequential, 
            manager_llm=openaigpt4
        )

        results = CacaoSupportServiceCrew.kickoff() 
        st.success("Here are the results:")
        st.markdown(results)
    elif submit and UserQueries == "":
        st.warning("Please enter a query to get started.")