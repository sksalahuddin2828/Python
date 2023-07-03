def bubble_sort(array):
    length = len(array)

    # Traverse through all array elements
    for first_variable in range(length - 1):
        # Last first_variable elements are already in place
        for second_variable in range(0, length - first_variable - 1):
            # Traverse the array from 0 to length - first_variable - 1
            # Swap if the element found is greater
            # than the next element
            if array[second_variable] > array[second_variable + 1]:
                array[second_variable], array[second_variable + 1] = array[second_variable + 1], array[second_variable]

# Driver code to test above
stored_array = [64, 34, 25, 12, 22, 11, 90]

bubble_sort(stored_array)

print("Sorted array is:")
for third_variable in range(len(stored_array)):
    print("%d" % stored_array[third_variable])


# Answer: Sorted array is:
#         11
#         12
#         22
#         25
#         34
#         64
#         90
