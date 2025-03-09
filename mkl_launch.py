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
    while True:
        command = input("Enter a command" "(add, remove, edit, list, export, search, quit): ")

        if command == "add":  # This will allow the user to add items.
            print(" Please enter an item to add to the list. ")

        if command == "add":  # This command inputs all the items to add to the ist.
            name, store, cost, amount, priority, buy, date, category = get_inputs()
            mkl_core.add_item(
                name=name,
                store=store,
                cost=cost,
                amount=amount,
                priority=priority,
                buy=buy,
                date=date,
                category=category,
            )
            
            print(f"{name} added to list")
            
        if command == "remove":  # his is the command to remove an item.
            name = input("Name of item to remove: ")
            mkl_core.remove_item(name)
            
            print(f"{name} removed from list.")
            

        if command == "edit":  # This is the command to be used to edit
            # items in the list.
            print("Please enter item to edit: ")

        if command == "edit":  # This command allows the user
            # to edit and keyword or value within the list.
            name, store, cost, amount, priority, buy, date, category = get_inputs()
            mkl_core.edit_item(name, store, cost, amount, priority, buy, date, category)
            
            print(f"{name} was edited.")

        if command == "search":  # his is the command to remove an item.
            item = input("Name of item to search for: ")
            mkl_core.search_item_name(item)
            

        if command == "list":  # This command will list the items
            # selected in the list from the core module.
            mkl_core.list_items()

        if command == "export":
            mkl_core.export_items()

        if command == "search": #This command allows the user to search for an item.
            mkl_core.search_item()
            
        if command == "quit":
            break
        print("You have quit the program.")

# Inputs Functions
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

    while True:  # this input will alert the user that
        # there is no valid entry if the option is skipped.
        category = input("Category to place item in: ")
        if category == "skip":
            category = None
            break
        elif category:
            category = category
            break
        print("Invalid input. Please add a valid category.")

    return name, store, cost, amount, priority, buy, date, category

# Call the function
if __name__ == "__main__":
    launch()
