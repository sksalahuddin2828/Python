class ClassificationContext:
    def __init__(self, number):
        self.number = number

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        pass

def positive(fn):
    def wrapper(context):
        return fn(context) if context.number > 0 else None
    return wrapper

def negative(fn):
    def wrapper(context):
        return fn(context) if context.number < 0 else None
    return wrapper

def zero(fn):
    def wrapper(context):
        return fn(context) if context.number == 0 else None
    return wrapper

num = float(input("Enter a number: "))

with ClassificationContext(num) as context:
    classification = (
        positive(lambda c: "positive"),
        negative(lambda c: "negative"),
        zero(lambda c: "zero")
    )

    result = next((classify(context) for condition, classify in classification if condition(context)), None)

print(f"The number is {result}.")
