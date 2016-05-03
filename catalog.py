import requests
import bs4


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


def find_product_urls(soups):
    product_links = []
    for soup in soups:
        product_element = soup.find('ul', class_="products")
        links = product_element.find_all('a')
        links = set([link["href"] for link in links])
        for link in links:
            if link.startswith("http"):
                product_links.append(link)
    return product_links


if __name__ == "__main__":
    url = "http://www.white2tea.com/tea-shop/product-category/raw-puer-tea/white2tea-raw-puer-tea/2015-white-2-tea-puer-teas/"
    print(find_product_urls(load_pages(url)))
