def make_taco():
    # Choose the taco type
    taco_type = input("What kind of taco are you making? (e.g., Chicken, Beef, Veggie): ")
    
    # Gather ingredients
def gather_ingredients():
    ingredients = []
    while True:
        ingredient = input("Enter an ingredient (or 'done' to stop): ")
        if ingredient.lower() == 'done':
            break
        ingredients.append(ingredient)
    
    # Assemble and display the taco
def assembly():
    print(f"\nAssembling your {taco_type} taco with the following ingredients:")
    for ingredient in ingredients:
        print(f"- {ingredient}")
    print(f"\nYour {taco_type} taco is ready! Enjoy!")
    
def format_ingredient(ingredient):
    new_ingredient = f"- {ingredient}"
    return new_ingredient

make_taco()
