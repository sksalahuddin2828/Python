import cmath

def find_square_root():
    # Take input from the user
    num = eval(input('Enter a number: '))

    # Find the square root of the number
    num_sqrt = cmath.sqrt(num)

    # Display the result
    if num_sqrt.imag == 0:
        print('The square root of {0} is {1:0.3f}'.format(num, num_sqrt.real))
    else:
        print('The square root of {0} is {1:0.3f}+{2:0.3f}j'.format(num, num_sqrt.real, num_sqrt.imag))

# Call the function to find the square root
find_square_root()


# Answer: Enter a number: 1+2j
#         The square root of (1+2j) is 1.272+0.786j


#-----------------------------------------------------Another way of solving---------------------------------------------------------


# find square root of real or complex numbers
# importing the complex math module
import cmath

numbers = 4 + 9j

num_sqrt = cmath.sqrt(numbers)
print('The square root of {0} is {1:0.3f}+{2:0.3f}j'.format(numbers, num_sqrt.real, num_sqrt.imag))

# Answer: The square root of (4+9j) is 2.631+1.710j


#-----------------------------------------------------Another way of solving---------------------------------------------------------

import cmath

# to take a complex input from the user
num = eval(input('Enter a number: '))

num_sqrt = cmath.sqrt(num)
print('The square root of {0} is {1:0.3f}+{2:0.3f}j'.format(num, num_sqrt.real, num_sqrt.imag))

# User give input in here like: 2 + 3j
# Answer: The square root of (2+3j) is 1.674+0.896j
