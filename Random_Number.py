import random

# It's always generate a random number from 0 to 1
num = random.random()
print(num)

# Random Integer short form is randint() generate only 1 one random number (it will be any number between 1 to 20) which you provide in here randint(start number, end number)
num = random.randint(1, 20)
print(num)

# Same like randint() but only 1 one big difference is random.uniform(start number, end number) gives only float number always
num = random.uniform(1, 20)
print(num)

# How many sample numbers from 1 to 100 are in the range which provide a list and give me 15 random numbers from this range number. You can change the value from here
# If you need 15 value from 1 to 100 then write 15
# If you need 10 / 12 / 5 any value from 1 to 100 then write 10 / 12 / 5

num = random.sample(range(1, 100), 10)
print(num)

num = random.sample(range(1, 100), 15)
print(num)

# Rearange all the values
numList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random.shuffle(numList)
print(numList)
# If you choose only one values from this numList variable you can use random.choice(variable name)
print(random.choice(numList))

#----------------------------------------------------------------------------------------------------

import random
num = random.randrange(1, 20)
print(num)


import random
print(random.randrange(1, 20))


import random
l = [10, 20, 30, 40, 50]
lc = random.choice(l)
print(lc)
