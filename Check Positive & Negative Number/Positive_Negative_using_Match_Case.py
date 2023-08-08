num = float(input("Enter a number: "))

classification = match num:
    case n if n > 0:
        "positive"
    case n if n < 0:
        "negative"
    case _:
        "zero"

print(f"The number is {classification}.")
