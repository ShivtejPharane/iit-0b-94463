import pandas as pd
import pandasql as ps

df = pd.read_csv("emp_hdr.csv")
query = "select count(*) from df"
result = ps.sqldf(query,globals())
print(result)