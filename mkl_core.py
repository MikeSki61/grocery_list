"""
mk_core.py
This file is the core file that provides the functions for the app.
It includes the ability to add, remove, edit, and export the list.

Functions are:
- add_items(): Add items to the list.
-remove_items(): Removes items from the list.
-edit_items(): Edits any item within the list. Any value can be edited.
-export_items(): Able to export the list.

Author: Mike Kwiatkowsky
Version:1.0.0
"""
import re
# The grocery_list is a list of items showing the keywords and values of each.
# Also this shows the type of item within the list ex: "name" is a string,
# cost is a float, priority is an integer and buy is a boolean.-True or False.
grocery_list: list[dict[str, float | int | bool | str]] = [
    {
        "name": "milk",
        "store": "Walmart",
        "cost": 6.47,
        "amount": 2,
        "priority": 1,
        "buy": True,
        "date": "Nov",
        "category": "dairy",
    },
    {
        "name": "bread",
        "store": "Wal-Mart",
        "cost": 4.50,
        "amount": 2,
        "priority": 1,
        "buy": True,
        "date": "Nov",
        "category": "dairy",
    },
    {
        "name": "eggs",
        "store": "Wal-Mart",
        "cost": 5.0,
        "amount": 1,
        "priority": 1,
        "buy": True,
        "date": "Nov",
        "category": "dairy",
    },
    {
        "name": "peanut butter",
        "store": "Costco",
        "cost": 12.5,
        "amount": 1,
        "priority": 3,
        "buy": True,
        "date": "Nov",
        "category": "snack",
    },
    {
        "name": "chicken",
        "store": "Costco",
        "cost": 25,
        "amount": 1,
        "priority": 2,
        "buy": True,
        "date": "Nov",
        "category": "poultry",
    },
]


def add_item(
    name: str,
    store: str,
    cost: float,
    amount: int,
    priority: int,
    buy: bool,
    date: str,
    category: str,
):
    """This is a function to add the arguments
    for the addition of an item to the list.

    Args:
        name (str): a string
        store (str): a string
        cost (float): a float
        amount (int): an integer
        priority (int): an integer
        buy (bool): a boolean
        date (str): a string
        category (str): a string
    """

    item = {
        "name": name,
        "store": store,
        "cost": cost,
        "amount": amount,
        "priority": priority,
        "buy": True,
        "date": date,
        "category": category,
    }
    grocery_list.append(item)


# Remove items from the list
def remove_item(name):
    """This is a function to remove items
        from the list as a string.

    Args:
        name (str): string

    Returns:
        str: _return item as a string
    """

    index = get_index_from_name(name)

    grocery_list.pop(index)


# Edit items
def edit_item(
    name: str,
    store: str,
    cost: float,
    amount: int,
    priority: int,
    buy: bool,
    date: str,
    category: str,
):
    """This is  function the allows the user to edit the items in a list.

    Args:
        name (str): _a string
        store (str): _a string
        cost (float): _ a float
        amount (int): _an integer
        priority (int): _an integer_
        buy (bool): _a boolean
        date (str): _a string
        category (str): _a string
    """
    index = get_index_from_name(name)

    item = grocery_list[index]

    if not store:
        store = item["store"]

    if not cost:
        cost = item["cost"]

    if not amount:
        amount = item["amount"]

    if not priority:
        priority = item["priority"]

    if buy == "skip":
        buy = item["buy"]

    if not date:
        date = item["date"]

    if not category:
        category = item["category"]

    item = {
        "name": name,
        "store": store,
        "cost": cost,
        "amount": amount,
        "priority": priority,
        "buy": True,
        "date": date,
        "category": category,
    }

    grocery_list[index] = item

def search_item_name(search_item):
    matching_items = []
    pattern = rf"^{search_item}" 

    for item in grocery_list:
        if re.match(pattern, item["name"], re.IGNORECASE):
            matching_items.append(item)

    return matching_items

def export_items():
    buy_list = []
    """_The export_items() function will export the items that may have
been edited, removed or  added to the list, 
creating a new list called the buy_list.
    """

    for item in grocery_list:  # Iterate over the grocery list.
        if item["buy"]:
            buy_list.append(item)  # If item is found, add to the grocery list.

    if buy_list:
        for item in buy_list:  # Iterates over buy_list
            print(
                f"name: {item['name']} -store: {item['store']} -"
                f"cost: ${item['cost']} -amount: {item['amount']} -"
                f"priority: {item['priority']} -date: {item['date']} -"
                f"category:{item['category']}"
            )

        total_cost = calculate_total_cost(buy_list, round_cost=True, tax=TAX)

        print(f"The total cost is ${total_cost}:")


def get_index_from_name(name):
    index = 0
    """_The get_index_from_name(name) function 
will return the name of the item.

    Returns:
        _name_: _will return a string
    """

    for item in grocery_list:
        if item["name"] == name:  # If item is equal to name, returns the value.
            return index
        else:
            index += 1  # Adds the item increases the count by one.


def list_items() -> str:
    """The list_items() function will list / print the items.

    Returns:
        str: -items as a string
    """
    for item in grocery_list:
        print(item)


        

    # Define a global constant for the default tax rate
TAX = 0.8


def calculate_total_cost(grocery_list: str, round_cost=False, tax=TAX):
    """_Parameters
    grocery_list (list[dict]): A list of dictionaries where each dictionary represents
                            an item with keys 'amount' (int) and 'cost' (float).
    round_cost (bool): If True, rounds the total cost to the nearest integer. Default is False.
    tax (float): The tax rate to apply to the total cost. Default is the global TAX constant.

    Returns:
        _float: The total cost after applying tax and optional rounding.
    """
    total_cost = 0

    # Iterate through each item in the grocery
    # list to calculate total cost
    for item in grocery_list:
        cost = item["amount"] * item["cost"]
        total_cost += cost

    # If rounding is enabled, round the total cost to the nearest integer
    if round_cost:
        total_cost = round(total_cost)

    # If a tax rate is specified, calculate and add tax to the total cos
    if TAX:
        tax_cost = total_cost * TAX
        total_cost += tax_cost

    # Return the final total cost
    return total_cost


export_items()
