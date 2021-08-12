from bs4 import BeautifulSoup
import requests


def get_weather_info():
    html = requests.get('https://search.naver.com/search.naver?query=서울날씨', headers={'User-Agent': 'Mozilla/5.0'})

    soup = BeautifulSoup(html.text, 'html.parser')
    print(soup)
    data1 = soup.find('div', {'class': 'weather_box'})

    weather = data1.find('p', {'class': 'cast_txt'}).text

    temp = data1.find('span', {'class': 'todaytemp'}).text

    data2 = data1.findAll('dd')
    dust = data2[0].find('span', {'class': 'num'}).text
    ultra_dust = data2[1].find('span', {'class': 'num'}).text
    ozone = data2[2].find('span', {'class': 'num'}).text

    return {'weather': weather, 'temp': temp, "dust": dust, "ultra_dust": ultra_dust}
