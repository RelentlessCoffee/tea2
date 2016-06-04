from catalog import find_year_urls, find_product_urls
from product import load_single_page, find_options, find_name, NoMaxQuantity
from storage import save

category_urls = [
    "http://www.white2tea.com/tea-shop/product-category/raw-puer-tea/misc-raw-puer-tea/",
    "http://www.white2tea.com/tea-shop/product-category/white2tea-raw-puer-tea/"
]
year_urls = [
    # Teas - Not under any category
    "http://www.white2tea.com/tea-shop/product-category/view-all-ripe-puer-teas/",
    "http://www.white2tea.com/tea-shop/product-category/black-tea/",
    "http://www.white2tea.com/tea-shop/product-category/oolong-tea/",
    "http://www.white2tea.com/tea-shop/product-category/tea-sample-sets/",
    "http://www.white2tea.com/tea-shop/product-category/white-tea/",

    # Accessories!
    "http://www.white2tea.com/tea-shop/product-category/teaware-and-tea-accessories/teacups-teaware-and-tea-accessories/",
    "http://www.white2tea.com/tea-shop/product-category/teaware-and-tea-accessories/teapots/"

]
product_urls = []

output_filename = "output"
data = {"products": []}

for category_url in category_urls:
    year_urls.extend(find_year_urls(category_url))

for year_url in year_urls:
    product_urls.extend(find_product_urls(year_url))

print("done finding product urls")

for product_url in product_urls:
    try:
        page = load_single_page(product_url)
        name = find_name(page)
        options = find_options(page)
        single_product = {
            "name": name,
            "options": options
        }
        data["products"].append(single_product)
    except NoMaxQuantity as exception:
        print(str(exception).upper())
save(data, output_filename)
