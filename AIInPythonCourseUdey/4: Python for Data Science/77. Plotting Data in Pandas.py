# Reading CVS File

import pandas as pd

# reading file cvs
data = pd.read_csv("./balance.csv")

print(data.head())

# reading excel files
df = pd.read_excel("./excel_example.xls")
print(df.head())

# bar plot 
print(data["instutional_sector_name"].value_counts().plot(kind="bar"))