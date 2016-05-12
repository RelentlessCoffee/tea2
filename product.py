import requests
import bs4
import json


class NoMaxQuantity(Exception):
    pass


def load_single_page(url):
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    return soup


def _find_quantities_from_form(soup):
    form = soup.find("form", class_="variations_form cart")
    product_data = form['data-product_variations']
    product_data = json.loads(product_data)
    quantities = [option["max_qty"] for option in product_data]
    options = soup.find_all("option")[1:]
    options = [option["value"] for option in options]
    return list(zip(options, quantities))


def _find_quantities_from_input(soup):
    product_data = soup.find("input", class_="input-text qty text")
    quantity = product_data['max']
    if quantity == "":
        raise NoMaxQuantity("no max quantity")
    return quantity


def find_quantities(soup):
    try:
        return _find_quantities_from_form(soup)
    except TypeError:
        return _find_quantities_from_input(soup)


def find_name(soup):
    title = soup.find("h1")
    return title.string
