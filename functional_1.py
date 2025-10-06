from functools import reduce


def Capt(item):
    return item.capitalize()


def above_50(item):
    return item >= 50


def Combine(acc, item):
    return acc + item


# 1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']

print(list(map(Capt, my_pets)))

# 2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5, 4, 3, 2, 1]

my_sorted_numbers = sorted(my_numbers)
print(list(zip(my_strings, my_sorted_numbers)))

# 3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]

print(list(filter(above_50, scores)))

# 4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?

all_numbers = my_numbers + scores

print(reduce(Combine, all_numbers, 0))
