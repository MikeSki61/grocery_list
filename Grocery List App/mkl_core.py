grocery_list = [
    {"name": "milk", "store": "Walmart", "cost": 6.47, "amount": 2, "priority": 1, "buy": True, "date": "Nov", "category": "dairy"},
    {"name": "bread", "store": "Wal-Mart", "cost": 4.50, "amount": 2, "priority": 1, "buy": True, "date": "Nov", "category": "dairy"},
    {"name": "eggs", "store": "Wal-Mart", "cost": 5.0, "amount": 1, "priority": 1, "buy": True, "date": "Nov", "category": "dairy"},
    {"name": "peanut butter", "store": "Costco", "cost": 12.5, "amount": 1, "priority": 3, "buy": True, "date": "Nov", "category": "snack"},
    {"name": "chicken", "store": "Costco", "cost": 25, "amount": 1, "priority": 2, "buy": True, "date": "Nov", "category": "poultry"}
]
# Add items to the list
def add_item(name, store, cost, amount, priority, buy, date, category):
    item = {"name": name, "store": store, "cost":cost, "amount":amount, "priority": priority, "buy": True, "date": date, "category": category}
    grocery_list.append(item)
    
# Remove items from the list   
def remove_item(name):
    index = get_index_from_name(name)
    
    grocery_list.pop(index)
    
#Edit items            
def edit_item(name, store, cost, amount, priority, buy, date, category):
    index = get_index_from_name(name)
    
    old_item = grocery_list[index]
    
    item = {"name": name, "store": store, "cost":cost, "amount":amount, "priority": priority, "buy": True, "date": date, "category": category}
    
    if not store:
        store = item["store"]
        
    if not cost:
        cost = item["cost"]
        
    if not amount:
        amount = item["amount"]
        
    if not priority:
        priority = item["priority"]
        
    if not buy:
        buy = item["buy"]
        
    if not date:
        date = item["date"]
        
    if not category:
        date = item["category"]
        
    grocery_list[index] = item
    
def export_items():
    buy_list = []
    
    for item in grocery_list:
        if item["buy"]:
            buy_list.append(item)
            
    if buy_list:
        for item in buy_list:
            print(f"name: {item['name']} - store: {item['store']} -cost: ${item['cost']} -amount: {item['amount']} -priority: {item['priority']} -date: {item['date']} -category:{item["category"]}")
        
        total_cost = calculate_total_cost(buy_list, round_cost = True)
        
        print(f"The total cost is ${total_cost}")

def get_index_from_name(name):
    index = 0
    
    for item in grocery_list:
        if item["name"] == name:
            return index
        else:
            index += 1
    
def list_items():
    for item in grocery_list:
        print(item)
            
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
        
    return total_cost

#export_items() 









