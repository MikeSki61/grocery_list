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



    


    


    






         
 
 









