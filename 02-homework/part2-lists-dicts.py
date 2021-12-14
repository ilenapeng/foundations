# Ilena Peng
# Homework 2, Part 2
# November 3, 2021

# PART TWO: Lists

# 1) Make a list called "countries" - it should contain seven different countries and NOT be in alphabetical order

countries = ['Mali', 'Belize', 'Fiji', 'Cuba', 'Peru', 'Chile', 'Norway']

# 2) Using a for loop, print each element of the list
for country in countries:
  print(country)

# 3) Sort the list permanently.
countries.sort()

# 4) Display the first element of the list.
print(countries[0])

# 5) Display the second-to-last element of the list.
print(countries[-2])

# 6) Delete one of the countries from the list using its name.
countries.remove('Fiji')

# 7) Using a for loop, print each country's name in all caps.
for country in countries:
  print(country.upper())

# PART TWO: Dictionaries

# These will require LATITUDE and LONGITUDE. You can ask Google for latitude and longitude by typing in *coordinates of CITYNAME*. You can also use https://itouchmap.com/?r=latlong (Links to an external site.).

# Store the latitude and longitude without the N/S/E/W - if the latitude is S, make it negative. If the longitude is W, make it negative. (See here for explanation: https://web.archive.org/web/20210425194537/https://answers.yahoo.com/question/index?qid=20080211182008AAMdUe8 (Links to an external site.) + https://www.mvorganizing.org/is-the-prime-meridian-east-or-west/#How_do_you_write_negative_longitude (Links to an external site.))

# 1) Make a dictionary called 'tree' that responds to 'name', 'species', 'age', 'location_name', 'latitude' and 'longitude'. Pick a tree from: https://en.wikipedia.org/wiki/List_of_trees

tree = {
  'name': 'Great sugi of Kayano',
  'species': 'Japanese cedar',
  'age': 2300,
  'location_name': 'Kaga, Ishikawa Prefecture, Japan',
  'latitude': 36.2275,
  'longitude': 136.36,
}

# 2) Print the sentence "{name} is a {years} year old tree that is in {location_name}"
print(f"{tree['name']} is a {tree['age']} year old tree that is in {tree['location_name']}")

# 3) The coordinates of New York City are 40.7128° N, 74.0059° W. Check to see if the tree is south of NYC, and print "The tree {name} in {location} is south of NYC" if it is. If it isn't, print "The tree {name} in {location} is north of NYC"
if tree['latitude'] < 40.7128:
    print(f"The tree {tree['name']} in {tree['location_name']} is south of NYC")
else:
    print(f"The tree {tree['name']} in {tree['location_name']} is north of NYC")

# 4) Ask the user how old they are. If they are older than the tree, display "you are {XXX} years older than {name}." If they are younger than the tree, display "{name} was {XXX} years old when you were born."
user_age = input("How old are you?")
user_age = int(user_age)

if user_age > tree['age']:
    print(f"You are {user_age - tree['age']} years older than {tree['name']}")
else:
    print(f"{tree['name']} was {tree['age'] - user_age} years old when you were born")

# PART TWO: Lists of dictionaries

# 1) Make a list of dictionaries of five places across the world - (1) Moscow, (2) Tehran, (3) Falkland Islands, (4) Seoul, and (5) Santiago. Each dictionary should include each city's name and latitude/longitude (see note above).

cities = [
    {'name': 'Moscow', 'latitude': 55.7558, 'longitude': 37.6173},
    {'name': 'Tehran', 'latitude': 35.6892, 'longitude': 51.3890},
    {'name': 'Falkland Islands', 'latitude': -51.7963, 'longitude': -59.5236},
    {'name': 'Seoul', 'latitude': 37.5665, 'longitude': 126.9780},
    {'name': 'Santiago', 'latitude': -33.4489, 'longitude': -70.6693}
]

# 2) Loop through the list, printing each city's name and whether it is above or below the equator (How do you know? Think hard about the latitude.). When you get to the Falkland Islands, also display the message "The Falkland Islands are a biogeographical part of the mild Antarctic zone," which is a sentence I stole from Wikipedia.

for city in cities:
    if city['name'] == 'Falkland Islands':
        if city['latitude'] < 0:
            print(f"{city['name']} is above the equator")
        else:
            print(f"{city['name']} is above the equator")
        print("The Falkland Islands are a biogeographical part of the mild Antarctic zone")
    else: 
        if city['latitude'] < 0:
            print(f"{city['name']} is above the equator")
        else:
            print(f"{city['name']} is above the equator")

# 3) Loop through the list, printing whether each city is north of south of your tree from the previous section.
for city in cities:
    if city['latitude'] < tree['latitude']:
        print(f"{city['name']} is below {tree['name']}")
    else:
        print(f"{city['name']} is below {tree['name']}")