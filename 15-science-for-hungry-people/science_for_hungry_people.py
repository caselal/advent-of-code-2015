"""
Advent of Code - Day 15: Science for Hungry People
"""

from itertools import permutations

# load data file
with open("input.txt", "r") as input:
    puzzle_input = input.read()
    puzzle_input = puzzle_input.splitlines()


def parse_ingredients(input_string):
    ingredient_properties = {}
    ingredient = input_string.split(":")[0]
    properties = input_string.split(": ")[1].split(", ")

    for property in properties:
        ingredient_properties[property.split(" ")[0]] = int(property.split(" ")[1])

    return ingredient, ingredient_properties


total_tsps = 100

###########
# Part One
###########
ingredients = {}
for string in puzzle_input:
    ingredient, properties = parse_ingredients(string)
    ingredients[ingredient] = properties

number_of_ingredients = len(ingredients.keys())
all_tsp_combinations = [
    permutation
    for permutation in permutations(range(total_tsps + 1), number_of_ingredients)
    if sum(permutation) == total_tsps
]

best_total_score = 0
for tsps in all_tsp_combinations:
    recipe_capacity, recipe_durability, recipe_flavor, recipe_texture = 0, 0, 0, 0

    for i, ingredient in enumerate(ingredients.keys()):
        recipe_capacity += ingredients.get(ingredient).get("capacity") * tsps[i]
        recipe_durability += ingredients.get(ingredient).get("durability") * tsps[i]
        recipe_flavor += ingredients.get(ingredient).get("flavor") * tsps[i]
        recipe_texture += ingredients.get(ingredient).get("texture") * tsps[i]

    if (
        recipe_capacity < 0
        or recipe_durability < 0
        or recipe_flavor < 0
        or recipe_texture < 0
    ):
        recipe_total_score = 0
    else:
        recipe_total_score = (
            recipe_capacity * recipe_durability * recipe_flavor * recipe_texture
        )

    best_total_score = max(best_total_score, recipe_total_score)

print(best_total_score)
