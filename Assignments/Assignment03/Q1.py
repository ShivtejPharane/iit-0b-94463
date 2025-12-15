import pandas as pd 
import streamlit as st
import pandasql as ps
st.title("CSV EXplorer")

file_path = "emp_hdr.csv"
datafile=st.file_uploader("Upload a CSV file",type=["csv"])
if datafile:
    df = pd.read_csv(datafile)
    st.dataframe(df)
    query = "select job, SUM(sal) total from data GROUP BY job"
    result = ps.sqldf(query,{"data":df})
    st.write(result)


    