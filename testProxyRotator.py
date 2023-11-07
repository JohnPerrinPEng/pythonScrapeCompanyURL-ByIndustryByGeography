import requests
import pandas as pd
import csv

class ProxyRotator:
    def __init__(self, proxy_file, user_agent):
        self.proxy_list = self.load_proxy_list(proxy_file)
        self.current_proxy = None
        self.user_agent = user_agent
    def load_proxy_list(self, proxy_file):
        with open(proxy_file, 'r') as file:
            proxies = file.read().splitlines()
        return proxies
    def get_next_proxy(self):
        if not self.current_proxy:
            self.current_proxy = self.proxy_list[0]
        else:
            current_index = self.proxy_list.index(self.current_proxy)
            next_index = (current_index + 1) % len(self.proxy_list)
            self.current_proxy = self.proxy_list[next_index]
        return self.current_proxy
    def make_request(self, url, query):
        proxy = self.get_next_proxy()
        headers = {
            'User-Agent': self.user_agent
        }
        proxies = {
            'http': f'http://{proxy}',
            'https': f'http://{proxy}'
        }
        try:
            params = {
                'q': query
            }
            response = requests.get(url, params=params, headers=headers, proxies=proxies)
            response.raise_for_status()
            return response.text
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
# Example usage

proxy_file = 'proxies_list.txt'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
rotator = ProxyRotator(proxy_file, user_agent)
# queries = ['Python Proxy Rotator', 'Web Scraping', 'Data Mining']

df = df.astype(str)
df = pd.read_csv('20231031 1125  Canada Mining Company List 25 Only.csv', on_bad_lines='skip',names=["Search Term","Response"])
keywords = "Canada Mining"
for index,row in df.iterrows():
    df.at[index,'Search Term'] = df.at[index,'Search Term']+' Canada Mine Industry'
print(df)

# df.to_csv('testoutput.csv', sep=',', index=True)

url = 'https://www.google.com/search'

for index,row in df.iterrows():
# for query in queries:
    response = rotator.make_request(url, df.at[index,'Search Term'])
    df.at[index,"Response"] = response
    print(f"Results for query '{df.at[index,'Search Term']}':")
    print(response)
    print("------------------")

print(df)