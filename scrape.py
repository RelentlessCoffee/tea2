from catalog import find_year_urls, find_product_urls
from product import load_single_page, find_quantities, find_name


category_url = "http://www.white2tea.com/tea-shop/product-category/white2tea-raw-puer-tea/"
year_urls = find_year_urls(category_url)
for year_url in year_urls:
    product_urls = find_product_urls(year_url)
    for product_url in product_urls:
        print(product_url)
