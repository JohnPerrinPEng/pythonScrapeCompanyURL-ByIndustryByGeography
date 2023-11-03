import configparser
import requests
import pandas as pd
import csv
# config = configparser.RawConfigParser()
# # config.read(filenames:'testAPIKey.txt’)
# config.read(filenames = 'testAPIKey.txt')
# print(config.sections())
# API_KEY = config.get('Google','googleapikey')
API_KEY = "AIzaSyBhQRTi72A68uWHh-CpnDqq6mOgyDTbI6U"
SEARCH_ENGINE_ID = "b4735cf32d7d746ee"

# gm = googlesearch.Client(key = apikey)

df = df.astype(str)
df = pd.read_csv('20231031 1125  Canada Mining Company List 25 Only.csv', on_bad_lines='skip',names=["Search Term","Response"])
keywords = "Canada Mining"
for index,row in df.iterrows():
    df.at[index,'Search Term'] = df.at[index,'Search Term']+' Canada Mine Industry'
print(df)

# the search query you want
query = "Lundin Canad Mining Industry"
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
        long_description = search_item["pagemap"]["metatags"][0]["og:description"]
    except KeyError:
        long_description = "N/A"
    # get the page title
    title = search_item.get("title")
    # page snippet
    snippet = search_item.get("snippet")
    # alternatively, you can get the HTML snippet (bolded keywords)
    html_snippet = search_item.get("htmlSnippet")
    # extract the page url
    link = search_item.get("link")
    # print the results
    print("="*10, f"Result #{i+start-1}", "="*10)
    print("Title:", title)
    print("Description:", snippet)
    print("Long description:", long_description)
    print("URL:", link, "\n")



# custom searchengineid b4735cf32d7d746ee
# custom search key AIzaSyBhQRTi72A68uWHh-CpnDqq6mOgyDTbI6U

# Search Engine Code
# <script async src="https://cse.google.com/cse.js?cx=b4735cf32d7d746ee">
# </script>
# <div class="gcse-search"></div>