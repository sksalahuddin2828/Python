import timeit
from memory_profiler import profile

n = 10

@profile
def init_for_loop(n):  
    a = []
    for i in range(n):
        a.append(0)
    return a

@profile
def init_list_comp(n):   
    a = [0 for i in range(n)]
    return a

@profile
def init_mul(n):
    a = [0] * n
    return a

t1 = timeit.timeit(lambda: init_for_loop(n), number=1000)
t2 = timeit.timeit(lambda: init_list_comp(n), number=1000)
t3 = timeit.timeit(lambda: init_mul(n), number=1000)

print(f"t1 = {t1:.3f}, t2 = {t2:.3f}, t3 = {t3:.3f}")
print(f"t1/t2 = {t1 / t2:.2f}")
print(f"t1/t3 = {t1 / t3:.2f}")
