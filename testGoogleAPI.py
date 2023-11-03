import requests
import pandas as pd
from csv import writer
import csv
from datetime import datetime

file = open(r"C:\Users\jperrin\OneDrive\Documents\CODE\_Credentials\credentialsJPSearch-SearchEngineID.txt","r")
SEARCH_ENGINE_ID=file.read()
file.close()
file = open(r"C:\Users\jperrin\OneDrive\Documents\CODE\_Credentials\credJPSearch-CustomSearchAPIKey.txt","r")
API_KEY = file.read()
file.close()


df = pd.read_csv('20231031 1125  Canada Mining Company List 25 Only.csv', on_bad_lines='skip',names=["Search Term","Rank","Title","Description","Long Description","URL"])
df = df.astype(str)
keywords = "Canada Mining"
for index,row in df.iterrows():
    df.at[index,'Search Term'] = df.at[index,'Search Term']+' Canada Mine Industry'
# print(df)

# create output file
current_datetime = datetime.now().strftime("%Y-%m-%d %H-%M")
filename = current_datetime +" - outputGoogleAPI.csv"

with open(filename,'w',newline='') as f:
    csv_writer = writer(f)
    for index,row in df.iterrows():
        # the search query you want
        query = bytes(df.at[index,'Search Term'], 'utf-8').decode('utf-8', 'ignore')
        # using the first page
        page = 1
        # constructing the URL
        # doc: https://developers.google.com/custom-search/v1/using_rest
        # calculating start, (page=2) => (start=11), (page=3) => (start=21)
        start = (page - 1) * 10 + 1
        url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}"
        # make the API request
        data = requests.get(url).json()

        # get the result items
        search_items = data.get("items")

        # iterate over 10 results found
        for i, search_item in enumerate(search_items, start=1):
            try:
                long_description = search_item["pagemap"]["metatags"][0]["og:description"].encode('ascii','ignore')
            except KeyError:
                long_description = "N/A"
            # get the page title
            title = search_item.get("title").encode('ascii','ignore')
            # # page snippet
            # snippet = search_item.get("snippet")
            # # alternatively, you can get the HTML snippet (bolded keywords)
            # html_snippet = search_item.get("htmlSnippet")
            # # extract the page url
            url = search_item.get("link").strip()

            rank = i

            columns = [query,rank,url,title,long_description]
            print(columns)
            csv_writer.writerow(columns)
            
# df.to_excel('test_out.xlsx')
# filename.close()

# custom searchengineid b4735cf32d7d746ee
# custom search key AIzaSyBhQRTi72A68uWHh-CpnDqq6mOgyDTbI6U

# Search Engine Code
# <script async src="https://cse.google.com/cse.js?cx=b4735cf32d7d746ee">
# </script>
# <div class="gcse-search"></div>