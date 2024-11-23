# Day 3 Practice Exercises

# Lists
""" my_list = [1, 'apple', 3.5]
print(my_list) """

# Indexing
""" my_list = [1, 'apple', 3.5]
print(my_list[0] ) """

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
""" print(set_a.intersection(set_b)) """


# Difference
""" set_x = {'cat', 'dog', 'fish'} 
set_y = {'dog', 'bird'}
print(set_x.diff(set_y)) """



# Day 3 Assignment

# Exercise 1: Creating a Grocery List with Tuples
grapes = ("grapes", 1.00, 10)
apples = ("apples", 2.00, 5)
pears = ("pears", 1.50, 2)

grocery_list = []
grocery_list.append(grapes)
grocery_list.append(apples)
grocery_list.append(pears)
print(grocery_list)

total_cost_grapes = 1.00 * 10
print(f'Total cost of grapes: ${total_cost_grapes: }')
total_cost_apples = 2.00 * 5
print(f'Total cost of apples: ${total_cost_apples: }')
total_cost_pears = 1.50 * 2
print(f'Total cost of pears: ${total_cost_pears: }')

# Exercise 2: Working with Dictionaries

apple_dict = {'name': 'apple', 'price': .90, 'quantity': 10}
lettuce_dict = {'name': 'lettuce', 'price': 1.99, 'quantity': 20}
bagel_dict = {'name': 'bagel', 'price': 2.25, 'quantity': 20}

apple_dict['total_cost'] = apple_dict['price'] * apple_dict['quantity']
print(f'The total cost of the apples: ${apple_dict['total_cost']:}')

lettuce_dict['total_cost'] = lettuce_dict['price'] * lettuce_dict['quantity']
print(f'The total cost of lettuce: ${lettuce_dict['total_cost']:}')

bagel_dict['total_cost'] = bagel_dict['price'] * bagel_dict['quantity']
print(f'The total cost of bagels: ${bagel_dict['total_cost']:}')

# Exercise 3: Slicing and Sorting a List
num_list = [16, 47, 1, 3, 5, 9, 15, 2]
print(num_list[2:])
print(num_list[:4])
print(num_list[-3])
num_list.sort(reverse=True)
print(num_list)
print(len(num_list))

#Exercise 4: Sets Operations
dairy_products = {'milk', 'butter', 'cream', 'yogurt', 'cheese'}
desserts = {'jello', 'chocolate', 'candy', 'cookies', 'muffins'}

dairy_products.add('ice_cream')
print(dairy_products)

desserts.add('ice_cream')
print(desserts)

dairy_products.remove('milk')
print(dairy_products)

desserts.remove('jello')
print(desserts)

print(dairy_products.intersection(desserts))














