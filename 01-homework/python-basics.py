# Ilena Peng
# Oct. 31, 2021
# Homework 1

# FEEDBACK
# should rename as birth_year
# LOC = Lines of code
# He likes my original method more than the one line: birth_year = int(input("What year were you born?")) bc it separates the step
# Also should add spaces between all the = and minus signs
# D.R.Y = don't repeat yourself
# if you want to run it in the future > currentyear = datetime.datetime.now().year  
# he dislikes comments, thinks that ur code should be self explanatory
# for heartbeats start from bpm and then multply so it's more self explanatory
# adding a dictionary for this might be a better idea
# magic #s = constants, don't change throughout the program

# Presidents: best way to do it
# he said this is too complicated bc too many syntax errors. rarely think "this is what i want to use a dictionary for"
# should think baout it like. was i born between X and Y. if no, was i born between X2 and Y2
# range1 = (X, Y)
# if birth_year in range(1977,1981):
#     print("Carter was president")
# elif birth_year in range (1981,1989):
#     print("Reagan was president")

# Instead of
# if birthyr > 1953 & birthyr < 1960: print("The president was Dwight D. Eisenhower")
    # elif birthyr > 1960 & birthyr < 1963: print("The president was John F. Kennedy")
    # elif birthyr > 1963 & birthyr < 1969: print("The president was Lyndon B. Johnson")

# Do
# if birthyr > 1953 & birthyr < 1960: print("The president was Dwight D. Eisenhower")
#     elif birthyr < 1963: print("The president was John F. Kennedy")
#     elif birthyr < 1969: print("The president was Lyndon B. Johnson")



#Chuqin's method
#create a dictionary, the keys are the start year and the values are names and parties
# Presidents = {1953:['Dwight D. Eisenhower','Republican'],
# 1961:['John F. Kennedy','Democratic'],
# 1963:['Lyndon B. Johnson','Democratic'],
# 1969:['Richard Nixon','Republican'],
# 1974:['Gerald Ford','Republican'],
# 1977:['Jimmy Carter','Democratic'],
# 1981:['Ronald Reagan','Republican'],
# 1989:['George H. W. Bush','Republican'],
# 1993:['Bill Clinton','Democratic'],
# 2001:['George W. Bush','Republican'],
# 2009:['Barack Obama','Democratic'],
# 2017:['Donald Trump','Republican'],
# 2021:['Joe Biden','Democratic']}

#check what range does the birthyear fall
#check from 2021 to 1953. It will stop when birthyear is bigger than the start year of the president
# if birthyear < 1960:
#     print("Sorry, finding the president service is not available yet for your birthyear.")
# else:
#     for y in sorted(Presidents.keys(), reverse=True):
#         if birthyear >= y:
#             break
#     president_year = y
#     president = Presidents[y][0]
#     print("President",president,"was in office when you were born.")

#  #check from the birthyear to 2021. If the president party is democratic, count once.
#     Democratic_number = 0
#     for y in sorted(Presidents.keys()):
#         if president_year <= y and Presidents[y][1] == 'Democratic':
#             Democratic_number = Democratic_number +1
#     print("There has been",Democratic_number,"Democratic presidents since you were born.")

# # Make list for presidents later
# party=['Republican' , 'Democratic','Democratic','Republican','Republican','Democratic' ,'Republican' ,'Republican' ,'Democratic' ,'Republican' ,'Democratic','Republican','Democratic']
# x='Democratic'

# Define function for counting number of presidents later
def countX(lst, x):
    count = 0
    for ele in lst:
        if (ele == x):
            count = count + 1
    return count

# Prompt the user for their year of birth (If someone says they were born in the future, try asking them again (assume they'll do it right the second time).
birthyr = input("What year were you born?")
birthyr=int(birthyr)
age=2021-birthyr

if birthyr < 2021:
        # How old the user is 
    print(f'You are {age} years old')

        # How many times the user's heart has beaten. Source: https://www.somatechnology.com/blog/fun-fact-friday/how-many-times-does-your-heart-beat-in-a-day/
    print(f'Your heart has beaten {age*3195648000:,} times')

        # How many times a blue whale's heart has beaten. 2 and 34 per minute, used midpoint of 17 
        #17 beats per minute times 60 (mins per hour) times 24 (hrs per day) times 365
        #Source: https://www.livescience.com/first-blue-whale-heartbeat.html
    print(f"A whale's heart has beaten {age*17*60*24*365:,} times")

        # How many times a rabbit's heart has beaten
        #120-150 beats per minute. used midpoint of 135
        #135 beats per minute times 60 (mins per hour) times 24 (hrs per day) times 365
        #Source: https://rabbit.org/temperature-and-respiration-rates
    print(f"A rabbit's's heart has beaten {(age*135*60*24*365)//1000000:,} million times")

        # Source for all planet questions: https://www.universetoday.com/37507/years-of-the-planets/
        # How old they are in Venus years
    print(f"You are {age*0.6152} years old on Venus")

        # How old they are in Neptune years
    print(f"You are {age*1648:,} years old on Neptune")

        # Whether they are the same age as you, older or younger and age difference
    if age > 20: print(f"You are {age-20} years older than me")
    else: print(f"You are {20-age} years younger than me")

        # If they were born in an even or odd year
    if birthyr % 3 == 0: print(f"You were born in an odd year")
    else: print(f"You were born in an even year")

        # How many times there has been a president from the Democratic Party in office since they were born (1960 onward, and each president only counts once)
    print('There have been {} {} presidents since you were born'.format(countX(party, x), x))

    if birthyr > 1953 & birthyr < 1960: print("The president was Dwight D. Eisenhower")
    elif birthyr > 1960 & birthyr < 1963: print("The president was John F. Kennedy")
    elif birthyr > 1963 & birthyr < 1969: print("The president was Lyndon B. Johnson")
    elif birthyr > 1969 & birthyr < 1974: print("The president was Richard Nixon")
    elif birthyr > 1974 & birthyr < 1977: print("The president was Gerald Ford")
    elif birthyr > 1977 & birthyr < 1981: print("The president was Jimmy Carter")
    elif birthyr > 1981 & birthyr < 1989: print("The president was Ronald Reagan")
    elif birthyr > 1989 & birthyr < 1993: print("The president was George H. W. Bush")
    elif birthyr > 1993 & birthyr < 2001: print("The president was George W. Bush")
    elif birthyr > 2001 & birthyr < 2009: print("The president was Bill Clinton")
    elif birthyr > 2009 & birthyr < 2016: print("The president was Barack Obama")
    elif birthyr > 2016 & birthyr < 2020: print("The president was Donald J. Trump")
    elif birthyr > 2020: print("Joseph R. Biden")
    else:
        print("Sorry! We didn't record presidents before 1960")

else:
  print("Sorry, you can't be born in the future!!")