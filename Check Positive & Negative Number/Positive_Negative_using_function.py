def check_positive_negative(num):
    if num > 0:
        return "positive"
    elif num < 0:
        return "negative"
    else:
        return "zero"

num = float(input("Enter a number: "))
result = check_positive_negative(num)
print(f"The number is {result}.")
