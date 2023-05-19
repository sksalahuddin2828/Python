from timeit import timeit 

my_list = list(range(100000))
my_set = set(range(100000))

# Measure time for list membership check
list_time = timeit(stmt='99999 in my_list', number=1000, globals=globals())

print(f"List: {list_time:.6f} seconds")

# Measure time for set membership check
set_time = timeit(stmt='99999 in my_set', number=1000, globals=globals())

print(f"Set: {set_time:.6f} seconds")

# Speed Difference between Set and List
speed_difference = (list_time - set_time) / list_time * 100 

print(f"{speed_difference:.3f}% faster.")

