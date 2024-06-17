import requests
from bs4 import BeautifulSoup
from datetime import datetime

def Bit():
    while True:
        url_bit = 'https://www.binance.com/ru/price/bitcoin'
        page_bit = requests.get(url_bit)
        soup_bit = BeautifulSoup(page_bit.text, "html.parser")
        search_price_bit = soup_bit.find('div', class_='css-1bwgsh3').text
        return search_price_bit
def Eth():
    while True:
        url_eth = 'https://www.binance.com/ru/price/ethereum'
        page_eth = requests.get(url_eth)
        soup_eth = BeautifulSoup(page_eth.text, "html.parser")
        search_price_eth = soup_eth.find('div', class_='css-dbxihu').text
        return search_price_eth
def Usd():
    while True:
        url_usd = 'https://ru.investing.com/currencies/'
        page_usd = requests.get(url_usd)
        soup_usd = BeautifulSoup(page_usd.text,"html.parser")
        search_price_usd = soup_usd.find('td', class_='pid-1-last').text
        return search_price_usd
def Usd():
    while True:
        url_usd = 'https://ru.investing.com/currencies/'
        page_usd = requests.get(url_usd)
        soup_usd = BeautifulSoup(page_usd.text,"html.parser")
        search_price_usd = soup_usd.find('td', class_='pid-1-last').text
        return 'EUR costs ' + search_price_usd + ' $'
print(Usd())