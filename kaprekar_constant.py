def kaprekar_constant(n):
    count = 0
    while n != 6174:
        count += 1
        digits = str(n).zfill(4)
        ascending = int(''.join(sorted(digits)))
        descending = int(''.join(sorted(digits, reverse=True)))
        n = descending - ascending
    return count

# Prompt user for input
user_input = int(input("Enter a number: "))
steps = kaprekar_constant(user_input)
print(f"Number of steps to reach Kaprekar constant: {steps}")


# Answer: Enter a number: 2352
#         Number of steps to reach Kaprekar constant: 3


#--------------------------------------------------------------------------

def kaprekar_constant(n):
    count = 0
    while n != 6174:
        count += 1
        digits = str(n).zfill(4)
        ascending = int(''.join(sorted(digits)))
        descending = int(''.join(sorted(digits, reverse=True)))
        n = descending - ascending
    return count

# Test the function
print(kaprekar_constant(1234))  

# Output: 3
