import requests
from bs4 import BeautifulSoup

import retrying

import random

def retry_if_result_none_random(result):
    r = random.random() < 0.6
    return result is None and r 

@retrying.retry(retry_on_result=retry_if_result_none_random)
def get_link_book_data(url, timeout=5):

    headers = {
        'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
        'Accept-Language': '*'
    }
    try:
        res = requests.get(url, headers=headers, timeout=5)
        soup = BeautifulSoup(res.text, "lxml")
        
        # book name
        name = soup.select_one(selector="#productTitle").getText()
        name = name.strip()

        # book price
        price = float(soup.select_one(selector="#price").getText()[3:].replace(',', '.'))

        # book image
        image_url = soup.select_one(selector="#imgBlkFront").get("src")

        data = {
            "name": name,
            "price": price,
            "image_url": image_url,
        }
        return data

    except (requests.exceptions.ConnectionError, requests.exceptions.ReadTimeout) as errors:
        pass