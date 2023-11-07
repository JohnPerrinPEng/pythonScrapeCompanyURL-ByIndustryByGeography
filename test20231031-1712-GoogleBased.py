import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd
from googlesearch import search
import time

url = "https://www.google.ca/search"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"
}

# companies = []
# with open("x.csv","r") as file:
#     reader = csv.reader(file)
#     for row in reader:x``
#         # print(row)
#         companies.append(row)
# file.close()

# companies = pd.read_csv('x.csv')
# data = {'Company': companies}
# df['Company'] = ''
df = df.astype(str)
df = pd.read_csv('20231031 1125  Canada Mining+ Company List.csv', on_bad_lines='skip',names=["Company","Site URL","Site Map"])

print(df)

# results = ['Company','URL','Site.xml']
# for company in companies:
#     # print("Company coming up next!")
#     # print(company[0])
#     results.append([company,getURL(company[0] ,"Canada Mining")])

for index,row in df.iterrows():
    df.at[index,'Site URL'] = getURL(row['Company'],'Canada Mining')
    df.at[index,"Site Map"] = df.at[index,'Site URL'] + "sitemap.xml"
    # sitexml = result[1] + "sitemap.xml"
    # results[index][2]=sitexml

df.to_csv('testoutput.csv', sep=',', index=True)
# print("Results coming up next!")
# print(results)

# df['URL'] = ''

# for index, row in df.iterrows():
#     df.at[index, 'URL'] = getURL(row['Compan'], row['State'])
#     time.sleep(2)

# for company in reader:
#     open("results.csv",'w',)

def getURL(companyName, State):
    try:
        term = ' '.join([companyName, State])
        for url in search(term, num_results=1):
            return url
    except:
        return ''