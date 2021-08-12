from bs4 import BeautifulSoup
import requests


def get_us_stock_price(company):
    html = requests.get('https://www.google.com/search?q='+company+'stock', headers={'User-Agent': 'Mozilla/5.0'})

    html = BeautifulSoup(html.text, 'html.parser')

    tags = html.select("div.BNeawe.iBp4i.AP7Wnd")
    for tag in tags:
        print(tag.text)

    return tags[0].text.split(' ')[0]