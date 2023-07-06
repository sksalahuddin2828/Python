drug_inventory = {}

def add_drug():
    name = input("Enter drug name: ")
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))
    drug_inventory[name] = {'price': price, 'quantity': quantity}
    print("Drug added successfully!")

def update_drug():
    name = input("Enter drug name: ")
    if name in drug_inventory:
        price = float(input("Enter new price: "))
        quantity = int(input("Enter new quantity: "))
        drug_inventory[name]['price'] = price
        drug_inventory[name]['quantity'] = quantity
        print("Drug information updated successfully!")
    else:
        print("Drug not found in the inventory!")

def view_drug():
    name = input("Enter drug name (leave blank to view all drugs): ")
    if name:
        if name in drug_inventory:
            drug = drug_inventory[name]
            print(f"Drug Name: {name}")
            print(f"Price: {drug['price']}")
            print(f"Quantity: {drug['quantity']}")
        else:
            print("Drug not found in the inventory!")
    else:
        if not drug_inventory:
            print("No drugs in the inventory!")
        else:
            for name, drug in drug_inventory.items():
                print(f"Drug Name: {name}")
                print(f"Price: {drug['price']}")
                print(f"Quantity: {drug['quantity']}")

def record_purchase():
    name = input("Enter drug name: ")
    if name in drug_inventory:
        quantity = int(input("Enter quantity purchased: "))
        if quantity <= drug_inventory[name]['quantity']:
            drug_inventory[name]['quantity'] -= quantity
            print("Purchase recorded successfully!")
        else:
            print("Insufficient quantity in the inventory!")
    else:
        print("Drug not found in the inventory!")

def search_drug():
    keyword = input("Enter a keyword to search for drugs: ")
    search_results = []
    for name in drug_inventory:
        if keyword.lower() in name.lower():
            search_results.append(name)
    if search_results:
        print("Search Results:")
        for result in search_results:
            print(result)
    else:
        print("No drugs found matching the keyword.")

def delete_drug():
    name = input("Enter drug name to delete: ")
    if name in drug_inventory:
        del drug_inventory[name]
        print(f"{name} deleted from the inventory.")
    else:
        print("Drug not found in the inventory!")

def set_expiration_date():
    name = input("Enter drug name: ")
    if name in drug_inventory:
        expiration_date = input("Enter expiration date (YYYY-MM-DD): ")
        drug_inventory[name]['expiration_date'] = expiration_date
        print("Expiration date set successfully!")
    else:
        print("Drug not found in the inventory!")

def check_low_stock_alert():
    threshold = int(input("Enter the minimum quantity threshold: "))
    low_stock_drugs = []
    for name, drug in drug_inventory.items():
        if drug['quantity'] <= threshold:
            low_stock_drugs.append(name)
    if low_stock_drugs:
        print("Low Stock Drugs:")
        for drug in low_stock_drugs:
            print(drug)
    else:
        print("No drugs are below the quantity threshold.")

#-----------------------------------------------------------------------------------
#-------------------------------------Edit Here-------------------------------------

def generate_sales_report():
    # Implement sales reporting functionality based on your requirements
    pass

def user_authentication():
    # Implement user authentication functionality based on your requirements
    pass

def save_data():
   # Save the drug inventory data to a file or database
    # Implement data persistence functionality based on your requirements
    pass

def load_data():
    # Load the drug inventory data from a file or database
    # Implement data persistence functionality based on your requirements
    pass

#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------

def menu():
    while True:
        print("\nPharmacy Management System")
        print("1. Add Drug")
        print("2. Update Drug Information")
        print("3. View Drug Information")
        print("4. Record Purchase")
        print("5. Search Drug")
        print("6. Delete Drug")
        print("7. Set Expiration Date")
        print("8. Check Low Stock Alert")
        print("9. Generate Sales Report")
        print("10. User Authentication")
        print("11. Save Data")
        print("12. Load Data")
        print("13. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_drug()
        elif choice == '2':
            update_drug()
        elif choice == '3':
            view_drug()
        elif choice == '4':
            record_purchase()
        elif choice == '5':
            search_drug()
        elif choice == '6':
            delete_drug()
        elif choice == '7':
            set_expiration_date()
        elif choice == '8':
            check_low_stock_alert()
        elif choice == '9':
            generate_sales_report()
        elif choice == '10':
            user_authentication()
        elif choice == '11':
            save_data()
        elif choice == '12':
            load_data()
        elif choice == '13':
            break
        else:
            print("Invalid choice. Try again!")

menu()
