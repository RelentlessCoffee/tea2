# CannedBS
# cannedBS = bs4.BeautifulSoup(body, 'html.parser')
# body = response.text
# response = requests.get("url")
import requests
import bs4
import json


def scrape(url):
    response = requests.get(url)
    body = response.text
    soup = bs4.BeautifulSoup(body, 'html.parser')
    form = soup.find("form", class_="variations_form cart")
    product_data = form['data-product_variations']
    product_data = json.loads(product_data)
    return product_data[1]["max_qty"]

url = "http://www.white2tea.com/tea-shop/2015-little-walk/"
print(scrape(url))
