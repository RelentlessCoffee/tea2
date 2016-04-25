import requests
import bs4


def load(url):
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    return soup


def find_product_urls(soup):
