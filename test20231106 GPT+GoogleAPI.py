import requests
import pandas as pd
from csv import writer
import csv
from datetime import datetime
import backoff
import time
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# @backoff.on_exception(backoff.expo, requests.exceptions.RequestException, max_tries=10)
# def make_request(url):
#     print("try")
#     response = requests.get(url)
#     response.raise_for_status()
#     return response.json()

# def make_request_with_backoff(url, max_tries=10):
#     for i in range(max_tries):
#         print("try loop "+ str(i))
#         response = requests.get(url)
#         if response.get("items") == "None":
#             if i == max_tries - 1:
#                 raise
#             else:
#                 delay = 2 ** i
#                 time.sleep(delay)
#         else:
#             response.raise_for_status()
#             return response.json()
#         try:
#             print("try loop "+ str(i))
#             response = requests.get(url)
#             # print(response)
#             if response == "None":
#                 print("Response = None")
#             response.raise_for_status()
#             return response.json()
#         except requests.exceptions.RequestException:
#             print("exception loop " + str(i))
#             if i == max_tries - 1:
#                 raise
#             else:
#                 delay = 2 ** i
#                 time.sleep(delay)

# should work but doesn't
# def make_request_with_backoff(url, max_tries=10):
#     for i in range(max_tries):
#         try:
#             print("try loop"+ str(i))
#             response = requests.get(url)
#             # print(response)
#             response.raise_for_status()
#             return response.json()
#         except requests.exceptions.RequestException:
#             print("exception loop" + str(i))
#             if i == max_tries - 1:
#                 raise
#             else:
#                 delay = 2 ** i
#                 time.sleep(delay)\

def make_request_with_backoff(query,api_key,cse_id,max_tries=10):
    service = build('customsearch', 'v1', developerKey=api_key)
    try:
        #Perform a search using the API
        results = service.cse().list(q=query,cx=cse_id).execute()
        #Process the search results
        print('we got a live one one')
        print(results)
        return results.json()
            
    except HttpError as e:
        print(f'API Error: {e}')
    except Exception as e:
        print(f'An error occured: {e}')

file = open(r"C:\Users\perri\OneDrive\Documents\CODE\_Credentials\credentialsJPSearch-SearchEngineID.txt","r")
SEARCH_ENGINE_ID=file.read()
file.close()
file = open(r"C:\Users\perri\OneDrive\Documents\CODE\_Credentials\credJPSearch-CustomSearchAPIKey.txt","r")
API_KEY = file.read()
file.close()


df = pd.read_csv('20231031 1125  Canada Mining+ Company List.csv', on_bad_lines='skip',names=["Search Term","Rank","Title","Description","Long Description","URL"])
df = df.astype(str)
keywords = "Canada Mining"
for index,row in df.iterrows():
    df.at[index,'Search Term'] = df.at[index,'Search Term']+' Canada Mine Industry Homepage Home'
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
        data = make_request_with_backoff(url,API_KEY,SEARCH_ENGINE_ID,3)
        # data = requests.get(url).json()

        # service = __build_class__('customsearch', 'v1', developerKey=API_KEY)
        
        



        # get the result items
        # search_items = data.get("items")

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
            url = search_item.get("link").encode('ascii','ignore')

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