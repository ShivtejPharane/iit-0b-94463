import pandas as pd 
import pandasql as ps 

file_path = "emp_hdr.csv"
df = pd.read_csv(file_path)
print("dataframe column types : ")
print(df.dtypes)
print("\nEmp Data : ")
print(df)
query = "select job, SUM(sal) total from data GROUP BY job"
result = ps.sqldf(query,{"data":df})
print(result)