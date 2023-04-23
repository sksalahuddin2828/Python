# Rediculus output

a: float = 0.1
b: float = 0.2

print(a + b)

# Answer= 0.30000000000000004 

#---------------------------

a: float = 0.1
b: float = 0.2
c: float = 0.3

print((a + b) == c)

# Answer = False why!

#---------------------------

a: float = 0.1
b: float = 0.2
c: float = 0.3

print(a + b == c)

# Answer = a+b 0.30000000000000004 
# c = 0.3

#---------------------------

first: float = 0.1
second: float = 0.2
third: float = 0.3

def compare_floats(a: float, b: float, tol:float) -> bool:
  absolute: float = abs(a - b)
  print(f"{a} - {b} = {a - b}")
  return absolute < tol

print(compare_floats(first + second, third, tol=1e-10))

#---------------------------

first: float = 0.1
second: float = 0.2
third: float = 0.25

def compare_floats(a: float, b: float, tol:float) -> bool:
  absolute: float = abs(a - b)
  print(f"{a} - {b} = {a - b}")
  return absolute < tol

print(compare_floats(first + second, third, tol=0.1))

#------------------------------

import math

first: float = 0.1
second: float = 0.2
third: float = 0.3

print(math.isclose(first + second, third, rel_tol=0.1))
print(math.isclose(first + second, third, rel_tol=1e-10))
print(math.isclose(first + second, third, rel_tol=1e-20))
