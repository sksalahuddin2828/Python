# If you don't understand this total code please watch this --
# List_initialization_Faster_way II

# Here are 3 three different way to initialize Python list for specific values which one is faster way

# Option No. 1 -- Total Time = 0.7 mili seconds

n = 10
a = []

def init_for_loop(n):  
    for i in range(n):
        a.append(0)
    return 0

init_for_loop(n)
print(a)

#-------------------------------------------------------------------

# Option No. 2 -- Total Time = 0.5 mili seconds

n = 10
a = [0 for i in range(n)]

def init_list_comp(n):   
    return a

init_list_comp(n)
print(a)

#-------------------------------------------------------------------

# Option No. 3 -- Total Time = 0.4 micro seconds
# This is faster way

n = 10
a = [0] * n

def init_mul(n):
    return a

init_mul(n)
print(a)

#-------------------------------------------------------------------

# How to calculate it write down to this code but must install a library or module
# pip install timeit

import timeit

t1 = timeit.timeit(lambda: init_for_loop(n), number=1000)
t2 = timeit.timeit(lambda: init_list_comp(n), number=1000)
t3 = timeit.timeit(lambda: init_mul(n), number=1000)

print(f"t1 = {t1:.3f}, t2 = {t2:.3f}, t3 = {t3:.3f}")
print(f"t1/t2 = {t1 / t2:.2f}")
print(f"t1/t3 = {t1 / t3:.2f}")
