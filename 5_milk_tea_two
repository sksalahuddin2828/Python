friends = ['Friend 1', 'Friend 2', 'Friend 3', 'Friend 4', 'Friend 5']
preferences = {
    'Friend 1': ['a', 'b', 'd'],
    'Friend 2': ['a', 'c', 'e'],
    'Friend 3': ['b', 'c', 'd'],
    'Friend 4': ['a', 'b', 'c'],
    'Friend 5': ['d', 'e']
}

ingredients = ['a', 'b', 'c', 'd', 'e']
combos = []
for i in range(len(ingredients)):
    for j in range(i+1, len(ingredients)):
        for k in range(j+1, len(ingredients)):
            combos.append([ingredients[i], ingredients[j], ingredients[k]])

counts = {}
for combo in combos:
    counts[tuple(combo)] = 0

for i in range(4):
    max_count = -1
    max_combo = None
    for combo in combos:
        count = 0
        for friend, prefs in preferences.items():
            if all(ingredient in prefs for ingredient in combo):
                count += 1
        counts[tuple(combo)] += count
        if counts[tuple(combo)] > max_count:
            max_count = counts[tuple(combo)]
            max_combo = combo
    print(f"Friend {i+1} wants {max_combo}")
    for friend, prefs in preferences.items():
        if all(ingredient in prefs for ingredient in max_combo):
            print(f"{friend} will have {max_combo}")
            preferences[friend].remove(max_combo[0])
            preferences[friend].remove(max_combo[1])
            preferences[friend].remove(max_combo[2])
