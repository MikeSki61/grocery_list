# Day 3 Practice Exercises

# Lists
""" my_list = [1, 'apple', 3.5]
print(my_list)  """

# Indexing
""" my_list = [1, 'apple', 3.5]
print(my_list[0] )  """

# Slicing
""" my_list = [1, 'apple', 3.5]
print(my_list[1:3]) """

# Adding
""" my_list = [1, 'apple', 3.5]
print(my_list)
my_list.append('banana')
print(my_list) """

# Removing
""" my_list = [1, 'apple', 3.5]
my_list.remove('apple')
print(my_list) """

# Sorting
""" my_list = [5, 9, 3, 11]
my_list.sort()
print(my_list) """

# Other Methods
""" .extend(list_a = [1, 'apple', 3.5]
list_b = ['banana', 'tomato'][new_list])
.insert(index, item): 
my_list = [1, 'apple', 3.5]
my_list.insert(1, 'banana')    """ 

# Tuples
#Key Operations
""" my_tuple = (10, 20, 'orange')
print(my_tuple) """

# Indexing
""" my_tuple = (10, 20, 'orange')
my_tuple[0] """

# Slicing
""" my_tuple = (10, 20, 'orange')
my_tuple[0:2] """

# Length
""" my_tuple = (10, 20, 'orange')
len(my_tuple) """

# Concatenation
""" my_tuple = (10, 20, 'orange')
my_tuple + (30, 40)
print(my_tuple) """

# Practice Exercises

# List Manipulation--add/remove items
""" movies = ["Inception", "Avatar", "Matrix", "Toy Story", "The Godfather"] 
movies.append("Rocky") # add rocky
print(movies)
movies.remove("Avatar") # remove 2nd item
print(movies) """

# Indexing and Slicing
""" numbers = [10, 20, 30, 40, 50] # retrieve last 2 numbers
print(numbers[3:]) """

# Inserting Items
""" colors = ["red", "blue", "green"]
colors.insert(1, "yellow")
print(colors)
colors.append("purple")
print(colors) """

# Tuples 

# Creating and Indexing Tuples
""" dimensions = (10, 5, 15)
print(dimensions[1])
"""
# Slicing
""" numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8)
print(numbers[2:6]) # slice 2-5 
"""

# Concatenating
""" fruits = ('apple', 'banana')
vegetables = ('carrot', 'lettuce')
groceries = fruits + vegetables
print(groceries) """

# DICTIONARIES
""" my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
print(my_dict)

#Accessing Values
print(my_dict["name"]) """

# Adding/Updating Values
""" my_dict = {'name': 'John', 'age': 25}
print(my_dict)
my_dict["city"] = "New York"
my_dict['age'] = 26
print(my_dict) """

# Removing Values
""" my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
my_dict.pop('age')
print(my_dict) """

# Useful Methods
# Get All Keys
""" my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
print(my_dict.keys())
# Get all Values
print(my_dict.values())
# Get all key-value pairs
print(my_dict.items()) """

# Practice Exercises
# Accessing Values
""" book = {'title': '1984', 'author': 'George Orwell', 'year': 1949}
print(book['author'])
"""
# Adding/Updating
""" profile = {"name": "Alice", "age": 30, "city": "Paris"}
print(profile)
profile["city"] = "London"
print(profile)
"""

# Removing/Retrieving
""" student = {'name': 'Emma', 'grade': 'A', 'subject': 'Math'}
print(student.pop("subject"))
print(student)
print(student.keys())
print(student.values()) """

#SETS

""" my_set = {'apple', 'banana', 'cherry'}
print(my_set) """

#Adding Elements
""" my_set = {'apple', 'banana', 'cherry'}
my_set.add("orange")
print(my_set) """

# Removing Elements
""" my_set = {'apple', 'banana', 'cherry'}
my_set.remove("banana")
print(my_set) """

# Set Operations

# Union
""" set1 = {'apple', 'banana'}
set2 = {'banana', 'orange'}
print(set1.union(set2)) """


# Intersection
""" set1 = {'apple', 'banana'}
set2 = {'banana', 'orange'}
print(set1.intersection(set2))
"""

# Difference
""" set1 = {'apple', 'banana', 'cherry'}
set2 = {'banana', 'orange'}
print(set1.difference(set2)) """

# Practice Exercises
# Add/Remove
""" fruits = {'apple', 'banana', 'cherry'}
fruits.add("orange")
print(fruits)
fruits.remove("banana")
print(fruits) """

# Union/Intersection
# Union
""" set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
print(set_a.union(set_b)) """

# Intersection
# print(set_a.intersection(set_b)) 


# Difference
""" set_x = {'cat', 'dog', 'fish'} 
set_y = {'dog', 'bird'} """

#day-4-control-structures
""" print(set_x.difference(set_y))  """

# day-4-control-structures
# print(set_x.difference(set_y))

# Day 4 Practice
# Conditional Statements
# Syntax
# if first_condition:
    # Code to execute if first condition is true
#elif second_condition:
    # Code to execute if first_condition is false but   
#second_condition is true
#elif third_condition:
    # Code to execute if first_condition and second_condition 
#are false but third_condition is true
#else: """
    # Code to execute if none of the conditions are true 
    
# Key Operations 
# IF Statement Runs code if a condition is true 
""" price = 20
if price < 30:
    print("This is affordable.") """

# ELIF Statement: Adds an additional condition if the first IF is false
""" price = 35
if price < 30:
    # This will be skipped because price is more than 30
    print("This is affordable.")
elif price < 40:
    # It will run this code here instead
    print("This is a bit expensive.")  """
    
# ELIF Statement Runs if none of the IF or ELIF conditions are met.
""" price = 50
if price < 30:
    # This will be skipped because price is more than 30
    print("This is affordable.")
elif price < 40:
    # This will also be skipped because price is more than 40
    print("This is a bit expensive.")
else:
    # It will run this code here instead
    print("This is too expensive.")
"""
# Nested Conditionals
""" if first_conditional:
    if nested_conditional: # Indented from the first conditional
        print(“I satisfy the nested conditional”)  """
        
# Full Example
weather = "sunny"
temperature = 75
""" print(set_x.diff(set_y))  """



# Day 3 Assignment

# Exercise 1: Creating a Grocery List with Tuples
""" grapes = ("grapes", 1.00, 10)
apples = ("apples", 2.00, 5)
pears = ("pears", 1.50, 2) """

""" grocery_list = []
grocery_list.append(grapes)
grocery_list.append(apples)
grocery_list.append(pears)
print(grocery_list) """

""" total_cost_grapes = 1.00 * 10
print(f'Total cost of grapes: ${total_cost_grapes: }')
total_cost_apples = 2.00 * 5
print(f'Total cost of apples: ${total_cost_apples: }')
total_cost_pears = 1.50 * 2
print(f'Total cost of pears: ${total_cost_pears: }') """

# Exercise 2: Working with Dictionaries
""" # apple_dict = {'name': 'apple', 'price': .90, 'quantity': 10}
# lettuce_dict = {'name': 'lettuce', 'price': 1.99, 'quantity': 20}
# bagel_dict = {'name': 'bagel', 'price': 2.25, 'quantity': 20} """

""" # apple_dict['total_cost'] = apple_dict['price'] * apple_dict['quantity']
# print(f'The total cost of the apples: ${apple_dict['total_cost']:}')
# lettuce_dict['total_cost'] = lettuce_dict['price'] * lettuce_dict['quantity']
# print(f'The total cost of lettuce: ${lettuce_dict['total_cost']:}') """

""" # bagel_dict['total_cost'] = bagel_dict['price'] * bagel_dict['quantity']
# print(f'The total cost of bagels: ${bagel_dict['total_cost']:}') """

""" # Exercise 3: Slicing and Sorting a List
# num_list = [16, 47, 1, 3, 5, 9, 15, 2]
# print(num_list[2:])
# print(num_list[:4])
# print(num_list[-3])
# num_list.sort(reverse=True)
# print(num_list)
# print(len(num_list))
"""
#Exercise 4: Sets Operations
""" #dairy_products = {'milk', 'butter', 'cream', 'yogurt', 'cheese'}
# desserts = {'jello', 'chocolate', 'candy', 'cookies', 'muffins'} """

""" # dairy_products.add('ice_cream')
# print(dairy_products) """

# desserts.add('ice_cream')
# print(desserts)

""" dairy_products.remove('milk')
print(dairy_products) """
""" desserts.remove('jello') """
#print(desserts)

#print(dairy_products.intersection(desserts))

# conditional 1: Check if the weather is sunny or not
"""if weather == "sunny":
    # conditional 2: if sunny, check if temperature is above 70
    if temperature > 70:
        print("Wear sunglasses and a t-shirt.")
    else: # matching else statement for conditional 2
        print("Wear sunglasses and a light jacket.")
else: # matching else statement for conditional 1
    print("Bring an umbrella.") """
    
# Day 4 Practice Exercises

# 1.Check if number is even or odd
""" number = int(input("Give me a number:"))
if number % 2 == 0:
    print("Even")
else:
    print("Odd") """
    
# 2. Temperature
""" temp = int(input("What is the temperature in Celsius or Fahrenheit: "))
if temp < 15:
    print("Cold")
elif temp in range(15, 25):
    print("Warm")
else:
    print("Hot") """
    
# 3.Nested Conditionals   
""" age = int(input("What is your age:? "))
citizenship = input("Are you a citizen? (yes/no): ").lower()
if age >= 18:
    print("You are old enough to vote")
    if  citizenship == "yes":
        print("You are eligible to vote.")
    else: 
        print("Not eligible: Must bea citizen.")
else:
    print("Not eligible: Must be 18 or older.")   """     
    
# Loops/While--For
# Syntax for loops
""" for item in sequence:  """ 
# Code to execute for each item

# Syntax for while loops
""" while condition:  """
# Code to execute as long as condition is true

# Key Operations

# For Loop: Used for iterating over lists, strings, or other iterable sequences.
""" items = ["apple", "banana", "cherry"]
for item in items:
    print(item) """
    
# While Loop: Used when you don’t know the number of repetitions in advance.
""" count = 0 
while count < 5:
    print("Counting:", count)
    count += 1  """
    
# Nested Loops
# a loop placed inside another loop, allowing complex, repeated actions within each iteration of the outer loop.
# each nested loop should be indented to clearly distinguish it from the outer loop
#for outer_item in outer_sequence:
    #for inner_item in inner_sequence:  # Indented to show it's nested
        #print("This is a nested loop example.")
        
# Full example:
""" shape_list = ["circle", "square", "triangle"]
color_list = ["red", "yellow", "green"] """

# Outer loop: Iterate over each shape
""" for shape in shape_list: """
    # Inner loop: Iterate over each color
    # for color in colors:
        # print(f"{shape} is {color}") """

#RESULT:
""" circle is red
circle is yellow
circle is green
square is red
square is yellow
square is green
triangle is red
triangle is yellow
triangle is green
"""
# Practice Exercise
# Basic for Loop: Create a for loop that prints each item in a list of groceries.
""" grocery_list = ["fruits", "bread", "soda", "milk"]
for i in grocery_list:
    print(i) """
    
# While Loop with User Input: Write a program that lets the user add items to a grocery list # until they type "done."
""" grocery_list = ["fruits", "bread", "soda", "milk"]
while True:
    user_input = input("Type a command add or done: ")
    if user_input == "done":
        break
    name = input("Enter an item name: ")
    amount = int(input("Enter amount: "))
    cost = float(input("Enter cost: "))
    store = input("Enter store name: ")
    new_item_dict = {"name": name, "amount": amount, "cost": cost, "store": store}
    grocery_list.append(new_item_dict)
    print(f"{"name"} was added to the grocery list.")
    print(grocery_list)

for item in grocery_list:
        print(item) 
print(grocery_list)
print(grocery_list) 

items = ['bread', 'peanuts', 'milk', 'butter']
for item in items:
    print(item)      
    
grocery_list = []

grocery_list = {'apples': {'price': 1.50, 'quantity': 4},'bread': {'price': 2.50, 'quantity': 3},'ice cream': {'price': 3.00,
'quantity': 2}}
for item, details in grocery_list.items():
     total_cost = details['price'] * details['quantity']
print(f'{item}: ${total_cost: }')   """


# Loop Control 

# Break Stops when a condition is met
""" for item in ["apple", "banana", "cherry", "mango"]:
    if item == "banana":
        break
print("{item} is yellow.")
"""
# Output: 
# banana is yellow.

# Continue--Skips the current loop iteration
""" yellow_fruits = ["banana", "mango"]
red_fruits = []

for item in ["apple", "banana", "cherry", "mango"]:
    if item in yellow_fruits:
        continue
    red_fruits.append(item)
print(red_fruits) """

# Output:
['apple', 'cherry']

# Pass--acts as a placeholder allowing the loop to continue without action
""" for item in ["apple", "banana", "cherry", "mango"]:
    if item == "banana":
        pass  # Does nothing
    print(item) """


""" grocery_list = ["milk", "bread", "eggs", "cheese","bananas"]
item_to_find = "tea"
for item in grocery_list:
    if item == item_to_find:
        print(f"Found {item_to_find}!")
        break
else:
    print(f"{item_to_find} not found in the grocery list.")
    
fruits = ["apples", "bananas"]

for item in grocery_list:
    if item in fruits:
        pass
    else:
    
        print(f"Non-fruit item: {item}")
"""
# Exercises---Break ---Continue---Pass
# Break
""" for item in  ["milk", "butter", "eggs"]:
    if item == "milk":
        break
print(f"{item} is found!.")
"""
# Continue
""" grocery_list = ["milk", "bread", "eggs", "cheese","bananas"]
fruits = ["apples", "bananas"]

for item in grocery_list:
    if item in fruits:
        continue
    else:
    
        print(f"Non-fruit item: {item}") """
        
# Pass
""" grocery_list = ["milk", "bread", "eggs", "cheese","bananas"]
fruits = ["apples", "bananas"]

for item in grocery_list:
    if item in fruits:
        pass
    else:
    
        print(f"Non-fruit item: {item}") """
        
# Errors/Tracebacks
# Try
# try:
    # Code to try
#except ErrorType:
    # Code to execute if error occurs
""" try:
    result = 10 / 0
except ZeroDivisionError:
    print("You can't divide by zero!")   """

""" try:
    # some code that may cause an error
except (TypeError, ValueError) as e:
    print(f"An error occurred: {e}")
"""
""" Traceback (most recent call last):
File "example.py", line 6, in <module>
    result = divide_numbers(10, 0)
File "example.py", line 2, in divide_numbers
    return a / b
ZeroDivisionError: division by zero """

""" count = 0
while count < 5:
    print(count)
    count += 1  # Ensures the loop will end """
    
""" number =int(input("Please enter a number: "))
if number <= 5:
        print(f"The number is {number}.")
try:
    print("You have not entered a number.")
"""

# Day 5 -- Functions and Modules
""" def my_first_function():
    print("This is a function")
    
my_first_function() """

"""  def :every function begins with this keyword
    function name :what you want to call the function ‘my_function_to_add’
    parenthesis () :this is where parameters live
    parameters  :variables that can be used as inputs of the function
    colon : marks the end of your function definition.  
    Indentation :the actual code block running the logic should be indented """ 
    
""" def print_something():
    print("Look,I'm printing something!")
        
print_something() """


# Day 5 --Functions and Modules
# Calling a Function
# Call (or "run") the function by typing its name followed by parentheses.
# ex: name of function()

# Practice Exercises:

# Display a message: 
def message():
    print("Welcome to this course.")
message()

# Print your favorite food:
def fav_food():
    print("My favorite food is Italian.")
fav_food()

# Show sum of numbers:
def show_sum():
    print(5 + 10)
    
show_sum()

# Parameters and Return Functions
# Parameters

grocery_list_a = [{"name": "pasta", "cost":2.00, "amount": 2},
                {"name": "onion", "cost":1.99, "amount": 1},
                {"name": "stewed_tomatoes", "cost":1.35, "amount": 1}
]

grocery_list_b = [
    {"name": "bread", "cost": 3.75, "amount": 1},
    {"name": "milk", "cost": 6.50, "amount": 1,},
    {"name": "strawberries", "cost": 10.25, "amount": 1}
]
def calculate_total_cost(grocery_list, round_cost = False, tax = 0.8):
    total_cost = 0

    for item in grocery_list:
        cost = item["amount"] * item["cost"]
        total_cost += cost
        
    if round_cost:
        total_cost = round(total_cost)
        
    if tax:
        tax_cost = total_cost * tax
        total_cost += tax_cost
        
    # print(f"The total cost is ${total_cost}")
    return total_cost

    
grocery_list_a_cost = calculate_total_cost(grocery_list = grocery_list_a)
grocery_list_b_cost = calculate_total_cost(grocery_list = grocery_list_b, round_cost = False)

print(f"This is the value of grocery list a ${grocery_list_a_cost}")
print(f"This is the value of grocery list b ${grocery_list_b_cost}")
combined_value = grocery_list_a_cost + grocery_list_b_cost 
print(f"The total value of list a and list b is :{combined_value}") 

# Day 5 Practice Exercises--Parameters and Return Values

# def print_grocery_list_items(grocery_list):  # Step 1--Define the Function
    #print(grocery_list) # Step 2-- Code Block, what code needs to run to accomplish the task

# Test 1:  
def print_grocery_list_items (grocery_list):
    print(grocery_list)
    
fruits_grocery_list = ['apple', 'banana', 'grapes']
veggie_list = ['kale', 'eggplant', 'spinach', 'broccoli']
misc_items = ['shampoo', 'dish-soap', 'sponges']  
# Test Lists:

print_grocery_list_items(fruits_grocery_list)
# Test 2:
print_grocery_list_items(veggie_list)
# Test 3
print_grocery_list_items(misc_items) 

# Improve the Function

def print_grocery_list_items(grocery_list):
    print("We need to buy the following: ") # Be more explicit 
    for item in grocery_list:
        print(item)  # print each item one at a time

# Call the function using fruits_grocery_list
print_grocery_list_items(fruits_grocery_list)


def print_grocery_list_items(grocery_list, nice_to_have_list=None):
    if nice_to_have_list != None:  # != means 'not equal to' 
        print("If possible, it would be nice to buy the following as well:")
    for item in nice_to_have_list:
        print(item)


# Testing the optional parameter
def print_grocery_list_items(grocery_list, nice_to_have_list=None):
    print("We need to buy the following: ")
    for item in grocery_list:
        print(item) 

    if nice_to_have_list:
        # ‘\n’ means new line. So this will add a blank line
        print("\nIf possible, it would be nice to buy the following as well:")
        for item in nice_to_have_list:
            print(item)
#Test List
desserts_list = ['tiramisu', 'ice cream', 'candy bar']
fruits_grocery_list = ['apple', 'banana', 'grapes']
# Call the function WITHOUT the optional parameter
print_grocery_list_items(fruits_grocery_list)
print_grocery_list_items(fruits_grocery_list, nice_to_have_list=desserts_list)


#Availability Function
def check_availability(item_name, stock_status):
    if stock_status:
        print(f"{item_name} is available.")
    else:
        print(f"{item_name} is out of stock.")
        
check_availability("Bananas", True)   
# Output: Bananas is available.

check_availability("Milk", False)   
# Output: Milk is out of stock.

def check_availability_in_store(item_name, stock_status, store_name):
    if stock_status:
        print(f"{item_name} are available at {store_name}")
    else:
        print(f"{item_name} are out of stock at {store_name}")
        
check_availability_in_store("Apples", True, "SuperMart") 
check_availability_in_store("Eggs", False, "Fresh Foods")  

#Freshness of a product.
def check_freshness(item_name, days_since_purchase):
    if days_since_purchase < 3:
        return f"{item_name} is fresh."
    else:
        return f"{item_name} might be past its prime."

message = check_freshness("Lettuce", 2)
print(message)      
print(check_freshness("Tomatoes", 7)) 

# Practice Exercises
# Grocery Item Search


def find_item(item_name, is_available):
    if is_available:
        print(f"{item_name} is available.")
    else:
        print(f"{item_name} is not available.")

find_item("Orange Juice", True)    
find_item("Bread", False)  

# Favorite Snack 
def favorite_snack(snack_name, quantity_left):
    if quantity_left:
        return(f"You have some {snack_name} left to enjoy")
    else:
        return(f"You're out of {snack_name}.")
        
print(favorite_snack("Chips", 3))   
print(favorite_snack("Cookies", 0))       

def item_location(item_name, store_section):
    if store_section:
        return(f"Find {item_name} in the {store_section}.")
    else:
        return(f"Find {item_name} in the {store_section}.")
    
print(item_location("Milk", "Dairy Aisle"))
print(item_location("Apples", "Produce Section")) 

# Scope Of Variables

#message = "I love chocolate!" # Global
def chocolate():
    message = "I love chocolate!" # Local
    print(message)

# test inside a function
chocolate()
#I love chocolate!  # output

# test outside a function
print(message)
#I love chocolate!  # output """

# LifeTime of Variables
def greet():
    name = "Skyler"
    print(f"Hello, {name}!")

# test inside a function
#greet()
#Hello, Skyler!   # output

# test outside a function
#print(name)        
#Error: NameError - name is not defined  # Errors out """

# Practice Exercises--Scope

food = "Pasta"
def favorite_food():
    food = "Soup"
    print("Local Food", food) # local var

favorite_food()
print("Global food:", food) # global var """
    
    
def counter():
    count = 0
    count += 1
    print("Count", count)
    
counter()
counter()
    
user_name = "Mike"   # Global variable

def change_name():
    user_name = "Tommy"  # Local variable
    print("Inside function:", user_name)

change_name()                         # Prints: Inside function: 
print("Outside function:", user_name) # Prints: Outside function:  """

# Modules--
# Create and Import Modules
import math # Built in Module
print(math.sqrt(16))

import random
print(random.randint(1, 10))  # Prints a random number between 1 and 10 """

from math import pi, sqrt

print(pi)
3.141592653589793   # output

print(sqrt(25))
5.0   # output

import numpy as np
array = np.array([1, 2, 3])  # we use alias np instead of numpy
print(array)
#[1 2 3]   output 

# Creating and Importing Modules
# Special Module Concepts


# Step 1: Create a file called greetings.py with the following content:
def say_hello(name):
    return f"Hello, {name}!"

# Step 2: Now, in another file, in the same directory, import and use the custom module:
#import greetings
#print(greetings.say_hello("Skyler!"))   
#Hello, Skyler!  # output

# How to import Modules
# Import Entire Modules
import random
print((random.randint(1,20)))


#Import Special Functions or Variables
from math import pi, sqrt

print(pi)
3.141592653589793   # output

print(sqrt(25))
5.0   # output

# Using Aliases
import numpy 
array = numpy.array([1, 2, 3])  # we use alias np instead of numpy
print(array)
#[1 2 3]   # output

# Creating and Importing Modules

# To create your own modules, you simply write Python code in a separate file and then import it.
#Creating Module A:
#Step 1: Create a new file called module_a.py. 
#Write a simple function inside module_a.py named ‘welcome’:
def welcome():
    print("Welcome to Module A!")
    
# Special Module Concepts
#c See Example in example.py file>>>

# Practice Exercises
#Exercise 1: Create a Custom Module: 
#Follow the instructions above and create module_a.py and module_b.py. Try running the commands mentioned on your own. Add functions in module_a and try calling them in module_b.

# Exercise 2: Import Specific Functions
#From the datetime module, import the date class and print today’s date.

from datetime import date
print(date.today())











    






         
 
 









