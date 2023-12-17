import random
import os

from math import sqrt

my_name = 'Bob'
my_age = 53
my_height = 1.83

my_list = [1, "text", 4.5, 5]

my_dictionary = {'name': 'bob', 'age': 53, 'height': 1.83}

# print (my_dictionary['name'])

# print (my_name[0].isupper())
# print (my_name[0].islower())

def add_numbers(number1, number2):
    return number1 + number2

results = add_numbers(1, 2)
print (results)
results = 16
sqrt_result = sqrt(results)
print (sqrt_result)


start = 1
end = 10
for i in range(start, end + 1):
    if i % 2 == 0:
        print (i, " is even")
    else:
        print (i, " is odd")