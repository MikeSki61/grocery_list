"""
mk_launch.py
This file is the launch file that imports the functions for the app.
It includes the ability to add, remove, edit, and export the list.

Functions are:
-add_items(): Add items to the list.
-remove_items(): Removes items from the list.
-edit_items(): Edits any item within the list. Any value can be edited.
-export_items(): Able to export the list.

Author: Mike Kwiatkowsky
Version:1.0.0
"""
import mkl_core


def launch():
    print("Welcome to your Grocery Shopping List!")
    """
    Start of the shopping list program.

    """
    
    while True:
        command: str = input(
            "Enter a command" "(add, remove, edit, list, export, search, quit): ").strip().lower()
        
        if command == "add":
            add_command()
        elif command == "remove":
            remove_command()
        elif command == "edit":
            edit_command()
        elif command == "list":
            list_command()
        elif command == "export":
            export_command()
        elif command == "search":
            search_command()
        elif command == "quit":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Unknown command. Please try again.")


def add_command():
    """
    Handles the logic triggered by the add command in command line mode.
    Adds an item to the grocery list.

    """
    name, store, cost, amount, priority, buy, date, category = get_inputs()
    mkl_core.add_item(
        name=name, 
        store=store,
        cost=cost,
        amount=amount,
        priority=priority,
        buy=buy,
        date=date,
        category=category
       
    )
    print(f"{name} was added to the grocery list.")

def remove_command():
    """
    Prompts the user for an item name, searches for matching items,
    and allows the user to select an item to remove.

    """
    name = input("Enter name of item to remove: ")
    matches = mkl_core.search_item_name(name)

    if not matches:
        print(f"There are no items with the name '{name}'.")
        return

    print("Multiple items found:")
    for match_num, item in enumerate(matches, start=1):
        print(f"Item {match_num}, Name: {item['name']}")

    item_num = int(input("Enter the item number you want to remove (i.e. 1): "))
    if 1 <= item_num <= len(matches):
        item_to_remove = matches[item_num - 1] # get the selected item
        mkl_core.remove_item(item_to_remove['name'])  # Remove by name
        print(f"Item '{item_to_remove['name']}' has been removed.")
    else:
        print("Invalid item number.")


def edit_command():
    """
    Prompts the user for an item name, searches for matching items,
    and allows the user to select an item to edit.
    """
    target_item = input("Which item would you like to edit? ")
    matches = mkl_core.search_item_name(target_item)

    if not matches:
        print(f"There are no items with the name '{target_item}'.")
        return

    if len(matches) > 1:
        print("Multiple items found:")
        for match_num, item in enumerate(matches, start=1):
            print(f"Item {match_num}: ID: {item['id']}, Name: {item['name']}")

        item_num = int(input("Enter the item number you want to "\
                             "edit (i.e. 1): "))
        if 1 <= item_num <= len(matches):
            match_item = matches[item_num - 1]
            name, store, cost, amount, priority, buy, date, category = get_inputs()
            mkl_core.edit_item(
                name,
                store,
                cost,
                amount,
                priority,
                buy,
                date
            
            )
            print(f"Item '{match_item['name']}' has been updated.")
        else:
            print("Invalid item number.")
    else:
        match_item = matches[0]
        name, store, cost, amount, priority, buy, date, category = get_inputs()
        mkl_core.edit_item(
            name,
            store,
            cost,
            amount,
            priority,
            buy,
            date,
            category
        
        )
        print(f"Item '{match_item['name']}' has been updated.")


def list_command():
    """
    Lists all current items in the grocery list.

    """
    print("These are the current items in the grocery list:")
    mkl_core.list_items()


def export_command():
    """
    Exports items marked for purchase in the grocery list.
    """
    print("These are the current items in the buy list:")
    mkl_core.list_items()


def search_command():
    """
    Searches for items in the grocery list based on user input.
    """
    search_keyword = input("What is the name of the item you would like to search? ")
    print("Searching for matching items...")
    matches = mkl_core.search_item_name(search_keyword)

    if matches:
        print("These items match your search:")
        for item in matches:
            print(f"Name: {item['name']}, Store: {item['store']}, Cost: {item['cost']:.2f}")
    else:
        print("No items match the provided search keyword.")

        
def get_inputs():

    """The following functions are for the inputs
    to collect information for the list.

        Returns:
            string:  item to be added as a string
    """
    while True:
        name = input("Name of item: ")
        if name:
            break
        print("Invalid input. Please enter a valid item")

    while True:  # this input will alert the user that
        # there is no valid entry if the option is skipped.
        store = input("Store name: ")
        if store == "skip":
            store = None
            break
        elif store:
            store = store
            break
        print("Invalid input. Please add a valid store name")

    while True:  # this input will alert the user that
        # there is no valid entry if the option is skipped.
        try:
            cost = input("Price of item: ")
            if cost == "skip":
                cost = None
                break
            else:
                cost = float(cost)
                break
        except ValueError:
            print("Invalid input. Please enter a valid price")

    while True:  # this input will alert the user that
        # there is no valid entry if the option is skipped.
        try:
            amount = input("Item quantity: ")
            if amount == "skip":
                amount = None
                break
            elif int(amount) > 0:
                amount = int(amount)
                break
            else:
                print("Quantity must be a positive number")
        except ValueError:
            print("Invalid input. Please enter a valid quantity")

    while True:  # this input will alert the user that
        # there is no valid entry if the option is skipped.
        try:
            priority = input("Priority: 1 - 5 of importance:  ")
            if priority == "skip":
                priority = None
                break
            elif 1 <= int(priority) <= 5:
                break
            else:
                print("Priority must be between 1 and 5")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5")

    while True:  # this input will alert the user that
        # there is no valid entry if the option is skipped.
        try:
            buy = input("Buy item, enter true or false: ")
            if buy.lower() == "true":
                buy = True
                break
            elif buy.lower() == "false":
                buy = False
                break
            elif buy == "skip":
                buy = "skip"
                break
            else:
                print("Invalid input. Please enter true or false")
        except ValueError:
            print("Invalid input. Please enter 'true' or 'false'")

    while True:
        try:
            date = input("Date: ")
            if date == "skip":
                date = None
                break
            elif date:
                date = str(date)
                break
        except ValueError:
            print("Invalid input. Please enter a date.")

    while True: 
        try:
            category = input("Category to place item in: ")
            if category == "skip":
                category = None
                break
            elif category:
                category = category
            break
        except ValueError:
            print("Invalid input. Please add a valid category.")

    return name, store, cost, amount, priority, buy, date, category

# Call the function
if __name__ == "__main__":
    launch()
