print("Hello Devs")
print("hdhdhd")

# Python Variables
# Variables are used to store data
# variable name cannot start with other characters except underscore ( _ )
print("//////Variables////////")
fname = "Blard"
age = 45
_gravity = 9.6
print(fname, type(fname))
print(age, type(age))
print(_gravity, type(_gravity))


# Data types
'''
-strings
-list
-sets
-dict
-float 
-int
-booleans
-tuples
''' 


#STRINGS
statement = "My name is " + fname + " I am" + str(age) + " years old"
statement2 = f'My name is {fname} and I am {age} years old'
print(statement)
print(statement2)

#String Methods- index, len, upper, lower, endwith, startwith, capitalize, tittle etc...

# len
a = len(statement)
print(a)
print(len(statement2))


# upper/lower
print(statement.upper())
print(statement.lower())

# capitalize/title
print(statement.capitalize())
print(statement2.title())

# index
print(statement[8]) 

# slice
words = "Techstudio academy"
print(words[0:10])
print(words[11:18].capitalize())
print(words[0::2])

# Give examples of the following string methods: join, replace, split, startswith, endswith
# join
liv_list = ['hello', 'world']
seperator = ' '
result = seperator.join(liv_list)
print(result)

#replace
mystring = "Hello, world!"
newstring = mystring.replace('world', 'love')
print(newstring)

#split
mysplit = 'Hello, world!'
oldstring = mysplit.split(' ')
print(oldstring)

#startswith
starts = 'Hello, world!'
startsnow = starts.startswith('Hello')
print(startsnow)

#endswith
ends = 'Hello, world!'
endsnow = ends.endswith('world!')
print(endsnow)


#Number data type
print("//////Number data type//////")

#Number data type in python int, float, complex
# num = 33
# print(num, type(num))
# BMI = 5.98
# print(BMI, type(BMI))
# comple_num = 3j + 5
# print(comple_num, type(comple_num))


# #Booleans true, false
# b = 10
# c = 32
# d = -6
# print(b, c, d)
# print(b>=c)
# print(b!=d)
# print(b > c or d < 0)
# print(b > d and c > b)
# print(d <= b and d != c)


# print(0 == False)
# print(1 == True)


# # Operators: arithemetic, assignment, comparison, logical, identity

# # Arithemetic operators are +, -, *, %, **, /, //
# print(5-1**5/2*8%2)
# print(25%4)
# print(20/3)
# print(20//3)

# #Assignment Operators are =, +=, -+=, *=, /=
# x = 4
# y = 5
# z = 6
# x = x + y
# print(x)
# x += y
# print(x)


# #Comparison Operators >, <, ==, !=, >=, <=
# print(x > y or y < x)
# print(x != y and y >= x)
# print(x == y or y != z)

# # input
# age = input("Okiki's age is: ")
# age_ = input("Enny's age is: ")
# age_sum = int(age) + int(age_)
# print(age_sum)
# final_statement = f"Okiki's age is {age} and Enny's age is {age_} and sum of their ages is {age_sum}"
# print(final_statement)

# Logical Operators and, or, not
isAdult = False
age = 16
if (not isAdult and age >= 18):
    action = f'You are permitted to drink alcohol'
    print(action)
else:
    print("Bro you're under age!")
    

# List Data Type
print("//////LISTS///////")
# List is one of the collection data types in python
# It's similar array in Javascript
# lst = list("2345566")
# print(lst, type(lst))
my_lst = ["Seun", "Dan", 45, ["javascript", "python"], 3j]
print(my_lst)

#Accessing list
first_item = my_lst[0]
print(first_item)
second_item = my_lst[1]
print(second_item)
# last_item = my_lst[-1]
index_of_last_item = len(my_lst) - 1
print(index_of_last_item)
last_item = my_lst[index_of_last_item]
print(last_item)

#len()
print(len(my_lst))

#unpacking list
fname, lname, age, skills, address = my_lst
skill1, skill2 = skills
print(f"My name is {fname} {lname}, i am {age} years old and I am a senior dev with the following stack {skill1.capitalize()} and {skill2.capitalize()}")


# List Methods
# Adding items to a list
# append(item) = can only add one item at a time
my_stacks = ['html', 'css', 'bootstrap', 'javascript', 'react']
my_stacks.append('python')
print(my_stacks)
my_stacks.append('Django')
print(my_stacks)

# Insert(index, item)
my_stacks.insert(3, 'git')
print(my_stacks)
my_stacks.insert(4, 'github')
print(my_stacks)

#extend()
even_num = [2, 4, 6]
print(even_num)
odd_num = [1, 3, 5]
even_num.extend(odd_num)
print(even_num)
odd_num.extend(even_num)
print(odd_num)

#slice()
#lst[start:end:steps]
sliced_stacks = my_stacks[0:5]
# print(sliced_stacks)
# print(sliced_stacks[0::2])

# Removing items from list
# pop(index)
sliced_stacks.pop() # removed last item of the list 
# print(sliced_stacks)
sliced_stacks.pop(0)
# print(sliced_stacks)

# clear()
sliced_stacks.clear()
# print(sliced_stacks)

# del()
del sliced_stacks
# print(sliced_stacks)

# Task 1
# Ascending order
scores = [22, 19, 24, 25, 26, 24, 25, 24, 15]
sorted_scores = sorted(scores)
print(sorted_scores)

# Descending order
scores.sort(reverse=True)
print(scores)

# Max score
max_score = max(scores, key=lambda x: x)
print(max_score)

# Min score
min_score = min(scores, key=lambda x: x)
print(min_score)

# Task 2
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']

# Join both lists
front_end.extend(back_end)
print(front_end)

# Copy the previous list
full_stack = front_end[:]
print(full_stack)

# Adding items
full_stack.insert(5, 'Python')
print(full_stack)
full_stack.insert(6, 'SQL')
print(full_stack)


# Tuples
# Tuple is one of the four collection data types in python
# tuple is created using () or constructor function tuple()
# Tuples are ordered and indexed
# Tuples can not be modified directly
# To modify tuples, you need to convert them to list, modify and then convert back to tuple
tpl = tuple([1,2,3,4,5])
print(tpl, type(tpl))
my_tpl = (1, 2, 3, 4, True, 5.3)
print(my_tpl, type(tpl))
print(my_tpl[-1])
print(my_tpl[0])

# How to update tuple
my_tpl2 = list(my_tpl)
print(my_tpl2, type(my_tpl2))
my_tpl2[0] = 'item1'
print(my_tpl2)
my_tpl2.insert(4, "james")
my_tpl2.insert(5, 'love')
print(my_tpl2)
my_tpl3 = tuple(my_tpl2)
print(my_tpl3)
print(my_tpl3[::2])


# Sets
# Set is also a collection data type in python
# set is unordered and unindexed
# set is created using curly braces or set constructor functions
# once a set is created, we can not change any items, but we can add additional items 
# set does not recognize duplicates

# Creating set
my_set = set([1, 3, True, 0, False, 5])
print(my_set, type(my_set))
new_set = {"red", "blue", "yellow", "black"}
print(new_set)

# updating sets
# Adding single item to a set
new_set.add("green")
print(new_set)

# Adding multiple item to a set
add_color = {"purple", "brown", "Orange"}
new_set.update(add_color)
print(new_set)
# print(new_set.pop())
# new_set.clear()
# print(new_set)
print('green' in new_set)
if (len(new_set) > 0 and 'purple' in new_set):
    print('Set background color to purple')
else:
    print("Set background color to black")
    
# CONDITIONALS if, else, elif, and range
# if(0 != False):
#     print("Waw!")
# else:
#     print("Wahala!")

# number = int(input("Enter a number:"))
    
# if(number % 2 == 0):
#     print(f'The {number} is an even number')
# elif (number % 2 == 1):
#     print(f'The {number} is an odd number')
# else:
#     print('Error')
    
# try:
#     entered_value = int(input('Enter a valid input:'))
#     print(f'You entered {entered_value}')
# except ValueError:
#     print(f'Invalid input!')
    

# Looping
# for loop
# while loop

# for
# for condition:
cars = ['mercedes', 'lexus', 'toyota', 'honda', 'bmw']
for car in cars:
    print(f"My favorite car is {car.capitalize()}")

# Task 5
for i in range(1, 13):
    print(f'{12} x {i} = {12} * {i}')
        
# Task 6
clubs = ('Arsenal', "Everton", "Chelsea", "Liverpool")

for club in clubs:
    print(club[0:3].upper())

# first, second, third, fourth = clubs
# print(first[0:3].upper())
# print(second[0:3].upper())
# print(third[0:3].upper())
# print(fourth[0:3].upper())

# Task 7
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in numbers:
    result = number * 2
    print(result)

# # steps in range
# for n in range(0,21,2):
#     if(n > 0):
#         print(n)

# for n in range(1,21):
#     print(n*2)

# While loop
i = 0
while i <= 4:
    print(f"This car brand is {cars[i]}")
    i += 1
    
# # Task 8
# try:
#   while True:
#     num_1 = int(input("Enter a number: "))
#     operator = input("Enter an operator (+, -, *, /): ")
#     num_2 = int(input("Enter a number: "))

#     result = None

#     if operator == '+':
#         result = num_1 + num_2
#     elif operator == '-':
#         result = num_1 - num_2
#     elif operator == '*':
#         result = num_1 * num_2
#     elif operator == '/':
#         if num_2 != 0:
#             result = num_1 / num_2
#         else:
#             print("Error: Division by zero")
#             break
#     else:
#         print("Invalid operator")
#         break

#     print("Result:", result)
    
#     choice = input("Continue? (y/n): ")
#     if choice.lower() != 'y':
#         break
    
#     operator = input("Enter an operator (+, -, *, /): ")
#     num_3 = int(input("Enter a number: "))
    
#     newresult = None
    
#     if operator == '+':
#         newresult = result + num_3
#     elif operator == '-':
#         newresult = result - num_3
#     elif operator == '*':
#         newresult = result * num_3
#     elif operator == '/':
#         if result != 0:
#             newresult = result / num_3
#         else:
#             print("Error: Division by zero")
#             break
#     else:
#         print('Invalid operator')
#         break
#     print("Newresult:", newresult)
# except ValueError:
#     print(f'Invalid input!')
        
        
# Dictionary
# Dict is one the four collection data type but more often referred to as mapping data type
# Dict are key-value pair of data type in python
# Dict are json-like data stored in curly braces
# Creating Dict

dct = dict()
my_dct = {
    "name": "Blard",
    "age": "20",
    "occupation": "farmer",
    "skills": ["html","python"],
    "address": {
        "street": "Lukuku",
        "city": "Lagos"  
    }
}
print(my_dct, type(my_dct))

# Accessing dict
print(my_dct["name"])
print(my_dct["skills"][1].capitalize())
print(my_dct["address"]['street'].capitalize())

# Adding items to dictionary
my_dct['hobbies'] = "Coding", "sky-diving"
print(my_dct['hobbies'])
print(my_dct)

my_dct.update({"qualifications": "PHD", "Gender": "M"})
print(my_dct)

# Remove items from dictionary
# pop()
print(my_dct.pop('qualifications'))
del my_dct["Gender"]
print(my_dct)
# popitem()
print(my_dct.popitem())

# Looping Dictionary
for value in my_dct['skills']:
    print(f"I'm proficient in {value.capitalize()}")
    
# unpacking dict
m, n, p, q, r = my_dct.keys()
m, n, p, q, r = my_dct.values()
m, n, p, q, r = my_dct.items()
print(m, n, p, q, r)
print(q)

# Assignment one
bro_tuple = ("Charles", "Patrick", "Rafeal", "Olamide")
sis_tuple = ("Lilian", "Precious", "Peculiar", "Treasure")
total_siblings = bro_tuple + sis_tuple
print(total_siblings)
print(len(total_siblings))
family_members = list(total_siblings)
family_members.insert(0, 'Austin')
print(family_members)
family_members.insert(1, "Veronica")
print(family_members)
one, two, three, four, five, six, seven, eight, nine, ten = family_members
print(one, two)
print(three, four, five, six, seven, eight, nine, ten)
parent = one, two
print(parent)
siblings = three, four, five, six, seven, eight, nine, ten
print(siblings)

# Assignment two
for x in range(1,101,3):
    print(x)
    
# Functions
def example_code():
    print("Sample code running...")
example_code()

# function with parameters
def greet(name="stranger"):
    print(f'Hello {name}')
greet("Okiki")

def add_num(a,b):
    print(f"{a+b}")
add_num(3,5)

# unlimited numbers of arguments *args
def num_args(*args):
    for n in args:
        print(f'The square of {n} = {n**2}')
num_args(2,3,4,5,5,78,99,20,13,77)

def my_siblings(*a):
    print(f'The youngest child is {a[0]}')
    print(f'The youngest child is {a[2]}')
    print(f'The youngest child is {a[3]}')
    
my_siblings("Tayo", "Enny", "Sam", "Pascal")

# Keyword arguments **kwargs
def my_keyword(**k):
    print(f"The keyword argument is {k['key3']}")
    print(f"The keyword argument is {k['key1']}")
    # print(f"The keyword argument is {k['key2']}")
    print(f"The keyword argument is {k['key4']}")

my_keyword(key3='Gerald', key1='Eddy', key4='Seun')

# return
def do_math(a,b):
    return a+b*a-b
print(do_math(4,2))

# pass
def do_pass():
    # empty function
    pass
do_pass()

# continue
fruits = ['apple', 'orange', 'pineapple', 'guava', 'grape']
def fav_fruits():
    for fruit in fruits:
        if fruit.endswith('e'):
            continue
        print(f'My favorite fruit is {fruit}')
fav_fruits()


# class work
numbers_1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
def find_even_num():
    evens = []
    for num in numbers_1:
        if num % 2 == 0:
            print(f'This {num} is even number')
            evens.append(num)
    return evens
 
print(find_even_num())


# Lambda Functions
# lambda args : expression
my_lambda_fn = lambda a : a**2
print(my_lambda_fn(8))
do_lam = lambda name, age : f'{name} is {age} years old'
print(do_lam("Blard", 65))

'''
Write different functions which take lists. They should calculate mean, median, mode, range, variance and standard deviation
'''
from statistics import mean, mode, median, stdev, variance

math_num = [10,5,12,5,6,7,9,5,15]
def calculate_mean(math_num):
    print(mean(math_num))
calculate_mean(math_num)


def calculate_median(math_num):
        print(median(math_num))
calculate_median(math_num)

def calculate_mode(math_num):
        print(mode(math_num))
calculate_mode(math_num)

def calculate_variance(math_num):
    print(variance(math_num))
calculate_variance(math_num)

def calculate_stdev(math_num):
    print(stdev(math_num))
calculate_stdev(math_num)

def calculate_range(math_num):
    max_num = math_num[-1]
    min_num = math_num[1]
    range = max_num - min_num
    return range
print(calculate_range(math_num))
# Modules
# What is a Module
'''
A module is a file containing a set of codes or a set of functions which can be included to an application. A module could be a file containing a single variable, a function or a big code base.
'''
# from module import generate_tax
# print(generate_tax("Blard",2500,8))

# from ajay import person_data
# print(person_data("Ajama","Samson",23))

'''
Like other programming languages we can also import modules by importing the file/function using the key wrod import. Let's import the common module we will use most of the time. Some of the common built-in modules: math, datetime, os, sys, random, statistics, collections, json, re

'''
# from math import pi, ceil, floor, sqrt, pow
# print(pi)
# print(sqrt(55))
# print(ceil(sqrt(443)))
# print(pow(4,5))

# from random import random, randint
# print(ceil(random()*7))
# print(randint(1,6))

# import re
# def re_gex():
#     exp = input("Enter a number: ")
#     exp2 = re.sub('[a-zA-z,.:()""]', '', exp)
#     result = eval(exp2)
#     return result
# print(re_gex())

# txt = "Python is my favorite programming language. Building with python is fun"
# print(txt)
# sub_txt = re.sub('[Pp]ython', 'Javascript', txt)
# print(sub_txt)

# # Changing the name of imports
# from module import free_style as something_else
# print(something_else())

# OOP (Object Oriented Programming)
# Classes
# Python is an object oriented programming language, with its properties and methods.
# Everything in python is an object of a corresponding built-in class
# We instantiate a class to create an object, however the class defines the attributes and behaviour of the object.

# Creating an class
# To create a class, we use the 'class' keyword.
class Person:
    # properties of person
    def __init__(self, fname, lname, nationality, lang):
        self.fname = fname
        self.lname = lname
        self.nationality = nationality
        self.lang = lang
        
    def person_info(self, age, tittle):
        self.age= age
        self.title= tittle
        return(f"I'm {self.title} {self.fname} {self.lname} and age {self.age}, I'm a {self.nationality} and i speak {self.lang}")
    def person_data(self, occupation, income, tax):
        self.occupation = occupation
        self.income = income
        self.tax = income*10//100
        return(f'I work at {self.occupation}, i earn {self.income} and i pay tax of {self.tax} every month')

# print(Person)

person1 = Person("Blard", "John", "Nigerian", "English")
person2 = Person("james", "john", 'argentina', 'spanish')
# print(person1)
print(person1.person_info(23, 'Sir'))
print(person2.person_data("TechStudio", 50000, 5000))


# class BankAccount:
#     def __init__(self, name, money, pin):
#         self.name = name
#         self.money = money
#         self.pin = pin
        
#     def deposit_amt(self, funds):
#         self.funds = funds
#         self.money += funds
        
#     def withdraw_amt(self, withdraw):
#         if self.money < withdraw:
#             return(f'Insufficient Funds')
#         else:
#             self.money -= withdraw
        
        
#     def check_balance(self):
#         enter_pin = int(input("Enter your pin"))
#         if (enter_pin == self.pin):
#             print("Account balance:", self.money)
#         else:
#             print('Incorrect PIN, try again...')
        
        
        
#         # print(BankAccount) 
# b1 = BankAccount("Blard", 400, 1234)
# b1.deposit_amt(500)
# b1.check_balance()



# def prime_num():
#     enter_num = int(input("Enter a number"))
#     for enter_num in range(50):
#         if enter_num % 2 == 0:
#             print(f'{enter_num} is not a prime number')
#         else:
#             print(f'{enter_num} is a prime number')
# prime_num()

# def prime_num(num):
#     num = int(input("Enter a number"))
#     if num % 2 == 0:
#         return False
#     else:
#         return True
    
# print(prime_num(10))

# my_grocery = ["mango", "banana", "pear", "chad", "orange"]

# def get_alph(my_grocery):
#     for list in my_grocery:
#         if len(list) < 5:
#             print(list)
# print(get_alph(my_grocery))


# class inheritance 
class NewPerson(Person):
    def __init__(self, fname, lname, country, lang, education):
        self.education = education
        super().__init__(fname, lname, country, lang)
    def info(self):
        return f'I am {self.lname}, I have {self.education} certificate'

p1 = NewPerson("Blard", "Omu", "Netherlands", "English", "PHD")
print(p1.info())

