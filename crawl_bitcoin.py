from bs4 import BeautifulSoup
import requests


def get_bitcoin_price():
    html = requests.get('https://www.google.com/search?newwindow=1&rlz=1C1CHZN_koKR935KR935&sxsrf=ALeKk03ZW01r2SN_lsEbNM5yB-xE4sRWLw%3A1615614504567&ei=KFJMYJybIpeIr7wP5Zia6A4&q=bitcoin+%EC%8B%9C%EC%84%B8&oq=bitc&gs_lcp=Cgdnd3Mtd2l6EAMYADIJCAAQQxBGEIICMgUIABCxAzIKCAAQsQMQgwEQQzIHCAAQsQMQQzIECAAQQzIFCAAQsQMyBAgAEEMyBAgAEEMyBAgAEEMyBAgAEEM6BQgAELADOgQIIxAnOgIIADoICAAQsQMQgwFQsfcCWMD7AmDNkgNoA3AAeACAAWKIAdADkgEBNZgBAKABAaoBB2d3cy13aXrIAQHAAQE&sclient=gws-wiz', headers={'User-Agent': 'Mozilla/5.0'})

    html = BeautifulSoup(html.text, 'html.parser')
    tags = html.select("div.BNeawe.iBp4i.AP7Wnd")
    for tag in tags:
        print(tag.text)

    return tags[0].text.split(' ')[0]
