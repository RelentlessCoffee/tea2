import requests
import bs4
YEAR_URL_PREFIX = "http://www.white2tea.com/tea-shop/product-category"


def load_pages(url):
    generic_url = url + "page/{}"
    soups = []
    page_number = 0
    while True:
        page_number += 1
        response = requests.get(generic_url.format(page_number))
        if response.status_code == 200:
            soup = bs4.BeautifulSoup(response.text, 'html.parser')
            soups.append(soup)
        else:
            break
    return soups


def find_year_urls(category_url):
    soups = load_pages(category_url)
    year_urls = []
    for soup in soups:
        category_element = soup.find('ul', class_="products")
        links = category_element.find_all('a')
        links = set([link["href"] for link in links])
        for link in links:
            if link.startswith(YEAR_URL_PREFIX):
                year_urls.append(link)
    return year_urls


def find_product_urls(year_url):
    soups = load_pages(year_url)
    product_urls = []
    for soup in soups:
        product_element = soup.find('ul', class_="products")
        links = product_element.find_all('a')
        links = set([link["href"] for link in links])
        for link in links:
            if link.startswith("http"):
                product_urls.append(link)
    return product_urls
