#-------------------------------------------------------------Python Coding Challenges---------------------------------------------------------

# Python Coding Challenges on Numbers 
# Write a program in Python to -

# 1. Convert decimal numbers to octal numbers.
# 2. Reverse an integer.
# 3. Print the Fibonacci series using the recursive method.
# 4. Return the Nth value from the Fibonacci sequence.
# 5. Find the average of numbers (with explanations).
# 6. Convert Celsius to Fahrenheit.

#----------------------------------------------------------------Solution of Problem:----------------------------------------------------------

# 1. Converting Decimal Numbers to Octal Numbers:

decimal_number = 25
octal_number = oct(decimal_number)[2:]
print(octal_number)  

# Output: 31

#----------------------------------------------------------------------------------------------------------------------------------------------

# 2. Reversing an Integer:

number = 12345
reversed_number = int(str(number)[::-1])
print(reversed_number)  

# Output: 54321

#----------------------------------------------------------------------------------------------------------------------------------------------

# 3. Printing the Fibonacci Series using Recursion:

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Printing the Fibonacci series up to the 10th number
for i in range(10):
    print(fibonacci(i))

#----------------------------------------------------------------------------------------------------------------------------------------------

# 4. Returning the Nth Value from the Fibonacci Sequence:

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Getting the 10th Fibonacci number
n = 10
fibonacci_number = fibonacci(n)
print(fibonacci_number)  

# Output: 55

#----------------------------------------------------------------------------------------------------------------------------------------------

# 5. Finding the Average of Numbers:

numbers = [10, 20, 30, 40, 50]
average = sum(numbers) / len(numbers)
print(average)  

# Output: 30.0
