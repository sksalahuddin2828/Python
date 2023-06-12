ingredients = ['a', 'b', 'c', 'd', 'e']

friend1 = [1, 0, 0, 0, 0]
friend2 = [0, 1, 0, 0, 0]
friend3 = [0, 0, 1, 0, 0]
friend4 = [0, 0, 0, 1, 0]
friend5 = [0, 0, 0, 0, 1]

preferences = [sum(x) for x in zip(friend1, friend2, friend3, friend4, friend5)]

most_popular_index = preferences.index(max(preferences))
most_popular = ingredients[most_popular_index]

print('The most popular ingredient is', most_popular, 'with', preferences[most_popular_index], 'votes.')
