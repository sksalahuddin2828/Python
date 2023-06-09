print(enumerate(['A', 'B', 'C']))

# Answer: <enumerate object at 0x7f7b7f7c8c20>


print(list(enumerate(['A', 'B', 'C'])))

# Answer: [(0, 'A'), (1, 'B'), (2, 'C')]

#-------------------------------------------------------------------------------------------------------------------------------------------

for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

# Answer: 0 A
#         1 B
#         2 C


for i, value in enumerate(['A', 'B', 'C'], start=1):
    print(i, value)

# Answer: 1 A
#         2 B
#         3 C

#-----------------------------------------------------Using timeit to calculate time--------------------------------------------------------

from timeit import timeit

def enumerate_func(values: list) -> list:
    temp_list: list = []
    for i, value in enumerate(values, start=1):
        temp_list.append((i, value))

    return temp_list

def normal_func(values: list) -> list:
    temp_list: list = []
    for i, value in enumerate(values):
        temp_list.append((i + 1, value))

    return temp_list

if __name__ == '__main__':
    fifty_numbers: list[int] = list(range(50))

    normal_time: float = timeit(f'normal_func({fifty_numbers})', globals=globals(), number=1000000)
    print('i + 1 ->',normal_time)
  
    enum_start_time: float = timeit(f'enumerate_func({fifty_numbers})', globals=globals(), number=1000000)
    print('start=1 ->',enum_start_time)

    print('Output is same:',normal_func(fifty_numbers) == enumerate_func(fifty_numbers))
  
  
# Answer: i + 1 -> 18.235193822999918
#         start=1 -> 14.654170921000059
#         Output is same: True
