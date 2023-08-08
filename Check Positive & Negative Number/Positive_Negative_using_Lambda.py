def positive():
    return "positive"

def negative():
    return "negative"

def zero():
    return "zero"

classifications = {
    lambda x: x > 0: positive,
    lambda x: x < 0: negative,
    lambda x: x == 0: zero
}

num = float(input("Enter a number: "))
classification = next(value() for condition, value in classifications.items() if condition(num))

print(f"The number is {classification}.")
