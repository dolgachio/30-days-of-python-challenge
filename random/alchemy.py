def check_ingredient_match(recipe, inventory):
    missing = []
    existing_count = 0
    recipe_count = len(recipe)
    
    for ingridient in recipe:
        if ingridient in inventory:
            existing_count += 1
        else:
            missing.append(ingridient)
            
    missing_percentage = existing_count / recipe_count * 100
    
    return missing_percentage, missing

recipe = ["Dragon Scale", "Unicorn Hair", "Phoenix Feather", "Troll Tusk"]
inventory = ["Dragon Scale", "Phoenix Feather", "Troll Tusk"]

percentage, missing_ingredients = check_ingredient_match(recipe, inventory)
print(percentage, missing_ingredients)
# Prints: 75.00 ["Unicorn Hair"]