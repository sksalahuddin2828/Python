a = [[1,2],[3,4]]
b = a.copy()

b[0] = 'A'
b[0][0] = 911

print(f"{a = }")
print(f"{b = }")

#----------------

from copy import deepcopy
a = [[1,2],[3,4]]
b = deepcopy(a)

b[0][0] = 'A'

print(f"{a = }")
print(f"{b = }")
