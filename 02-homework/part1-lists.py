# Ilena Peng
# Homework 2, Part 1
# November 3, 2021

# PART ONE: Lists

# Make a list of the following numbers: 22, 90, 0, -10, 3, 22, and 48
my_list = [22, 90, 0, -10, 3, 22, 48]

# Display the number of elements in the list.
print(len(my_list))

# Display the 4th element of this list.
print(my_list[3])

# Display the sum of the 2nd and 4th element of the list.
print(my_list[1] + my_list[3])

# Display the 2nd-largest value in the list.
list_sorted = my_list
list_sorted.sort()
print(list_sorted[-2])

# Display the last element of the original unsorted list
print(my_list[-1])

# Display the sum of all of the numbers divided by two.
print(sum(my_list))

# Print whether the median or the mean of the numbers is higher
n = len(list_sorted)
# Find mean
mean = sum(list_sorted) / n
# Find median 
median = list_sorted[n//2]

if median > mean:
    print("The median is higher")
else: 
    print("The mean is higher")

# PART ONE: Dictionaries

# 1) Sometimes dictionaries are used to describe multiple aspects of a single object. Like, say, a movie. Define a dictionary called movie that works with the following code.
# print("My favorite movie is", movie['title'], "which was released in", movie['year'], "and was directed by", movie['director'])
movie = {
  'title': 'Spotlight',
  'year': 2015,
  'director': 'Tom McCarthy'
}

# 2) On the lines after that, add keys to the movie dictionary for budget and revenue (you'll use code like movie['budget'] = 1000), and print out the difference between the two.
# Source: https://www.the-numbers.com/movie/Spotlight#tab=summary
movie['budget'] = 20000000
movie['revenue'] = 91902438
print(movie['revenue'] - movie['budget'])

# 3) If the movie cost more to make than it made in theaters, print "That was a bad investment". If the film's revenue was more than five times the amount it cost to make, print "That was a great investment." Otherwise print "That was an okay investment."
if movie['budget'] > movie['revenue']:
    print("That was a bad investment.")
elif movie['revenue'] > 5*movie['budget']:
    print("That was a great investment.")
else:
    print("That was an okay investment.")

# 4) Sometimes dictionaries are used to describe the same aspects of many different objects. Make ONE dictionary that describes the population of the boroughs of NYC. Manhattan has 1.6 million residents, Brooklyn has 2.6m, Bronx has 1.4m, Queens has 2.3m and Staten Island has 470,000. (Tip: keeping it all in either millions or thousands is a good idea)
ny_population = {
  'Manhattan': 1.6,
  'Brooklyn': 2.6,
  'Bronx': 1.4,
  'Queens': 2.3,
  'Staten Island': 0.47
}

# 5) Display the population of Brooklyn.
print(ny_population['Brooklyn'])

# 6) Display the combined population of all five boroughs.
ny_sum_population = sum(ny_population.values())
print(ny_sum_population)

# 7) Display what percent of NYC's population lives in Manhattan.
bklyn_percent = (ny_population['Brooklyn'] / ny_sum_population)*100
print(f'{bklyn_percent:.2f}%')