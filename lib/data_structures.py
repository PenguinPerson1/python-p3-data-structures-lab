spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return [item["name"] for item in spicy_foods]
    pass

def get_spiciest_foods(spicy_foods):
    return [item for item in spicy_foods if item['heat_level']>5]
    pass

def print_spicy_foods(spicy_foods):
    for item in spicy_foods:
        print(f"{item['name']} ({item['cuisine']}) | Heat Level: {'🌶'*item['heat_level']}")
    pass

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for item in spicy_foods:
        if item['cuisine']==cuisine:
            return item

def print_spiciest_foods(spicy_foods):
    print_spicy_foods(get_spiciest_foods(spicy_foods))

def get_average_heat_level(spicy_foods):
    if len(spicy_foods)==0:
        return 0
    total_heat=0
    for item in spicy_foods:
        total_heat+=item["heat_level"]
    return total_heat/len(spicy_foods)

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods


print(get_spicy_food_by_cuisine(spicy_foods,"American"))