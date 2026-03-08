'''import pandas as pd

#Importing CSV File in pythob
df=pd.read_csv(r'C:\Users\Dell\Downloads\e0e00a350a16fd19b0c9b05f3bb8536b-4b3ac34622b92fd995e23da6a88c50e9554355ae\e0e00a350a16fd19b0c9b05f3bb8536b-4b3ac34622b92fd995e23da6a88c50e9554355ae\sales_data.csv')

#LOADING 5 COLUMNS DATA WITH HEAD() BY DEFAULT GIVES ONLY 5
print(df.head())

#GETTING ALL COLUMNS NAME 
print(df.columns)

#Knowing how MANY COLUMNS ARE NULL AOR MISSING VALUES ARE THERE
print(df.isnull().sum())
print(df.info())'''

import pandas as pd

# Load dataset
df=pd.read_csv(r'C:\Users\Dell\OneDrive\Desktop\python\Visual Studio Code\sales_data.csv')

# Convert columns to numeric
df["Quantity Ordered"] = pd.to_numeric(df["Quantity Ordered"], errors="coerce")
df["Price Each"] = pd.to_numeric(df["Price Each"], errors="coerce")

# Create Revenue column
df["Revenue"] = df["Quantity Ordered"] * df["Price Each"]

# Display first 5 rows
print(df.head())
#IF THERE IS NO NULL VALUE WE MOVE TO DIRECT FOR MAKING INSIGHTS

