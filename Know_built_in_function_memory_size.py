import sys

memory = sys.getsizeof(range(100))
memory1 = sys.getsizeof(input(""))
memory2 = sys.getsizeof(print(100))


print(f"Range built-in function in RAM - Memory size = {memory}")
print(f"Input built-in function in RAM - Memory size = {memory1}")
print(f"Print built-in function in RAM - Memory size = {memory2}")
