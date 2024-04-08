import decimal
import requests
from bs4 import BeautifulSoup

url = 'https://coinmarketcap.com/currencies/bitcoin/'
page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")
search_price = soup.find('span', class_='sc-f70bb44c-0 jxpCgO base-text').text[1:].replace(',','')
search_price = decimal.Decimal(search_price)