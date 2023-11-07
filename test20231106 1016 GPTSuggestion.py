from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from csv import writer
import pandas as pd
from datetime import datetime
import time
import json


# Get Credentials
file = open(r"C:\Users\perri\OneDrive\Documents\CODE\_Credentials\credentialsJPSearch-SearchEngineID.txt","r")
cse_id=file.read()
file.close()
file = open(r"C:\Users\perri\OneDrive\Documents\CODE\_Credentials\credJPSearch-CustomSearchAPIKey.txt","r")
api_key = file.read()
file.close()

# Get Query Data
df = pd.read_csv('20231031 1125  Canada Mining Company List 100 Only.csv', on_bad_lines='skip',names=["Search Term","Rank","Title","Description","Long Description","URL"])
df = df.astype(str)
keywords = "Canada Mining"
for index,row in df.iterrows():
    df.at[index,'Search Term'] = df.at[index,'Search Term']+' Canada Mine Industry Homepage Home'
# print(df)

# Set up your Custom Search API client
# api_key = 'YOUR_API_KEY'
# cse_id = 'YOUR_CSE_ID'
service = build('customsearch', 'v1', developerKey=api_key)

# create output file
current_datetime = datetime.now().strftime("%Y-%m-%d %H-%M")
filename = current_datetime +" - outputGoogleAPI.csv"
# with open(filename,'w',newline='') as f:

# https://ankushkunwar7777.medium.com/get-data-from-large-nested-json-file-cf1146aa8c9e#:~:text=To%20extract%20data%20from%20a,from%20nested%20JSON.%22%22%22
# def item_generator(json_input, lookup_key):
#     if isinstance(json_input, dict):
#         for k, v in json_input.items():
#             if k == lookup_key:
#                 yield v
#             else:
#                 yield from item_generator(v, lookup_key)
#     elif isinstance(json_input, list):
#         for item in json_input:
#             yield from item_generator(item, lookup_key)

def write_results(filename, query, results):
    # data = results.json()
    # search_items = results.get("items")
    search_items = ['results', json.dumps('items')]
    print("got results!")
    print(results)
    with open(filename,'a',newline='') as f:
        csv_writer = writer(f)
        for i, search_item in enumerate(search_items, start=1):
        # for index,row in df.iterrows():
            print(search_item['title'])
            # print(results[index,'url'])
            # try:
            #     long_description = search_item["pagemap"]["metatags"][0]["og:description"].encode('ascii','ignore')
            # except KeyError:
            #     long_description = "N/A"
            # # get the page title
            # title = search_item.get("title").encode('ascii','ignore')
            # # # page snippet
            # # snippet = search_item.get("snippet")
            # # # alternatively, you can get the HTML snippet (bolded keywords)
            # # html_snippet = search_item.get("htmlSnippet")
            # # # extract the page url
            # url = search_item.get("link").encode('ascii','ignore')
            # rank = i
            # columns = [query,rank,url,title,long_description]
            # print(columns)
            csv_writer.writerow(search_item)




for index,row in df.iterrows():
    # the search query you want
    query = bytes(df.at[index,'Search Term'], 'utf-8').decode('utf-8', 'ignore')
    # using the first page
    # page = 1
    # start = (page - 1) * 10 + 1
    # url = f"https://www.googleapis.com/customsearch/v1?key={api_key}&cx={cse}&q={query}&start={start}"
    max_tries = 10
    try:
        # Perform a search using the API
        results = service.cse().list(q=query, cx=cse_id).execute()
    except HttpError as e:
        # Handle API-related errors
        print(f'API Error: {e}')
        for j in range(1, max_tries):
            if j == max_tries - 1:
                raise
            else:
                delay = 2 ** j
                time.sleep(delay)
                results = service.cse().list(q=query, cx=cse_id).execute()
    except Exception as e:
        # Handle other exceptions
        print(f'An error occurred: {e}')
        
    
    write_results(filename, query, results)