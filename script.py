# CannedBS
# cannedBS = bs4.BeautifulSoup(body, 'html.parser')
# body = response.text
# response = requests.get("url")
import requests
import bs4

tester = "https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup"


def scrape(url):
    response = requests.get(url)
    body = response.text
    soup = bs4.BeautifulSoup(body, 'html.parser')
    return soup

url = "http://numberoverzero.com/ctf"
page = scrape(url)
print(page.title.string)
