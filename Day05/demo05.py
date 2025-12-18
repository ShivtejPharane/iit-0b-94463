
from langchain.chat_models import init_chat_model
import os
from dotenv import load_dotenv
import pandas as pd
import pandasql as ps
load_dotenv()
llm = init_chat_model(
    model = "llama-3.3-70b-versatile",
    model_provider = "openai",
    base_url = "https://api.groq.com/openai/v1",
    api_key = os.getenv("api_key")
)
conversation = [
    {"role" : "system","content":"You are healpful assistent."}
]
csv_file = input("Entre the path of csv file :")
df = pd.read_csv(csv_file)
print("Schema : ")
print(df.dtypes)

while True:
    user_input = input("Ask anythin about the csv : ")
    if user_input == "exit":
        break
    llm_msg = '''
    Table name : data
    table schmea : {df.dtypes}
    Qusetion :{user_input}
    instruction : write sql query to above question
    genrate ony sql query nothing else
    if you connot genrate show message question sedha puch re :
    '''
    result = llm.invoke(llm_msg)
    print(result.content)