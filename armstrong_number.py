def is_armstrong_number(n):
    num_digits = len(str(n))
    sum_of_powers = 0
    temp = n
    while temp > 0:
        digit = temp % 10
        sum_of_powers += digit ** num_digits
        temp //= 10
    return n == sum_of_powers

# Prompt user for input
user_input = int(input("Enter a number: "))
if is_armstrong_number(user_input):
    print(f"{user_input} is an Armstrong number.")
else:
    print(f"{user_input} is not an Armstrong number.")

#-------------------------------------------------------------------

def is_armstrong_number(n):
    num_digits = len(str(n))
    sum_of_powers = 0
    temp = n
    while temp > 0:
        digit = temp % 10
        sum_of_powers += digit ** num_digits
        temp //= 10
    return n == sum_of_powers

# Test the function
print(is_armstrong_number(153))  

# Output: True
