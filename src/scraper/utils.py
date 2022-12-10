import requests
from bs4 import BeautifulSoup

def get_link_book_data(url):
    headers = {
        'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
        'Accept-Language': '*'
    }
    try:
        res = requests.get(url, headers=headers, timeout=1)
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

    except (requests.exceptions.ConnectionError, requests.exceptions.ReadTimeout):
        # tratamento do erro
        return False