import streamlit as st
from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

@st.cache_data
def write(state_df):
    st.header("Loading Data Info ...")
    with st.spinner("Loading Data Info...."):
        if state_df is not None:
            pr=ProfileReport(state_df,explorative=True, minimal=True)
            st_profile_report(pr)
        else:
            st.error("Please Upload Dataset First 🚨")