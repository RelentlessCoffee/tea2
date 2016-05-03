import requests
import bs4
import json


def load_single_page(url):
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    return soup


def find_quantities(soup):
    form = soup.find("form", class_="variations_form cart")
    product_data = form['data-product_variations']
    product_data = json.loads(product_data)
    quantities = [option["max_qty"] for option in product_data]
    options = soup.find_all("option")[1:]
    options = [option["value"] for option in options]
    return list(zip(options, quantities))


def find_name(soup):
    title = soup.find("h1")
    return title.string


if __name__ == "__main__":
    url = "http://www.white2tea.com/tea-shop/big-leaf-bamboo-sheng-puer/"
    page = load_single_page(url)
    print(find_quantities(page))
    print(find_name(page))
