def are_arrays_equal(array1, array2):
    length1 = len(array1)
    length2 = len(array2)

    # If lengths of arrays are not equal, they are not equal
    if length1 != length2:
        return False

    # Sort both arrays
    array1.sort()
    array2.sort()

    # Linearly compare elements
    for i in range(length1):
        if array1[i] != array2[i]:
            return False

    # If all elements are the same
    return True


# Driver code
if __name__ == "__main__":
    array1 = [3, 5, 2, 5, 2]
    array2 = [2, 3, 5, 5, 2]

    if are_arrays_equal(array1, array2):
        print("The arrays are equal.")
    else:
        print("The arrays are not equal.")


# Answer: The arrays are equal.
