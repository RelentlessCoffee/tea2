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
    product_links = []
    for link in links:
        if link.startswith("http"):
            product_links.append(link)
    return product_links


if __name__ == "__main__":
    url = "http://www.white2tea.com/tea-shop/product-category/raw-puer-tea/white2tea-raw-puer-tea/2015-white-2-tea-puer-teas/"
    print(find_product_urls(load(url)))
