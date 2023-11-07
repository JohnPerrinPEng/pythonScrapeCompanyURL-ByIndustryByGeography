import httpx

url = "https://www.google.com/search?q=python+tutorial&gl=us"
headers = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.2816.203 Safari/537.36"}

async def fetch_data():
    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)
        response.raise_for_status()
        print(response.content)
        return response.text

response_text = httpx.run(fetch_data)
print(response_text)