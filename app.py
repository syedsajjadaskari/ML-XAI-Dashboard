from src.ML_XAI_Dashboard.components import Home,DataInfo,RegPreProcessing,ClsPreProcessing,RegTraining,ClsTraining,RegModel,Prediction,ClsModel
import streamlit as st
import os
import pymongo
from pathlib import Path

PAGES={
    "Home": Home,
    "DataInfo":DataInfo,
    "PreProcessing": (RegPreProcessing, ClsPreProcessing),
    "Training":(RegTraining, ClsTraining),
    "Model Analysis":(RegModel, ClsModel),
    "Prediction And Save": Prediction,
}


footer="""
<style>
  footer {
    visibility: visible;
    margin-top: 50px;
    text-align: center;
  }
  
  footer a {
    color: #333;
    text-decoration: none;
    margin: 0 10px;
  }
  
  footer a:hover {
    color: #007bff;
  }
  
  footer:after {
    content: '|';
    margin: 0 10px;
    color: #ccc;
  }
  
  footer .coffee-link:after {
    content: ' ';
  }
  
  footer .linkedin-link:after {
    content: ' 'https://www.linkedin.com/in/syed-sajjad-askari-06b4bb101';
  }
</style>
"""

def run():
    state=st.session_state
    st.set_page_config(
        page_title='ML XAI DASHBOARD',
        layout='centered',
        initial_sidebar_state='expanded'
    )

    st.image("artifacts/Header.png")
    st.title("Machine Learning Explainable Dashboard")
    st.sidebar.title("Navigations")
    st.sidebar.image('artifacts/logo.png')
    st.info("This Application allows you to explain ML pipeline , Profiling, model and Explanation", icon="🤖")
    st.markdown(footer,unsafe_allow_html=True)
    selection = st.sidebar.radio("Go to", list(PAGES.keys()))

#To upload the file in the csv format
    if selection=="Home":
        try:
            state_df,task = PAGES[selection].write(state)
            state.df, state.task = state_df,task
            #To initializa the ignore columns and removed columns
            state.is_remove=False
            state.log_history={}
            state.ignore_columns = []
        except:
            st.header("Please Upload CSV or Excel first!..")
            st.stop()
    if selection=="DataInfo":
        PAGES[selection].write(state.df)

    if selection=="PreProcessing":
        if state.task=="Regression":
            PAGES[selection][0].write(state)
        else:
            PAGES[selection][1].write(state)

    if selection == "Training":
        if state.task == "Regression":
            PAGES[selection][0].write(state)
        else:           
            PAGES[selection][1].write(state)
    if selection == "Model Analysis":
        if state.task=="Regression":
            PAGES[selection][0].write(state)
        else:
            PAGES[selection][1].write(state)
    if selection == "Prediction And Save":
        PAGES[selection].write(state)
            



    

if __name__=='__main__':
    run()

