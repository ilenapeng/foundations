# JSON = JavaScript Object Notation
# (basically looks like a dictionary, basically acts like a dictionart)
# It's a data format that is used for computers talking to each other
# We don't care if it's related to JavaScript, we're using it anyway!!!!!!!

import requests

response = requests.get("https://pokeapi.co/api/v2/pokemon/slowpoke")

# how tall is raichu
data = response.json()
print(data)





response = requests.get("https://pokeapi.co/api/v2/pokemon/raichu")

# how tall is raichu
data = response.json()
print(data)
print("The keys are")
print(data.keys())
print("The height is", data['height'])
#print(data['height'])