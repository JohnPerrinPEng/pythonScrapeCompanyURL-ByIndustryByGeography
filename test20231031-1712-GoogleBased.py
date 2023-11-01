import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.google.ca/search"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"
}

with open("20231031 1125  Canada Mining Company List 100 Only.csv","r") as file:
    reader = csv.reader(file)
    
print(reader)