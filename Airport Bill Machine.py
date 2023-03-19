print("Dear passenger's Welcome to Incheon International Airport, South Korea")
print("This is an automated shopping payement system. You can buy what if you want from here")
print("You may specify payment syatem from next section")
print(" ")

proceed = input("Do you want to proceed: Yes/No \n")

if proceed == "Yes":
    print(" ")
    
    number_of_book = float(input("One book costs 4.99 USD. Hoy many books do you want?\n"))
    
    number_of_pen = float(input("One pen costs 3.20 USD. Hoy many books do you want?\n"))
    
    number_of_pencil = float(input("One pencil costs 1.49 USD. Hoy many books do you want?\n"))
    
    number_of_ruler = float(input("One ruler costs 0.50 USD. Hoy many books do you want?\n"))

    number_of_w_paper = float(input("One Whiter Paper costs 0.13 USD. Hoy many books do you want?\n"))

    total_costs = (4.99*number_of_book) + (3.20*number_of_pen) + (1.49*number_of_pencil) + (0.50*number_of_ruler) + (0.13*number_of_w_paper)
    
    print("Your total bill is: " + str(total_costs))
    print("You can payment via VISA / MasterCard / bKash / Upay / Nagad / Gpay / Qcash / Maestro")

elif proceed == "No":
    print("Thank you for your interest, see you in next time. Have a good day")
