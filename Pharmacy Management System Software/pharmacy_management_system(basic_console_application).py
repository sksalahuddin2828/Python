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

def generate_sales_report():
    # Here are some possible steps to implement the sales reporting functionality:
    # 1. Calculate the total sales by iterating over the drug_inventory and multiplying the price with the quantity sold.
    # 2. Determine the top-selling drugs by sorting the drug_inventory based on the quantity sold or revenue generated.
    # 3. Display the sales report with relevant information such as total sales, top-selling drugs, etc.
    # You can modify and enhance the code below based on your specific reporting requirements.
    
    total_sales = 0
    for name, drug in drug_inventory.items():
        price = drug['price']
        quantity_sold = drug['quantity'] - drug_inventory[name]['quantity']
        total_sales += price * quantity_sold

    print(f"Total Sales: ${total_sales:.2f}")

    sorted_drugs = sorted(drug_inventory.items(), key=lambda x: x[1]['quantity'], reverse=True)
    print("Top Selling Drugs:")
    for drug_name, drug_info in sorted_drugs[:5]:  # Display top 5 selling drugs
        print(f"Drug Name: {drug_name}")
        print(f"Quantity Sold: {drug_info['quantity'] - drug_inventory[drug_name]['quantity']}")


def user_authentication():
    # Implementing user authentication depends on your specific requirements and the level of security you need.
    # You can create a login system with username and password, store user credentials in a database or file,
    # and validate the user's input against the stored credentials.
    # You can also assign different roles or permissions to users to restrict access to certain functionalities.
    # Below is a basic example that assumes a single user and doesn't use encryption. Modify it based on your needs.

    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == "admin" and password == "password":
        print("Authentication successful. Access granted.")
    else:
        print("Authentication failed. Access denied.")

def save_data():
    # You can implement data persistence by saving the drug inventory to a file or database.
    # Here's an example of saving the drug_inventory dictionary to a JSON file using the `json` module.

    import json

    with open("drug_inventory.json", "w") as file:
        json.dump(drug_inventory, file)

    print("Data saved successfully.")

def load_data():
    # To load data from a file or database, you can use the corresponding functionality based on your chosen data format.
    # Here's an example of loading drug inventory data from a JSON file.

    import json

    try:
        with open("drug_inventory.json", "r") as file:
            drug_inventory.update(json.load(file))
        print("Data loaded successfully.")
    except FileNotFoundError:
        print("No previous data found.")

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


#--------------------------------------------------------------------------------------------
# After running the program, what you want to do, choose the option according to your choice:
#--------------------------------------------------------------------------------------------

# Answer: Pharmacy Management System
#         1. Add Drug
#         2. Update Drug Information
#         3. View Drug Information
#         4. Record Purchase
#         5. Search Drug
#         6. Delete Drug
#         7. Set Expiration Date
#         8. Check Low Stock Alert
#         9. Generate Sales Report
#         10. User Authentication
#         11. Save Data
#         12. Load Data
#         13. Quit
#         Enter your choice: 
