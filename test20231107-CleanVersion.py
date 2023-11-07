import pandas as pd
import csv


# Get Google CSE Credentials
file = open(r"C:\Users\perri\OneDrive\Documents\CODE\_Credentials\credentialsJPSearch-SearchEngineID.txt","r")
cse_id=file.read()
file.close()
file = open(r"C:\Users\perri\OneDrive\Documents\CODE\_Credentials\credJPSearch-CustomSearchAPIKey.txt","r")
api_key = file.read()
file.close()


# Hardcoded or input keywords added to company name for search term
keywords = " Canada Mining Home Homepage landing"
# keywords = input("Keywords to include with company names")

# Read company namelist into dataframe
df = pd.read_csv('20231031 1125  Canada Mining Company List 100 Only.csv', on_bad_lines='skip',names=["Search Term"])
df = df.astype(str)


for index,row in df.iterrows():
    df.at[index,'Search Term'] = df.at[index,'Search Term']+keywords
    
