num = int(input("Enter a number: "))

if num <= 100:
    print("No charge")
elif num > 100 and num <= 200:
    num = (num - 100) * 5
    print("Bill is",num)
elif num > 200:
    num = 500 + (num - 200) * 10
    print("Bill is",num)
else:
    print("Wrong number input")
