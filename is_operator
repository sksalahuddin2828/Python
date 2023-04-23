class Fruit:
  def __init__(self, name, calories):
    self.name = name
    self.calories = calories

  def __eq__(self, other):
    return self.__dict__ == other.__dict__

fruit_a = Fruit("Banana", 10)
fruit_b = Fruit("Banana", 10)
print(f"fruit_a is fruit_b = {fruit_a is fruit_b}")
print(f"fruit_a == fruit_b = {fruit_a == fruit_b}")

#--------------------------------------------------

a = None 
b = None

print(a is b)
# Answwer = True

a = 500
b = 500

print(a is b)
# Answwer = True

a = 500
b = 500

print(a == b)
# Answwer = True

_ = 500
a = 1000
b = 500 + _

print(id(a), id(b))
print(a is b)
# Answwer = False
print(a == b)
# Answwer = True

# What's happning here !

a = 1000
b = 1000

print(f"a: {id(a)}, b: {id(b)}")
print(f"a is b = {a is b}")
print(f"a == b = {a == b}")
print(a, b)

#-------------------------------

a = 100
b = 10_000 / a

print(f"a: {id(a)}, b: {id(b)}")
print(f"a is b = {a is b}")
print(f"a == b = {a == b}")
print(a, b)
