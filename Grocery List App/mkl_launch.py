import mkl_core

def launch():
    
    while True:
        command = input("Enter a command (add, remove, edit, list, export, quit): ")
        
        if command =="add":
            print("This is the the command to add items to the list. ex. item name: 'Bread'")
            
        if command == "add":
            name, store, cost, amount, priority, buy, date, category = get_inputs()
            mkl_core.add_item(name=name, store=store, cost=cost, amount=amount, priority=priority, buy=buy, date=date, category = category)
            
        if command =="remove":
            print("This is the the command to remove items from the list.")
            
        if command == "remove":
            name = input("Item name to remove: ")
            mkl_core.remove_item(name)
            
        if command =="edit":
            print("This is the the command to edit items from the list.")    

        if command == "edit":
            name, store, cost, amount, priority, buy, date, category = get_inputs()
            mkl_core.edit_item(name, store, cost, amount, priority, buy, date, category)

        if command =="list":
            print("This is the the command to list all the items in the list.")  
            
        if command == "list":
            mkl_core.list_items()

        if command =="list":
            print("This is the the command to export all the items in the list.")  
            
        if command == "export":
            mkl_core.export_items()
        
        if command =="quit":
            print("This is the the command to quit the program.")  

        if command == "quit":
            break
# Inputs Function      
def get_inputs():
    while True:
        name = input("item name: ")
        if name:
            break
        print("Invalid input. Please enter a valid item")

    while True:
        store = input("Store name: ")
        if store == "skip":
            store = None
            break
        elif store:
            store = store
            break
        print("Invalid input. Please add a valid store name")

    while True:
        try:
            cost = input("item price: ")
            if cost == "skip":
                cost = None
                break
            else:
                cost = float(cost)
                break
        except ValueError:
            print("Invalid input. Please enter a valid price")

    while True:
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

    while True:
        try:
            priority = input("Priority: ")
            if priority == "skip":
                priority = None
                break
            elif 1 <= int(priority) <= 5:
                break
            else:
                print("Priority must be between 1 and 5")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5")

    while True:
        try:
            buy = input("Buy: ")
            if buy.lower() =="true":
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
            
#Added expiration_date/ category
        
    while True:
        try:
            date = input("Date: ")
            if date == "skip":
                date = None
                break
            elif date:
                date = date
                break
            print("Invalid input. Please enter a date.")
        except ValueError:
            print("Invalid input. Please enter a date.")
            
    while True:
        category = input("Category: ")
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

