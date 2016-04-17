# CannedBS
# cannedBS = bs4.BeautifulSoup(body, 'html.parser')
# body = response.text
# response = requests.get("url")
import requests
import bs4


def scrape(url):
    response = requests.get(url)
    body = response.text
    soup = bs4.BeautifulSoup(body, 'html.parser')
    return soup

url = "http://www.white2tea.com/tea-shop/2016-fade-raw-puer-huangpian-brick/"
page = scrape(url)

print(page.title.string)
