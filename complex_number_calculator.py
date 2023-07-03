class Complex:
    def __init__(self):
        self.real = 0.0
        self.imag = 0.0
    
    def set_data(self):
        self.real = float(input("Enter the real value of the complex number: "))
        self.imag = float(input("Enter the imaginary value of the complex number: "))
    
    def add(self, a, b, c, d):
        self.real = a + c
        self.imag = b + d
    
    def subtract(self, a, b, c, d):
        self.real = a - c
        self.imag = b - d
    
    def multiply(self, a, b, c, d):
        self.real = (a * c) - (b * d)
        self.imag = (a * d) + (b * c)
    
    def divide(self, a, b, c, d):
        self.real = ((a * c) + (b * d)) / ((c * c) + (d * d))
        self.imag = ((b * c) - (a * d)) / ((c * c) + (d * d))
    
    def get_data(self):
        if self.imag >= 0:
            print(f"{self.real}+{self.imag}i")
        else:
            print(f"{self.real}{self.imag}i")


if __name__ == "__main__":
    x1 = Complex()
    x2 = Complex()
    addition = Complex()
    subtraction = Complex()
    multiplication = Complex()
    division = Complex()

    x1.set_data()
    x2.set_data()

    print("Complex number 1 is:")
    x1.get_data()
    print("Complex number 2 is:")
    x2.get_data()

    ans = 1
    while ans == 1:
        print("Choose the operation to perform:")
        print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division")
        a = int(input())

        if a == 1:
            addition.add(x1.real, x1.imag, x2.real, x2.imag)
            print("Addition of Complex 1 and Complex 2 is:")
            addition.get_data()
        elif a == 2:
            subtraction.subtract(x1.real, x1.imag, x2.real, x2.imag)
            print("Subtraction of Complex 2 from Complex 1 is:")
            subtraction.get_data()
        elif a == 3:
            multiplication.multiply(x1.real, x1.imag, x2.real, x2.imag)
            print("Multiplication of Complex 1 and Complex 2 is:")
            multiplication.get_data()
        elif a == 4:
            if x2.real == 0 and x2.imag == 0:
                print("Can't divide by zero")
            else:
                division.divide(x1.real, x1.imag, x2.real, x2.imag)
                print("On division of Complex 1 by Complex 2, we get:")
                division.get_data()
        else:
            print("Invalid option chosen!")
        
        ans = int(input("Do you want to check more? (1 for yes / 2 for no): "))
        if ans == 2:
            break

    print("\nThank you")


# Answer: Enter the real value of the complex number: 1
#         Enter the imaginary value of the complex number: 2
#         Enter the real value of the complex number: -1
#         Enter the imaginary value of the complex number: 4
#         Complex number 1 is:
#         1.0+2.0i
#         Complex number 2 is:
#         -1.0+4.0i
#         Choose the operation to perform:
#         1. Addition
#         2. Subtraction
#         3. Multiplication
#         4. Division
#         1
#         Addition of Complex 1 and Complex 2 is:
#         0.0+6.0i
#         Do you want to check more? (1 for yes / 2 for no): 2
#         Thank you
