# How do you start a Jupyter notebook server?

jupyter notebook

# How do you stop a Jupyter notebook server?

ctrl+c (hold down ctrl, press c)
DO YOU REALLY WANT TO?, then press y
exit()
exit
\q

# APIs don’t usually give us CSV files – what data format do they use?

json
javascript object notation

# My editor wants me to use the urllib library to talk to an API. What do I do?

use requests!!!!

# When you’re using an API, what does the word “endpoint” mean?

URL

# We're trying to run the code below, but we get the error (also below). What went wrong, and how do we fix it?

import giraffes
Module Not Found: giraffes


# rm = remove
# -rf = r = recursive "go inside of directories" = f = "force" = "don't confirm if i want to do this"
# rm -rf / 
# alt+f4 

# WELCOME TO THE BUBBLEGUM API
# Dear User,
# Welcome to the Bubblegum JSON API, available at api.bubblegum.com! Your API key is b335. Endpoints are below.
# Note: Your API key must be added to the end of the URL using the parameter APIKEY, like: ?APIKEY=[APIKEY]


# What is the full URL to retrieve complete data for the gum named “Minty Fresh”?

https://api.bubblegum.com/gum/321/show.json?APIKEY=b335

# Request a list of all gum flavors, and print each flavor’s name

import requests
url = "https://api.bubble.gum/gum/list.json?APIKEY=b335"
response = requests.get(url)
data = response.json()

for gum in data['gums']:
    print(gum['name'])
