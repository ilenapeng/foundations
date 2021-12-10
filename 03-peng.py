# Ilena Peng
# Homework 3, Starting with APIs
# November 7, 2021

import requests

# Using the Pokemon API:
# What is the URL to the documentation?
# https://pokeapi.co/docs/v2

# What pokemon has the ID of 55?
# Goldluck: https://pokeapi.co/api/v2/pokemon/55
response = requests.get("https://pokeapi.co/api/v2/pokemon/55")
data_goldluck = response.json()
# data_goldluck['name']

# How tall is that pokemon?
#print(data_goldluck['height'])
goldluck_height = data_goldluck['height']
print(f'Goldluck is {goldluck_height} decimeters tall')

# How many versions of Pokemon games have been released?
response = requests.get("https://pokeapi.co/api/v2/version/")
data_version = response.json()

version_count = len(data_version['results'])
print(f'{version_count} versions of the game have been released')

# THIS IS WRONG. THE CORRECT ANSWER IS 34 it's in the first entry: 'count' in the link pokeapi.co/api/v2/version. or you can add /?limit=100 to get the API to give you all of them

# Print out the name of every electric-type pokemon.
# Found that electric was type 13 by looking here: https://pokeapi.co/api/v2/type/
response = requests.get("https://pokeapi.co/api/v2/type/13/")
data_electric = response.json()

for pokemon in range(len(data_electric['pokemon'])):
    print(data_electric['pokemon'][pokemon]['pokemon']['name'])

# What are electric-type Pokemon called in the Korean version of the game?
korean = data_electric['names'][1]['name']
print(f'Electric-type Pokemon are called {korean} in the Korean version of the game')
# Electric-type Pokemon are called 전기 in the Korean version of the game

# THE BETTER WAY OF DOING THIS IS TO USE A FOR LOOP
for language in data_electric['names']:
    lang_code = language['language']['name']
    if lang_code == 'ko':
        print(language['name'])

# Who has a higher speed stat, Eevee or Pikachu?
response = requests.get("https://pokeapi.co/api/v2/pokemon/eevee")
data_eevee = response.json()
#print(data_eevee['stats'][5])
response = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")
data_pikachu = response.json()
#print(data_pikachu['stats'][5])

speed_eevee = data_eevee['stats'][5]['base_stat']
speed_pikachu = data_pikachu['stats'][5]['base_stat']

if speed_pikachu > speed_eevee:
    print(f"Pikachu's speed ({speed_pikachu}) is faster than Eevee's ({speed_eevee}).")
else:
    print(f"Eevee's speed ({speed_eevee}) is faster than Pikachu's ({speed_pikachu}).")

# PART TWO: Weather API

# Register for an account at weatherapi.com (Links to an external site.). 
# What is the URL to the documentation?
# https://www.weatherapi.com/docs/

# Make a request for the current weather where you are born, or somewhere you've lived.
response = requests.get("http://api.weatherapi.com/v1/current.json?key=1a6fa10583f54fcdbfa115430210411&q=95014&aqi=no")
cupertino_weather = response.json()
# http://api.weatherapi.com/v1/current.json?key=1a6fa10583f54fcdbfa115430210411&q=95014&aqi=no

# Print out the country this location is in.
print(cupertino_weather['location']['country'])

# Print out the difference between the current temperature and how warm it feels. Use "It feels ___ degrees colder" or "It feels ___ degrees warmer," not negative numbers.
current_temp = cupertino_weather['current']['temp_f']
feels_like = cupertino_weather['current']['feelslike_f']

if feels_like > current_temp:
    print(f"It feels {feels_like - current_temp} warmer")
else:
    print(f"It feels {current_temp - feels_like} colder")

# What's the current temperature at Heathrow International Airport? Use the airport's IATA code to search.
response = requests.get("http://api.weatherapi.com/v1/current.json?key=1a6fa10583f54fcdbfa115430210411&q=LHR&aqi=no")
lhr_weather = response.json()

print(lhr_weather['current']['temp_f'])

# What URL would I use to request a 3-day forecast at Heathrow?
response = requests.get("http://api.weatherapi.com/v1/forecast.json?key=1a6fa10583f54fcdbfa115430210411&q=LHR&days=3&aqi=no&alerts=no")
lhr_weather_forecast = response.json()

# Print the date of each of the 3 days you're getting a forecast for.
for day in range(len(lhr_weather_forecast['forecast']['forecastday'])):
    print(lhr_weather_forecast['forecast']['forecastday'][day]['date'])

# NOTING FOR MYSELF: range len here returns 3 for 3 days

# Print the maximum temperature of each of the days.
for day in range(len(lhr_weather_forecast['forecast']['forecastday'])):
    print(lhr_weather_forecast['forecast']['forecastday'][day]['day']['maxtemp_f'])

# Print the day with the highest maximum temperature.
max_temp = 0
for day in range(len(lhr_weather_forecast['forecast']['forecastday'])) :
  if lhr_weather_forecast['forecast']['forecastday'][day]['day']['maxtemp_f'] > max_temp:
    max_temp = lhr_weather_forecast['forecast']['forecastday'][day]['day']['maxtemp_f']
    print(lhr_weather_forecast['forecast']['forecastday'][day]['date'])