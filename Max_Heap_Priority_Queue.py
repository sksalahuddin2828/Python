def heapify(arr, n, i):
    # Find the largest among root, left child, and right child
    largest = i
    left_child = 2 * i + 1
    right_child = 2 * i + 2

    if left_child < n and arr[i] < arr[left_child]:
        largest = left_child

    if right_child < n and arr[largest] < arr[right_child]:
        largest = right_child

    # Swap and continue heapifying if root is not the largest
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def insert(array, new_num):
    size = len(array)
    if size == 0:
        array.append(new_num)
    else:
        array.append(new_num)
        for i in range((size // 2) - 1, -1, -1):
            heapify(array, size, i)


def delete_node(array, num):
    size = len(array)
    i = 0
    for i in range(0, size):
        if num == array[i]:
            break

    array[i], array[size - 1] = array[size - 1], array[i]
    array.pop()

    for i in range((len(array) // 2) - 1, -1, -1):
        heapify(array, len(array), i)


store_array = []

insert(store_array, 3)
insert(store_array, 4)
insert(store_array, 9)
insert(store_array, 5)
insert(store_array, 2)

print("Max-Heap array:", store_array)

delete_node(store_array, 4)
print("After deleting an element:", store_array)


# Answer: Max-Heap array: [9, 5, 4, 3, 2]
#         After deleting an element: [9, 5, 2, 3]
