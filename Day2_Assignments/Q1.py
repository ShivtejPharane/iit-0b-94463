import pandasql as ps
import streamlit as st
import pandas as pd

st.title("CSV Uploader!!")

datafile= st.file_uploader("Upload the Csv File",type =["csv"])
if datafile:
    df = pd.read_csv(datafile)
    st.dataframe(df)
query = "select job, SUM(sal) total from data GROUP BY job"
result = ps.sqldf(query,{"data":df})
st.write(result)