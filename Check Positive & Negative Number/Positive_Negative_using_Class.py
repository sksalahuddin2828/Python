class NumberClassifier:
    def __init__(self, num):
        self.num = num

    def classify(self):
        if self.num > 0:
            return "positive"
        elif self.num < 0:
            return "negative"
        else:
            return "zero"

num = float(input("Enter a number: "))
classifier = NumberClassifier(num)
result = classifier.classify()
print(f"The number is {result}.")
