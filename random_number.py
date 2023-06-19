import random as r

nums = [1,2,3,4,5]

# any one elements 'choice' by random
random = r.choice(nums)
print(random)

# any three elements 'choices' by random
random = r.choices(nums, k=3)
print(random)
