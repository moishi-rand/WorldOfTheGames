import datetime
import requests
from forex_python.converter import CurrencyRates
from Utills.utility import validate_input_number

difficult_level = 0
# Where USD is the base currency you want to use
url = 'https://v6.exchangerate-api.com/v6/188507c8b99fdc52b0a5bdb1/latest/USD'


#The library is not updated by the current date, it has an old currency exchange rate
def currency_exchange_rate_from_libraryi():
    c = CurrencyRates()
    dt = datetime.datetime(2021, 5, 30)
    return c.get_rate('USD', 'ILS', dt)

#API for get current currency exchange rate
def currency_exchange_rate_from_api():
    # Making our request
    response = requests.get(url)
    data = response.json()
    # Your JSON object
    # return f'{data["conversion_rates"]["ILS"]}'
    return data["conversion_rates"]["ILS"]

#Get interval with mix the currency exchange rate and difficulty
def get_money_interval(difficulty):
    currency_rate_value = currency_exchange_rate_from_api()
    min_interval = currency_rate_value - (5 - difficulty)
    max_interval = currency_rate_value + (5 - difficulty)
    my_interval = (min_interval, max_interval)
    return my_interval

#Get input of number from user
def get_guess_from_user():
    print(f"Please guess the currency exchange rate: ")
    input_number = validate_input_number()
    return input_number

#Check if input user in the interval
def check_results():
    guess_user = get_guess_from_user()
    interval = get_money_interval(difficult_level)
    return guess_user >= interval[0] and guess_user <= interval[1]

#Start play the game, return if user win or not
def play(difficulty):
    difficult_level = difficulty
    return check_results()
