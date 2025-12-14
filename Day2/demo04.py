import pandas as pd 
import streamlit as st

st.title("CSV EXplorer")

datafile=st.file_uploader("Upload a CSV file",type=["csv"])
if datafile:
    df = pd.read_csv(datafile)
    st.dataframe(df)
    