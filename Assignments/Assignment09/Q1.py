from langchain.chat_models import init_chat_model
from langchain.agents import create_agent
from langchain.tools import tool
import pandas as pd
import pandasql as ps
from selenium import webdriver
from selenium.webdriver.common.by import By
import streamlit as st 
import time
@tool
def csv_query_tool(question: str) -> str:
    """
    Automatically generate SQL from user question using LLM
    and execute it on CSV using pandasql.
    """
    file_path = "E:\Internship\Git_hub_repo\iit-0b-94463\Assignments\Assignment09\emp_hdr.csv"

    df = pd.read_csv(file_path)
    schema = df.dtypes.to_string() 

    sql_prompt = f"""
You are an expert SQLite developer.

Table name: csv_df

Schema:
{schema}

Rules:
- Return ONLY SQL
- No explanation
- No markdown
- No semicolon

Question:
{question}
"""

    sql_response = llm.invoke(sql_prompt)
    sql_query = sql_response.content.strip() #Removing extra spaces/newlines

    try:
        result = ps.sqldf(sql_query, {"csv_df": df})
    except Exception as e:
        return f"SQL ERROR:\n{e}\n\nSQL:\n{sql_query}"

    return f"""
        Generated SQL:
        {sql_query}
        Result:
        {result}"""


@tool
def internship_tool(user_input):
    """
    Scrape Sunbeam website and answer user question
    based on scraped content.
    """
    url = "https://sunbeaminfo.in/internship"
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(3)

    internship_data = []
    rows = driver.find_elements(By.XPATH, '//div//table//tbody//tr')
    for row in rows:
        cols = row.find_elements(By.XPATH, './/td')
        if len(cols) >= 7:
            internship_data.append({
                "Batch": cols[1].text.strip(),
                "Batch_Duration": cols[2].text.strip(),
                "Start_Date": cols[3].text.strip(),
                "End_Date": cols[4].text.strip(),
                "Time": cols[5].text.strip(),
                "Fees_INR": cols[6].text.strip()
            })
    driver.quit()

    df = pd.DataFrame(internship_data)

    # LLM prompt to answer question based on DataFrame
    context = df.to_string(index=False)
    prompt = f"""
    You are an AI assistant.
    Answer the user's question strictly using the internship data below.
    Do not make assumptions outside the data.

    Internship Data:
    {context}

    Question:
    {user_input}

    Explain the answer in simple English.
    """

    response = llm.invoke(prompt)
    return response.content


llm = init_chat_model(
    model="google/gemma-3n-e4b",
    model_provider="openai",
    base_url="http://127.0.0.1:1234/v1",
    api_key="non-needed"
)

agent = create_agent(
    model=llm,
    tools=[csv_query_tool, internship_tool],
    system_prompt="""
    You are an intelligent assistant.
    - Use CSV tool for CSV questions
    - Use Web tool for Sunbeam questions
    - Answer briefly and clearly
    """
)


with st.sidebar:
    option = st.selectbox("Select Mode", ["CSV-QNA", "Scraping"])

st.title("Chat Bot")
st.write("Best for CSV-QNA and Data Scraping")
if option == "CSV_QNA":
    path = st.chat_input("paste the file path")
conversation = []

user_input = st.chat_input("Enter your question")

if user_input:
    conversation.append({"role": "user", "content": user_input})
    result = agent.invoke({"messages": conversation})
    llm_output = result["messages"][-1]
    st.write("AI:", llm_output.content)
