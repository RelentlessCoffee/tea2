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
    quantities = []
    # for option in product_data:
    #    quantity = option["max_qty"]
    #    quantities.append(quantity)
    quantities = [option["max_qty"] for option in product_data]
    options = soup.find_all("option")[1:]
    options = [option["value"] for option in options]
    return list(zip(options, quantities))
url = "http://www.white2tea.com/tea-shop/2015-little-walk/"
print(scrape(url))
