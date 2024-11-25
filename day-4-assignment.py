# Exercise 1--Grocery List Categorization

food_items = ["peaches", "apples", "oranges" ]
non_food_items = ["soap", "paper", "detergent"]

item = input("Please enter an item: ")
if item in food_items:
    print("This is is the food item group.")
elif item in non_food_items:
    print("This item is in the non-food item group.")
else:
    print("Unknown Item.")

# Exercise 2--Making a Burger While Loop

items_list = [
    {"name": "fries", "cost":6.25, "amount": 1},
    {"name": "burger patties", "cost":13.50, "amount": 1},
    {"name": "burger buns", "cost":3.50, "amount": 2},
    {"name": "tomato", "cost":1.50, "amount": 2},
    {"name": "lettuce", "cost":5, "amount": 1},
    {"name": "Ketchup", "cost":3.47, "amount": 1},
    {"name": "pickles", "cost":4.25, "amount": 1}] 
shopping_list = []
budget = 27.50
total_cost = 0
index = 0

while total_cost <= budget and index < len(items_list):
    item = items_list[index]
    item_cost = item['cost' ] * item['amount']
    if total_cost + item_cost <= budget:
        shopping_list.append(item['name'])
        total_cost += item_cost
    index += 1
    
print(shopping_list) 


# #EXERCISE 3--Extending Logic with Nesting

items_list = [
    {"name": "fries", "cost":6.25, "amount": 1},
    {"name": "burger patties", "cost":13.50, "amount": 1},
    {"name": "burger buns", "cost":3.50, "amount": 2},
    {"name": "tomato", "cost":1.50, "amount": 2},
    {"name": "lettuce", "cost":5, "amount": 1},
    {"name": "Ketchup", "cost":3.47, "amount": 1},
    {"name": "pickles", "cost":4.25, "amount": 1}]
shopping_list = []
budget = 27.50
total_cost = 0
index = 0 

while total_cost <= budget and index < len(items_list):
    item = items_list[index]
    item_cost = item['cost' ] * item['amount']
    if total_cost + item_cost <= budget:
        shopping_list.append(item['name'])
        total_cost += item_cost
        
    for item_name in shopping_list:
        print(item_name)
    print('-----------')
    index += 1
print(shopping_list)


#EXERCISE 4--Breaking the Loop
items_list = [
    {"name": "fries", "cost":6.25, "amount": 1},
    {"name": "burger patties", "cost":13.50, "amount": 1},
    {"name": "burger buns", "cost":3.50, "amount": 2},
    {"name": "tomato", "cost":1.50, "amount": 2},
    {"name": "lettuce", "cost":5, "amount": 1},
    {"name": "Ketchup", "cost":3.47, "amount": 1},
    {"name": "pickles", "cost":4.25, "amount": 1}]
shopping_list = []
budget = 27.50
total_cost = 0
index = 0

while total_cost <= budget and index < len(items_list):
    item = items_list[index]
    item_cost = item['cost' ] * item['amount']
    if total_cost + item_cost <= budget:
        shopping_list.append(item['name'])
        total_cost += item_cost
        
    for item_name in shopping_list:
        print(item_name)
    print('-----------')
    
    if ('burger buns' in shopping_list and 'fries' in shopping_list and 'burger patties' in shopping_list):
            print(f'We can make burgers and fries for ${total_cost}!')
    
            break

    index += 1
print(shopping_list)


# #EXERCISE 5-- Error Handling with Try-Except
items_list = [
    {"name": "fries", "cost":6.25, "amount": 1},
    {"name": "burger patties", "cost":13.50, "amount": 1},
    {"name": "burger buns", "cost":3.50, "amount": 2},
    {"name": "tomato", "cost":1.50, "amount": 2},
    {"name": "lettuce", "cost":5, "amount": 1},
    {"name": "Ketchup", "cost":3.47, "amount": 1},
    {"name": "pickles", "cost":4.25, "amount": 1}]
shopping_list = []
budget = 27.50
total_cost = 0
index = 0

while total_cost <= budget and index < len(items_list):
    try:
        item = items_list[index]
    except: TypeError
    print('ERROR: The index must be an integer')
    break

print(shopping_list)

#EXERCISE 6 -- Customize Your Script

items_list = [
    {"name": "pasta", "cost":2.00, "amount": 2},
    {"name": "onion", "cost":1.99, "amount": 1},
    {"name": "canned_tomato_sauce", "cost":1.05, "amount": 1},
    {"name": "stewed_tomatoes", "cost":1.35, "amount": 1},
    {"name": "parm_cheese", "cost":4.99, "amount": 1},
    {"name": "garlic_powder", "cost":2.99, "amount": 1}]
shopping_list = []
budget = 27.50
total_cost = 0
index = 0

while total_cost <= budget and index < len(items_list):
    item = items_list[index]
    item_cost = item['cost' ] * item['amount']
    if total_cost + item_cost <= budget:
        shopping_list.append(item['name'])
        total_cost += item_cost
        
    for item_name in shopping_list:
        print(item_name)
    print('-----------')
    
    if ('pasta' in shopping_list and 'onion' in shopping_list and 'canned_tomato_sauce' in shopping_list and    'stewed_tomatoes' and 'parm_cheese' in shopping_list and 'garlic_powder' in shopping_list):
        print(f'We can make pasta sauce for ${total_cost:}!')
        break
    index += 1
print(shopping_list) 
        
    
    
