import decimal
import requests
import time
from bs4 import BeautifulSoup
while True:
    url = 'https://www.binance.com/ru/price/bitcoin'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    search_price = soup.find('div', class_='css-1bwgsh3').text[1:].replace(',', '')
    search_price = decimal.Decimal(search_price)
    print(f'Курс Bitcoin - {search_price}')