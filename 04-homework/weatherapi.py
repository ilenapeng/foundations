#!/usr/bin/env python
# coding: utf-8

# # WeatherAPI (Weather)
# 
# Answer the following questions using [WeatherAPI](http://www.weatherapi.com/). I've added three cells for most questions but you're free to use more or less! Hold `Shift` and hit `Enter` to run a cell, and use the `+` on the top left to add a new cell to a notebook.
# 
# Be sure to take advantage of both the documentation and the API Explorer!
# 
# ## 0) Import any libraries you might need
# 
# - *Tip: We're going to be downloading things from the internet, so we probably need `requests`.*
# - *Tip: Remember you only need to import requests once!*

# In[1]:


import requests


# ## 1) Make a request to the Weather API for where you were born (or lived, or want to visit!).
# 
# - *Tip: The URL we used in class was for a place near San Francisco. What was the format of the endpoint that made this happen?*
# - *Tip: Save the URL as a separate variable, and be sure to not have `[` and `]` inside.*
# - *Tip: How is north vs. south and east vs. west latitude/longitude represented? Is it the normal North/South/East/West?*
# - *Tip: You know it's JSON, but Python doesn't! Make sure you aren't trying to deal with plain text.* 
# - *Tip: Once you've imported the JSON into a variable, check the timezone's name to make sure it seems like it got the right part of the world!*

# In[2]:


url_cupertino = "http://api.weatherapi.com/v1/current.json?key=1a6fa10583f54fcdbfa115430210411&q=95014&aqi=no"

response_cupertino = requests.get(url_cupertino)
data_cupertino = response_cupertino.json()


# In[3]:


print(data_cupertino['location']['tz_id'])


# ## 2) What's the current wind speed? How much warmer does it feel than it actually is?
# 
# - *Tip: You can do this by browsing through the dictionaries, but it might be easier to read the documentation*
# - *Tip: For the second half: it **is** one temperature, and it **feels** a different temperature. Calculate the difference.*

# In[4]:


print(data_cupertino['current'])


# In[5]:


# current wind speed
print(data_cupertino['current']['wind_mph'])


# In[6]:


# difference between actual and feels like temperature
current_temp = data_cupertino['current']['temp_f']
feels_like = data_cupertino['current']['feelslike_f']

difference = current_temp - feels_like
print(difference)


# ## 3) What is the API endpoint for moon-related information? For the place you decided on above, how much of the moon will be visible tomorrow?
# 
# - *Tip: Check the documentation!*
# - *Tip: If you aren't sure what something means, ask in Slack*

# In[7]:


# The API endpoint is http://api.weatherapi.com/v1/astronomy.json
url_moon = "http://api.weatherapi.com/v1/astronomy.json?key=1a6fa10583f54fcdbfa115430210411&q=Cupertino&dt=2021-11-09"

response_moon = requests.get(url_moon)
data_moon = response_moon.json()


# In[8]:


# print(data.keys())
# print(data['astronomy'])
print(data_moon['astronomy']['astro']['moon_illumination'])


# ## 4) What's the difference between the high and low temperatures for today?
# 
# - *Tip: When you requested moon data, you probably overwrote your variables! If so, you'll need to make a new request.*

# In[9]:


# No max/min temp in the current temperatures for the day -- need to look at the forecast
url_forecast = "http://api.weatherapi.com/v1/forecast.json?key=1a6fa10583f54fcdbfa115430210411&q=Cupertino&days=3&aqi=no&alerts=no"

response_forecast = requests.get(url_forecast)
data_forecast = response_forecast.json()


# In[10]:


# print(data_forecast.keys())
# print(data_forecast['forecast'])
max_temp = data_forecast['forecast']['forecastday'][0]['day']['maxtemp_f']
min_temp = data_forecast['forecast']['forecastday'][0]['day']['mintemp_f']

print(max_temp - min_temp)


# ## 4.5) How can you avoid the "oh no I don't have the data any more because I made another request" problem in the future?
# 
# What variable(s) do you have to rename, and what would you rename them?

# In[11]:


# Did this in my above variables already, as opposed to renaming them in this block!
# Added _cupertino to the end of url, response and data fields for requesting the Cupertino data
# Added _moon to the end of url, response and data fields for requesting the Astronomy data
# Added _forecast to the end of url, response and data fields for requesting the forecast data

# Marked below are all the places where variables had to be renamed
# url field here:
# url_moon = "http://api.weatherapi.com/v1/astronomy.json?key=1a6fa10583f54fcdbfa115430210411&q=Cupertino&dt=2021-11-09"
# # response and url field here:
# response_moon = requests.get(url_moon)
# # data and response field here:
# data_moon = response_moon.json()


# ## 5) Go through the daily forecasts, printing out the next three days' worth of predictions.
# 
# I'd like to know the **high temperature** for each day, and whether it's **hot, warm, or cold** (based on what temperatures you think are hot, warm or cold).
# 
# - *Tip: You'll need to use an `if` statement to say whether it is hot, warm or cold.*

# In[12]:


# print(data_forecast['forecast']['forecastday'][0]['day']['maxtemp_f'])

# for day in data_forecast['forecast']['forecastday']:
#     print (day['day']['maxtemp_f']) 

for day in data_forecast['forecast']['forecastday']:
    print (day['day']['maxtemp_f']) 
    if day['day']['maxtemp_f'] > 80:
        print("Yowza, it's hot!")
    if day['day']['maxtemp_f'] < 50:
        print("Brrr, it's cold!")
    else:
        print("It's just right!")


# ## 5b) The question above used to be an entire week, but not any more. Try to re-use the code above to print out seven days.
# 
# What happens? Can you figure out why it doesn't work?
# 
# * *Tip: it has to do with the reason you're using an API key - maybe take a look at the "Air Quality Data" introduction for a hint? If you can't figure it out right now, no worries.*

# In[13]:


url_forecast7 = "http://api.weatherapi.com/v1/forecast.json?key=1a6fa10583f54fcdbfa115430210411&q=Cupertino&days=7&aqi=no&alerts=no"

response_forecast7 = requests.get(url_forecast)
data_forecast7 = response_forecast7.json()


# In[14]:


# Nothing happens, it just returns the same three days we had before!
for day in data_forecast7['forecast']['forecastday']:
    print (day['day']['maxtemp_f']) 
    if day['day']['maxtemp_f'] > 80:
        print("Yowza, it's hot!")
    if day['day']['maxtemp_f'] < 50:
        print("Brrr, it's cold!")
    else:
        print("It's just right!")


# In[15]:


# This is because of the API key's limits
# https://www.weatherapi.com/docs/ -> "Air Quality" section
# "Depending upon your subscription plan we provide current and 3 day air 
# quality data for the given location in json and xml."


# ## 6) What will be the hottest day in the next three days? What is the high temperature on that day?

# In[16]:


max_temp = 0
max_temp_day = 0
for day in data_forecast['forecast']['forecastday']:
    if (day['day']['maxtemp_f'] > max_temp):
            max_temp = day['day']['maxtemp_f']

print(f"{day['date']} is the hottest day in the next three days with a temperature of {max_temp}")


# ## 7) What's the weather looking like for the next 24+ hours in Miami, Florida?
# 
# I'd like to know the temperature for every hour, and if it's going to have cloud cover of more than 50% say "{temperature} and cloudy" instead of just the temperature. 
# 
# - *Tip: You'll only need one day of forecast*

# In[17]:


url_miami = "http://api.weatherapi.com/v1/forecast.json?key=1a6fa10583f54fcdbfa115430210411&q=Miami&days=1&aqi=no&alerts=no"

response_miami = requests.get(url_miami)
data_miami = response_miami.json()


# In[18]:


# temperature for every hour
# print(data_miami['forecast']['forecastday'][0].keys())
# print(data_miami['forecast']['forecastday'][0]['hour'])

# testing this out without the for loop
# print(data_miami['forecast']['forecastday'][0]['hour'][0]['time'])
# print(data_miami['forecast']['forecastday'][0]['hour'][0]['temp_f'])
# print(data_miami['forecast']['forecastday'][0]['hour'][0]['cloud'])

for hour in data_miami['forecast']['forecastday'][0]['hour']:
    if hour['cloud'] > 50:
        print(f"{hour['time']}: {hour['temp_f']} and cloudy")
    else:
        print(f"{hour['time']}: {hour['temp_f']}")


# ## 8) For the next 24-ish hours in Miami, what percent of the time is the temperature above 85 degrees?
# 
# - *Tip: You might want to read up on [looping patterns](http://jonathansoma.com/lede/foundations-2017/classes/data%20structures/looping-patterns/)*

# In[19]:


above85_count = 0

for hour in data_miami['forecast']['forecastday'][0]['hour']:
  if hour['temp_f'] > 85:
    above85_count = above85_count + 1

# len(data_miami['forecast']['forecastday'][0]['hour']) -> returns 24
above85_pct = above85_count/len(data_miami['forecast']['forecastday'][0]['hour'])

print(f'For the next 24 hours in Miami, the temperature is above 85 degrees {above85_pct}% of the time')


# ## 9) How much will it cost if you need to use 1,500,000 API calls?
# 
# You are only allowed 1,000,000 API calls each month. If you were really bad at this homework or made some awful loops, WeatherAPI might shut down your free access. 
# 
# * *Tip: this involves looking somewhere that isn't the normal documentation.*

# In[20]:


# https://www.weatherapi.com/pricing.aspx
# The Developer plan gets you 2 million calls per month


# ## 10) You're too poor to spend more money! What else could you do instead of give them money?
# 
# * *Tip: I'm not endorsing being sneaky, but newsrooms and students are both generally poverty-stricken.*

# In[21]:


# Sign up for a new account with a different email address

