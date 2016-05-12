from catalog import find_year_urls, find_product_urls
from product import load_single_page, find_quantities, find_name, NoMaxQuantity


category_url = "http://www.white2tea.com/tea-shop/product-category/white2tea-raw-puer-tea/"
year_urls = find_year_urls(category_url)

for year_url in year_urls:
    product_urls = find_product_urls(year_url)

    for product_url in product_urls:
        try:
            page = load_single_page(product_url)
            print(find_name(page))
            print(find_quantities(page))
        except NoMaxQuantity as exception:
            print(exception)
