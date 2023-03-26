import random

ingredients = ['a', 'b', 'c', 'd', 'e']

friend1 = random.choice(ingredients)
friend2 = random.choice(ingredients)
friend3 = random.choice(ingredients)
friend4 = random.choice(ingredients)
friend5 = random.choice(ingredients)

preferences = [friend1, friend2, friend3, friend4, friend5]

count_a = preferences.count('a')
count_b = preferences.count('b')
count_c = preferences.count('c')
count_d = preferences.count('d')
count_e = preferences.count('e')

counts = {'a': count_a, 'b': count_b, 'c': count_c, 'd': count_d, 'e': count_e}
most_popular = max(counts, key=counts.get)

print('Friend 1 prefers', friend1)
print('Friend 2 prefers', friend2)
print('Friend 3 prefers', friend3)
print('Friend 4 prefers', friend4)
print('Friend 5 prefers', friend5)
print('The most popular ingredient is', most_popular, 'with', counts[most_popular], 'votes.')
