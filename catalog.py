import requests
import bs4


def load(url):
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    return soup


def find_product_urls(soup):
    product_element = soup.find('ul', class_="products")
    links = product_element.find_all('a')
    links = set([link["href"] for link in links])
    return links

url = "http://www.white2tea.com/tea-shop/product-category/raw-puer-tea/white2tea-raw-puer-tea/2015-white-2-tea-puer-teas/"
page = load(url)
print(find_product_urls(page))
