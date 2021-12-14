# Cmd + / = comments things out (even multiple lines)
# How old the user is
# "LOC"
birth_year = input("What year were you born?")
# birth_year = int(input("What year were you born?"))
birth_year = int(birth_year)
age = 2021 - birth_year


year_of_birth = input("Enter the year you were born in: ")
current_year = 2021



year_of_birth = int(year_of_birth)

# How old the user is
age = 2021 - year_of_birth


if year_of_birth > 2000:
    print("Soma was president")

year_of_birth
birth_year
year
year_person_was_born



# D.R.Y. = don't repeat yourself


whale_heart_beat_4 = 4 * 60 * 24 * 365 * exact_age

# usually beats per minute
print("Your heart has beaten", heartbeats, "times")
print(f"Your heart has beaten {heartbeats:,} times")
print("Your heart has beaten 35,000,000 times")
whale_heartbeats = age * 37 * 60 * 24 * 365
print("A blue wale's heart has beaten", whale_heartbeats, "times") #source: https://www.medicalnewstoday.com/articles/327129#Blue-whales-heart-performs-at-extremes


birthmin = age * 365 * 60
humanheart = birthmin * 72
print(f'Your heart has beaten {humanheart:,} times')



#heartbeats: heartbeats per year * age
print("Your life in heartbeats:")
beats = {
    "human": 35000000,
    "whale": 10512000,
    "rabbit": 84096000
}
print (f"Your heart: {beats['human'] * age:,} times")
print (f"A blue whale: {beats['whale'] * age:,} times")


# "magic numbers" = "constants"
HUMAN_HEARTBEATS_PER_YEAR = 35000000
BLUE_WHALE_HEARTBEATS_PER_YEAR = 13000000


lifetime_human_heartbeats = user_age_by_year * HUMAN_HEARTBEATS_PER_YEAR / 1000000
lifetime_blue_whale_heartbeats = user_age_by_year * BLUE_WHALE_HEARTBEATS_PEAR_YEAR / 1000000

print(f"Your heart has beaten {lifetime_human_heartbeats} million times since you were born\n")
print(f"A blue whale's heart has beaten {lifetime_blue_whale_heartbeats} million times since you were born\n")





whale_heart_beat_4 = 4 * 60 * 24 * 265 * exact_age
whale_heart_beat_8 = 8 * 60 * 24 * 265 * exact_age
print("3. A blue whale's heart beats an average of 4 to 8 times per minute. This means that since you've been alive, a blue whale's heart has beaten between", whale_heart_beat_4, "and", whale_heart_beat_8, "times on average.")

# How many times the user's heart has beaten
# How many times a blue whale's heart has beaten
# How many times a rabbit's heart has beaten
# If the answer to rabbit heartbeats is more than a million, say "XXX million" instead of the very long raw number
# How old they are in Venus years
# How old they are in Neptune years
# Whether they are the same age as you, older or younger
# If older or younger, how many years difference
# If they were born in an even or odd year
# How many times there has been a president from the Democratic Party in office since they were born (1960 onward, and each president only counts once)
# Which US President was in office when they were born (1960 onward)


presidents = {
    '1960': "Dwight D. Eisenhower",
    '1961': "John F. Kennedy",
    '1962': "John F. Kennedy",
    '1963': "John F. Kennedy",
    '1964': "Lyndon B. Johnson",
    '1965': "Lyndon B. Johnson", 
    '1966': "Lyndon B. Johnson", 
    '1967': "Lyndon B. Johnson",
    '1968': "Lyndon B. Johnson",
    '1969': "Richard Nixon"
}


for key, value in presidents.items():
    if birth_str in key: 
        print (f"In {birth}, {value} was in office.") 


presidents = {
    1960: ["Dwight D. Eisenhower", 6],
    1961: ["John F. Kennedy", 6],
    1964: ["Richard Lyndon B. Johnson", 5],
    1969: ["Richard Nixon", 4],
    1975: ["Gerald Ford", 4],
    1977: ["Jimmy Carter", 4],
    1981: ["Ronald Reagan", 3],
    1989: ["George H.W. Bush", 3],
    1993: ["Bill Clinton", 3],
    2001: ["George W. Bush", 2],
    2009: ["Barack Obama", 2],
    2017: ["Donald Trump", 1],
    2021: ["Joe Biden", 1]
}


def find_president(year):
    current_president = None
    current_democratic_tally = None
    for key in presidents.keys():
        presidential_info = presidents[key]
        if (year >= key):
            current_president = presidential_info[0]
            current_democratic_tally = presidential_info[1]
    print(f"You were born when {current_president} was president!\n")
    print(f"There have been {current_democratic_tally} Democratic presidents since you were born!\n")

find_president(user_year)


presidents = {
1961:"John F. Kennedy", 
1963:"Lyndon B. Johnson", 
1969:"Richard M. Nixon",
1974:"Gerald R. Ford",
1977:"Jimmy Carter",
1981:"Ronald Reagan", 
1989:"George Bush", 
1993:"Bill Clinton", 
2001:"George W. Bush", 
2009:"Barack Obama", 
2017:"Donald J. Trump", 
2021:"Joe Biden"
}
birth_president = ""
for year, president in presidents.items():
    if birth_year >= year:
        birth_president = president
print(f"When you were born, {birth_president} was the President")


# Carter: 1977 – 1981
# Reagan: 1981 – 1989
# Bush 1: 1989 – 1993

# "Was I born between 1977 and 1981" no
# "Was I born between 1981 and 1989" yes


birth_year = 1983

if birth_year in range(1977, 1981):
#if birth_year in [1977, 1978, 1979, 1980, 1981]:
    print("Carter was president")
elif birth_year in range(1981, 1989):
    print("Reagan was president")


if birth_year <= 1977:
    print("No one was president before then"):
elif birth_year > 1977 and birth_year <= 1981:
    print("Carter was president")
elif birth_year > 1981 and birth_year <= 1989:
    print("Reagan was president")
elif birth_year > 1989 and birth_year <= 1993:
    print("Bush 1 was president")



elif 1977 < birth_year <= 1981:




if birth_year <= 1977:
    print("No one was president before then"):
elif birth_year <= 1981:
    print("Carter was president")
elif birth_year <= 1989:
    print("Reagan was president")
elif birth_year <= 1993:
    print("Bush 1 was president")

