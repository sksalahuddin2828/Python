# Using nested if with Python list comprehension

my_list = [i for i in range(50) if i % 2 == 0 if i % 5 == 0]

# Answer: [0, 10, 20, 30, 40, 50]


# Using if else statement with Python list comprehension

even_odd_number = [f"{i} is even" if i % 2 == 0 else f"{i} is odd" for i in range(51)]
print(even_odd_number)

# Answer: ['0 is even', '1 is odd', '2 is even', '3 is odd', '4 is even', '5 is odd', '6 is even', '7 is odd', '8 is even', '9 is odd', '10 is even', '11 is odd', '12 is even', '13 is odd', '14 is even', '15 is odd', '16 is even', '17 is odd', '18 is even', '19 is odd', '20 is even', '21 is odd', '22 is even', '23 is odd', '24 is even', '25 is odd', '26 is even', '27 is odd', '28 is even', '29 is odd', '30 is even', '31 is odd', '32 is even', '33 is odd', '34 is even', '35 is odd', '36 is even', '37 is odd', '38 is even', '39 is odd', '40 is even', '41 is odd', '42 is even', '43 is odd', '44 is even', '45 is odd', '46 is even', '47 is odd', '48 is even', '49 is odd', '50 is even']



list = [[i*j for j in range(1,11)] for i in range(2,8)]
print(list)

# Answer: [[3, 6, 9, 12, 15, 18, 21, 24, 27, 30], 
           [4, 8, 12, 16, 20, 24, 28, 32, 36, 40], 
           [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]]


# Nested lists in Python list comprehension
# From user input (User give an input number like 1st number: 1, and 2nd number: 6 then it's print from 1 to 5 multiplication table)

num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
for i in range(num1,num2):
    for j in range(1,11):
        print(f"{i} * {j} = {i*j}")


# Nested lists in Python list comprehension

for i in range(1,6):
    for j in range(1,11):
        print(f"{i} * {j} = {i*j}")

# Answer:

1 * 1 = 1
1 * 2 = 2
1 * 3 = 3
1 * 4 = 4
1 * 5 = 5
1 * 6 = 6
1 * 7 = 7
1 * 8 = 8
1 * 9 = 9
1 * 10 = 10
2 * 1 = 2
2 * 2 = 4
2 * 3 = 6
2 * 4 = 8
2 * 5 = 10
2 * 6 = 12
2 * 7 = 14
2 * 8 = 16
2 * 9 = 18
2 * 10 = 20
3 * 1 = 3
3 * 2 = 6
3 * 3 = 9
3 * 4 = 12
3 * 5 = 15
3 * 6 = 18
3 * 7 = 21
3 * 8 = 24
3 * 9 = 27
3 * 10 = 30
4 * 1 = 4
4 * 2 = 8
4 * 3 = 12
4 * 4 = 16
4 * 5 = 20
4 * 6 = 24
4 * 7 = 28
4 * 8 = 32
4 * 9 = 36
4 * 10 = 40
5 * 1 = 5
5 * 2 = 10
5 * 3 = 15
5 * 4 = 20
5 * 5 = 25
5 * 6 = 30
5 * 7 = 35
5 * 8 = 40
5 * 9 = 45
5 * 10 = 50

