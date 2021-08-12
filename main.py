from flask import Flask, render_template, jsonify
from crawl_stock import get_today_price, get_daily_stock_prices
from crawl_news import get_news_list
from crawl_bitcoin import get_bitcoin_price
from crawl_us_stock import get_us_stock_price
from crawl_weather import get_weather_info
import requests
from flask_cors import CORS


app = Flask(__name__,
            static_url_path='',
            static_folder='static',
            template_folder='templates'
            )
CORS(app)


@app.route('/')
def dashboard():
    hyundai_price = get_today_price('005380')
    company1_stock = {'title': "현대자동차", "today_price": hyundai_price}
    company1_news_list = get_news_list("현대자동차")

    shinsegae_price = get_today_price('004170')
    company2_stock = {'title': "신세계", "today_price": shinsegae_price}
    company2_news_list = get_news_list("신세계")

    us_stock_price = {'title': "tesla", 'today_price': get_us_stock_price('tesla')}
    bitcoin_price = get_bitcoin_price()

    weather_info = get_weather_info()

    return render_template('index.html',
                           company1_stock=company1_stock,
                           company1_news_list=company1_news_list,
                           company2_stock=company2_stock,
                           company2_news_list=company2_news_list,
                           us_stock_price=us_stock_price,
                           bitcoin_price=bitcoin_price,
                           weather_info=weather_info
                           )


@app.route('/weather_forecast')
def get_weather_forecast_info():
    result = requests.get('https://api.openweathermap.org/data/2.5/onecall?lat=37.413294&lon=126.734086&exclude=current,minutely,hourly,alerts&appid=3c9021aa10b48b8251d6555460a9f989&units=metric')
    json_result = result.json()
    print(type(json_result))
    print(type(json_result['daily']))
    return jsonify(json_result['daily'])


@app.route('/daily_prices')
def get_daily_prices():
    daily_price_list = get_daily_stock_prices()
    print(type(daily_price_list))
    return jsonify(daily_price_list)


if __name__ == '__main__':
    app.run(debug=True)
