"""
Real world example : Multi-threading for I/O bound tasks
Scenario: Web Scraping
In web scraping, we often need to fetch data from multiple web pages. This is an I/O bound task because the program spends a lot of time waiting for responses from the web servers. Using multi-threading can help us fetch data from multiple web pages concurrently, improving the overall efficiency of our web scraping tasks.

https://www.langchain.com/
https://www.mongodb.com/
https://www.bseindia.com/
"""

import threading
import requests
from bs4 import BeautifulSoup

urls= [
    'https://www.langchain.com/',
    'https://www.mongodb.com/',
    'https://www.bseindia.com/'
]

def fetch_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    print(f'Title of {url}: {soup.title.string}')
    
threads = []
for url in urls:
    thread = threading.Thread(target=fetch_data, args=(url,))
    threads.append(thread)
    thread.start()
    
for thread in threads:
    thread.join()
    
print('All data has been fetched.')