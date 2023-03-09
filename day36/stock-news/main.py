import requests
import os
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API = os.environ["STOCK_API_KEY"]
NEWS_API = os.environ["NEWS_API_KEY"]

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
TWILIO_SID = os.environ["TWILIO_ACCOUNT_SID"]
TWILIO_AUTH_TOKEN = os.environ["TWILIO_AUTH_TOKEN"]

stock_parameters = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API
}

#!################### Gets the stock price data and formats it ##############
stock_response = requests.get(url=STOCK_ENDPOINT, params=stock_parameters)
stock_response.raise_for_status()

data = stock_response.json()["Time Series (Daily)"]
# list comprehensions on Python dictionaries
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print(yesterday_closing_price)


two_days_ago_data = data_list[1]
two_days_ago_closing_price = two_days_ago_data["4. close"]
print(two_days_ago_closing_price)


#!#### positive difference between yesterday and two days ago ###############
difference = float(yesterday_closing_price) - float(two_days_ago_closing_price)
print(difference)
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"


#!#### percentage difference in price between closing price yesterday and closing price the day before yesterday.###########
diff_percent = round((difference / float(yesterday_closing_price)) * 100)
print(diff_percent)

#!################## If the stock price changes by 5% fetches news###############
if abs(diff_percent) > 2:
    news_parameters = {
    "qInTitle": COMPANY_NAME,
    "apiKey": NEWS_API
}   
    news_response = requests.get(url=NEWS_ENDPOINT, params=news_parameters)
    news_response.raise_for_status()
    news_data = news_response.json()
    article = news_data["articles"][0]["title"]
    link = news_data["articles"][0]["url"]

#!################# Formats and Sends text message ######################################
    stock_up_down = f"{STOCK_NAME}: {up_down}{diff_percent} "
    text = stock_up_down + " " + link
    print(text)
    
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    message = client.messages.create(
                    body=text,
                    from_='+18888233160',
                    to='+13155613980'
                )
    print(message.sid)

