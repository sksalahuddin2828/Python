source: str = 'str(10 + 10 * 2) + "Bangladesh"'

result: str = eval(source)
print(result)

# Answer: 30Bangladesh

#-----------------------------------------------------------------------

source: str = 'print()'

result: str = eval(source)
print(result)

# Answer: None

#-----------------------------------------------------------------------

source: str = 'print("Hello World!")'

result: str = eval(source)
print(result)

# Answer: Hello World!
#         None

#-----------------------------------------------------------------------

user_input: str = input("Calculate: ")

print(eval(user_input))

# Input: 10 + 10 + (10 / 2)
# Answer: 25.0

#-----------------------------------------------------------------------

source: str = """
print("exec():")

x = 10
y = 11

for i in range(3):
    print(x + y, i, sep='-')
"""

exec(source)

# Answer: exec():
#         21-0
#         21-1
#         21-2

#-----------------------------------------------------------------------

source: str = input("Enter any built-in function: ")

exec(source)

# Input: print("Hello World!")
# Answer: Hello World!

#-----------------------------------------------------------------------

source: str = """
print("exec():")

x = 10
y = 11

for i in range(3):
    print(x + y, i, sep='-')
"""

result = exec(source)
print(result)

# Answer: exec():
#         21-0
#         21-1
#         21-2
#         None

#-----------------------------------------------------------------------

source: str = """
print("exec():")

x = 10
y = 11

for i in range(3):
    print(x + y, i, sep='-')
"""

result = exec(source)
print(result)
print(x)

# Answer: exec():
#         21-0
#         21-1
#         21-2
#         None
#         10

#-----------------------------------------------------------------------

x = "Bangladesh"

source: str = """
print("exec():")

x = 10
y = 11

for i in range(3):
    print(x + y, i, sep='-')
"""

result = exec(source)
print(result)
print(x)

# Answer: exec():
#         21-0
#         21-1
#         21-2
#         None
#         10

#-----------------------------------------------------------------------

x = "Bangladesh"

source: str = """
print("exec():")

x = 10
y = 11

for i in range(3):
    print(x + y, i, sep='-')
    
result = "Try something!"
"""

exec(source)
print(result)
print(x)

# Answer: exec():
#         21-0
#         21-1
#         21-2
#         Try something!
#         10
