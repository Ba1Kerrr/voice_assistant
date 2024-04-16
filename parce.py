import requests
from bs4 import BeautifulSoup
while 1:
    url_bit = 'https://www.binance.com/ru/price/bitcoin'
    page_bit = requests.get(url_bit)
    soup_bit = BeautifulSoup(page_bit.text, "html.parser")
    search_price_bit = soup_bit.find('div', class_='css-1bwgsh3').text[1:].replace(',', '')
    last_bit = float(search_price_bit)