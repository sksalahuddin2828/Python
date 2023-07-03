def calculate_factorial(n):
    if n > 1:
        return n * calculate_factorial(n - 1)
    else:
        return 1

number = int(input("Enter a non-negative number: "))
result = calculate_factorial(number)
print(f"Factorial of {number} = {result}")


# Answer: Enter a non-negative number: 6
#         Factorial of 6 = 720
