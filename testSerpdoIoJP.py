# https://serpdog.io/blog/scrape-google-search-results-with-python/
import httpx
import asyncio
from bs4 import BeautifulSoup
import json
# headers = []
URL = "https://www.google.com/search?q=Lundin+Canada+Mining&gl=us"
async def get_organic_data():
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4703.0 Safari/537.36"
    }
    async with httpx.AsyncClient() as client:
        response = await client.get(URL, headers=headers)

async with httpx.AsyncClient() as client:
    print("S'up Dawg")
    response = await client.get(URL, headers=headers)
    soup = BeautifulSoup(response.content, "lxml")
    organic_results = []
    i = 0
    for el in soup.select("div.g"):
        print("We here")
        organic_results.append({
            "title": el.select_one("h3").text,
            "link": el.find("a").get("href"),
            "rank": i+1
        })
        i+=1
        
    print(json.dumps(organic_results, indent=2))

await get_organic_data()

