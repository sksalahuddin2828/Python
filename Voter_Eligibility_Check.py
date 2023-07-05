# Program for checking voter age
while True:
    try:
        age = int(input("Enter your age: "))
        # Check if the age is within a valid range for voting

        if 18 <= age <= 120:
            print("Congratulations!")
            print("You are eligible to vote.")
        elif 12 <= age < 18:
            print("You are not yet eligible to vote.")
            print("Enjoy your teenage years!")
        elif 0 <= age < 12:
            print("You are too young to vote.")
            print("Make the most of your childhood!")
        elif age < 0:
            print("Invalid age entered.")
            print("Please enter a positive value.")
        else:
            print("You have surpassed the maximum voting age.")
            print("Thank you for your contribution to society!")
            
        break  # Exit the loop after successful age input
    except ValueError:
        print("Invalid age entered. Please enter a valid integer age.")
