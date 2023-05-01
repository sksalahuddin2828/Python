# Set is faster than List -- wait 1 minutes max you can see this result on your terminal or console 

from timeit import timeit

a_list = list(range(1000000))
a_set = set(range(1000000))

list_time = timeit('999999 in a_list', number=1000, globals=globals())
print(f'List: {list_time:.6} seconds')

set_time = timeit('999999 in a_set', number=1000, globals=globals())
print(f'Set: {list_time:.6f} seconds')

speed_difference = (list_time - set_time) / list_time * 100
print(f'{speed_difference:.3f}% faster')
