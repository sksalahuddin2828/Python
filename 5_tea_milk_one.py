from itertools import combinations

# Define the list of friends and their ingredient preferences
friends = {
    'Friend 1': ['a', 'b', 'e'],
    'Friend 2': ['b', 'c', 'd'],
    'Friend 3': ['a', 'c', 'd'],
    'Friend 4': ['b', 'c', 'e'],
    'Friend 5': ['a', 'b', 'c']
}

ingredients = ['a', 'b', 'c', 'd', 'e']

MAX_CUPS = 3
MAX_INGREDIENTS_PER_CUP = 3

ingredient_combinations = []
for num_ingredients in range(1, MAX_INGREDIENTS_PER_CUP+1):
    ingredient_combinations += list(combinations(ingredients, num_ingredients))

cups_sold = {}
for combination in ingredient_combinations:
    cups_sold[combination] = 0

for friend, preferences in friends.items():
    for combination in ingredient_combinations:
        if all(ingredient in preferences for ingredient in combination):
            cups_sold[combination] += 1

sorted_combinations = sorted(ingredient_combinations, key=lambda x: cups_sold[x], reverse=True)

best_combinations = []
for combination in sorted_combinations:
    if cups_sold[combination] > 0:
        best_combinations.append(combination)
    if len(best_combinations) == MAX_CUPS:
        break

for i, combination in enumerate(best_combinations):
    print(f"Cup {i+1}: {combination} ({cups_sold[combination]} cups sold)")
