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


decimal_number = 42
octal_number = oct(decimal_number)
print(octal_number)  

# Output: 0o52

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

#----------------------------------------------Printing the Fibonacci Series Using Recursion: (Another way)------------------------------------

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        sequence = fibonacci(n - 1)
        sequence.append(sequence[-1] + sequence[-2])
        return sequence

n = 10  # The number of Fibonacci numbers to print
fib_series = fibonacci(n)
print(fib_series) 

# Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

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

#-------------------------------------------Returning the Nth Value from the Fibonacci Sequence: (Another way)---------------------------------

def fibonacci(n):
    if n <= 0:
        return None
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(n - 2):
            a, b = b, a + b
        return b

n = 7  # The position of the Fibonacci number to find
fib_value = fibonacci(n)
print(fib_value) 

# Output: 8

#----------------------------------------------------------------------------------------------------------------------------------------------

# 5. Finding the Average of Numbers:

numbers = [10, 20, 30, 40, 50]
average = sum(numbers) / len(numbers)
print(average)  

# Output: 30.0

#-----------------------------------------------------Finding the Average of Numbers: (Another way)-------------------------------------------

def calculate_average(numbers):
    if len(numbers) == 0:
        return None
    else:
        total = sum(numbers)
        average = total / len(numbers)
        return average

number_list = [2, 4, 6, 8, 10]
avg = calculate_average(number_list)
print(avg)  

# Output: 6.0

#----------------------------------------------------------------------------------------------------------------------------------------------

# 6. Convert Celsius to Fahrenheit:

celsius = float(input("Enter the temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"The temperature in Fahrenheit is: {fahrenheit}")
