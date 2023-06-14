my = ["This","is","Python","tutorial","from","SK. SALAHUDDIN"]
my_list = [i[0] for i in my]
print(my_list)

# Answer: ['T', 'i', 'P', 't', 'f', 'S']


a = [3, 4, 5]
multiplied = [i*2 for i in a]
print(multiplied)

# Answer: [6, 8, 10]


# Cubes using **kwargs = keyword_arguments

_kwargs = [x**3 for x in range(5)]
print(_kwargs)

# Answer: [0, 1, 8 , 27, 64]

#------------------------------------Start-------------------------------------

letter = list(map(lambda x: x, "Sk. Salahuddin"))
print(letter)

# Answer: ['S', 'k', '.', ' ', 'S', 'a', 'l', 'a', 'h', 'u', 'd', 'd', 'i', 'n']


name = 'Bangladesh'
letter = [i for i in name]
print(letter)

# Answer: ['B', 'a', 'n', 'g', 'l', 'a', 'd', 'e', 's', 'h']


letter = list(map(lambda i: i, "Bangladesh"))
print(letter)

# Answer: ['B', 'a', 'n', 'g', 'l', 'a', 'd', 'e', 's', 'h']

#-------------------------------------End---------------------------------------

# Normal Way:
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list1)
my_list = [i for i in list1 if i % 2]
print(my_list)

# Answer: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Answer: [1, 3, 5, 7, 9]

# Complex Way:
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list1 = list(map(int, list1))
my_list = filter(lambda x: x%2, list1)
print(list(my_list))

# Answer: [1, 3, 5, 7, 9]

# Hardest Way:
from functools import reduce
list1 = [1, 2, 3, 4, 5, 6]
my_list = reduce(lambda x,y: x+y, list1)
print(my_list)

# Answer: 21   Like = 1 + 2 + 3 + 4 + 5 + 6 = 21

# Easiest Way:
list1 = [1, 2, 3, 4, 5, 6]
my_list = sum([i for i in list1])
print(my_list)

# Answer: 21   Like = 1 + 2 + 3 + 4 + 5 + 6 = 21
