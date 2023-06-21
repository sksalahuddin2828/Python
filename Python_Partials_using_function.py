#--------------------------Shorter Way------------------------------>

from functools import partial

def multiply(a: float, b: float, name:str | None = None) -> float:
    if name not in None:
        print(f"\n{name} (a: {a}, b: {b})")
    return a * b

double = partial(multiply(2))
triple = partial(multiply(3))

print(double(10))
print(triple(10))


# Answer: 20
#         30

#--------------------------Longer Way------------------------------>

def multiply_setup(a: float):
    def multiply(b: float) -> float:
        return a * b
    return multiply

double = multiply_setup(2)
triple = multiply_setup(3)

print(double(10))
print(triple(10))


# Answer: 20
#         30
