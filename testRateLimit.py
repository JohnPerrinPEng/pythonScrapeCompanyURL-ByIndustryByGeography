# https://akshayranganath.github.io/Rate-Limiting-With-Python/

from ratelimiter import RateLimiter
import asyncio
import requests

def access_rate_limited_api(count):
    resp = requests.get('http://192.168.1.2:8000/knockknock')
    print(f"{count}.{resp.text}")    

for i in range(60):
    access_rate_limited_api(i)

@RateLimiter(max_calls=10, period=1)
def do_something():
    pass