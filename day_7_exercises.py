# import math

# def get_square_root(number):
"""
    Calculate and print the square root of a given number.
    Args:
        number (float or int): The number to calculate the square    root of.
    Returns:
        None: This function prints the result directly.
    """

#     square_root =  math.sqrt(number)
#     print(f"the square root of {number} is {square_root: .2f}")

# number = 1028
# get_square_root(number) 

# Exercise 1

#import math

# def calculate_circle_area(radius):
#     """
#     Calculate the area of a circle given its radius.

#     Parameters:
#     radius (float): The radius of the circle. Must be a non-negative number.

#     Returns:
#     float: The area of the circle if the radius is non-negative.
#     str: An error message if the radius is negative.
    
#     Formula:
#     Area = π * radius^2
#     """
#     if radius <  0:
#         return "Radius cannont be negative."
#     area = math.pi *  (radius ** 2)
#     return area

# radius = float(input("Enter the radius of the circle (i.e 2.5): "))
# area = calculate_circle_area(radius)
# print(f"The area of the circle with radius {radius} is: {area: .2f}")

# Exercise 2

# import requests

# def fetch_github_api_data():
#     """
#     Fetches data from the GitHub API and prints the response.

#     This function makes a GET request to the GitHub API and prints the
#     response in text format.
#     """
#     response = requests.get('https://api.github.com')
#     print(response.text)

# fetch_github_api_data()


# Exercise 3

# def factorial(n):
#     """
#     Calculate the factorial of a non-negative integer n.

#     Parameters:
#     n (int): A non-negative integer whose factorial is to be calculated.

#     Returns:
#     int: The factorial of the number n. Returns 1 if n is 0.
    
#     Raises:
#     ValueError: If n is a negative integer.
#     """
#     if n < 0:
#         raise ValueError("Factorial is not defined for negative numbers.")
    
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
    
#     return result

# try:
#     number = int(input("Enter a non-negative integer (i.e. 5): "))
#     print(f"The factorial of {number} is: {factorial(number)}")
# except ValueError as e:
#     print(e)


# Exercise 4

# import math

# def factorial_with_math(n):
#     """
#     Calculate the factorial of a non-negative integer n using the math library.

#     Parameters:
#     n (int): A non-negative integer whose factorial is to be calculated.

#     Returns:
#     int: The factorial of the number n. Returns 1 if n is 0.
    
#     Raises:
#     ValueError: If n is a negative integer.
#     """
#     if n < 0:
#         raise ValueError("Factorial is not defined for negative numbers.")
    
#     return math.factorial(n)

# # Example usage:
# try:
#     number = int(input("Enter a non-negative integer: "))
#     print(f"The factorial of {number} is: {factorial_with_math(number)}")
# except ValueError as e:
#     print(e)


# Generate UUID script
# import uuid

# for i in range(5):
#     unique_id = int(uuid.uuid4())
#     print(unique_id)


# Regex 
# Find all prices in a receipt
#import re


#receipt = "Apples: $2.99, Bananas:  $1.50, Milk: $3.75, Eggs: $4.20"
# pattern = r"\$\d+\.\d{2}"

# prices = re.findall(pattern, receipt)
# print("Prices", prices)

# text = "apples, bananas, milk, bread"
# new_text = re.sub(r",", "\n", text)
# print("Shopping list:\n",  new_text)

# .group()

# match = re.search(r"(\d+)\s(apples)", "I bought 10 apples.")
# print(match.group(0))
# print(match.group(1))
# print(match.group(2))


# import re

# grocery_list = [
#     "some bread",
#     "A Can of Diced Tomatoes",
#     "A can of peas",
#     "An Heirloom Tomato",
#     "1 beefsteak tomato",
#     "A Block Of Cheese",
#     "3 tomatoes on the vine"
# ]

# # Loop through the grocery list and check for matches
# for item in grocery_list:
#     # Use re.match() to check if the item contains "tomato" or "tomatoes"
#     if re.match(r".*\b(tomato|tomatoes)\b.*", item, re.IGNORECASE):
#         print(item)


# import re

# grocery_list = [
#     {"name": "milk", "store": "Walmart"},
#     {"name": "bread", "store": "Walmart"},
#     {"name": "eggs", "store": "Walmart"},
#     {"name": "peanut butter", "store": "Costco"},
#     {"name": "chicken", "store": "Costco"}
# ]

# # The item we are searching for
# search_item = "peanut butter"
# # Loop through the grocery list
# for item in grocery_list:
#     # Use re.search() to check if the item name matches the search item
#     if re.search(search_item, item["name"], re.IGNORECASE):
#         print(item)


# Remove items from Shopping list - resub()
# import re

# grocery_list = [
#     "2kg apples",
#     "5lbs potatoes",
#     "3g salt",
#     "1kg  bananas",
#     "250g rice"
# ]

# updated_list = []

# for item in grocery_list:
#     cleaned_item = re.sub(r"\d+\s?(kg|lbs|g)?", "", item).strip()
#     updated_list.append(cleaned_item)

# print(updated_list)


# Visualizing Data with Matplotlib

# import matplotlib.pyplot as plt
# """
# This was a fun one to work on. I had a small problem it turneed
# out I had put linestyles instead of linestyle. After fixing that 
# I added a couple of features like rotating the grid 45 degrees,
# and made the layout tighter
# """

# months = [
#     "January",
#     "February",
#     "March",
#     "April",
#     "May",
#     "June",
#     "July",
#     "August",
#     "September",
#     "October",
#     "November",
#     "December"
# ]

# prices = [
#     5.50,
#     5.45,
#     5.60,
#     5.80,
#     6.00,
#     6.10,
#     6.20,
#     6.50,
#     6.70,
#     6.90,
#     7.10,
#     7.20
# ]


# plt.plot(months, prices, marker='o', linestyle="-", color='b')
# plt.title("Cost of Olive Oil over the Last Year")
# plt.xlabel("Month")
# plt.ylabel("Price ($/L)")
# plt.grid(True)
# plt.xticks(rotation=45) # rotate month labels for better readability
# plt.tight_layout() # Adjust layout to prevent clipping labels
# plt.show()