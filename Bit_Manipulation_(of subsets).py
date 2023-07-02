# Print to subsets of an array using Bit Manipulation

array = [1, 2, 3, 4]
length = (1 << len(array))

for var in range(0, length):
    number = var
    position = 0
    store_array = []
    while number != 0:
        if number & 1 << 0: store_array.append(array[position])
        number = number >> 1
        position = position + 1
    print(store_array) 


# Answer: []
#         [1]
#         [2]
#         [1, 2]
#         [3]
#         [1, 3]
#         [2, 3]
#         [1, 2, 3]
#         [4]
#         [1, 4]
#         [2, 4]
#         [1, 2, 4]
#         [3, 4]
#         [1, 3, 4]
#         [2, 3, 4]
#         [1, 2, 3, 4]
