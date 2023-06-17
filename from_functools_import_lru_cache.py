def increment(num):
    print("Running 1000 line of code")
    return num + 1
    
print(increment(1))
print(increment(2))
print(increment(3))
print(increment(1))


# Answer:  Running 1000 line of code
#          2
#          Running 1000 line of code
#          3
#          Running 1000 line of code
#          4
#          Running 1000 line of code
#          2

#-----------------------------------------------

from functools import lru_cache

@lru_cache
def increment(num):
    print("Running 1000 line of code")
    return num + 1
    
print(increment(1))
print(increment(2))
print(increment(3))
print(increment(1))


# Answer:  Running 1000 line of code
#          2
#          Running 1000 line of code
#          3
#          Running 1000 line of code
#          4
#          2
