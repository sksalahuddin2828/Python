import json
import tkinter as tk
from tkinter import messagebox


class PharmacyManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Pharmacy Management System")
        self.root.geometry("400x200")

        # Create labels, text inputs, and buttons
        self.name_label = tk.Label(root, text="Drug Name:")
        self.name_input = tk.Entry(root)
        self.price_label = tk.Label(root, text="Price:")
        self.price_input = tk.Entry(root)
        self.quantity_label = tk.Label(root, text="Quantity:")
        self.quantity_input = tk.Entry(root)
        self.add_button = tk.Button(root, text="Add Drug", command=self.add_drug)
        self.search_button = tk.Button(root, text="Search Drug", command=self.search_drug)
        self.delete_button = tk.Button(root, text="Delete Drug", command=self.delete_drug)
        self.save_button = tk.Button(root, text="Save Data", command=self.save_data)
        self.load_button = tk.Button(root, text="Load Data", command=self.load_data)
        self.sales_report_button = tk.Button(root, text="Generate Sales Report", command=self.generate_sales_report)
        self.auth_button = tk.Button(root, text="User Authentication", command=self.user_authentication)

        # Layout using grid
        self.name_label.grid(row=0, column=0)
        self.name_input.grid(row=0, column=1)
        self.price_label.grid(row=1, column=0)
        self.price_input.grid(row=1, column=1)
        self.quantity_label.grid(row=2, column=0)
        self.quantity_input.grid(row=2, column=1)
        self.add_button.grid(row=3, column=0, columnspan=2)
        self.search_button.grid(row=4, column=0, columnspan=2)
        self.delete_button.grid(row=5, column=0, columnspan=2)
        self.save_button.grid(row=6, column=0, columnspan=2)
        self.load_button.grid(row=7, column=0, columnspan=2)
        self.sales_report_button.grid(row=8, column=0, columnspan=2)
        self.auth_button.grid(row=9, column=0, columnspan=2)

        # Load data from file
        self.load_data()

    def add_drug(self):
        name = self.name_input.get()
        price = float(self.price_input.get())
        quantity = int(self.quantity_input.get())
        drug_inventory[name] = {'price': price, 'quantity': quantity}
        messagebox.showinfo("Drug Added", "Drug added successfully!")

    def search_drug(self):
        keyword = self.name_input.get()
        search_results = []
        for name in drug_inventory:
            if keyword.lower() in name.lower():
                search_results.append(name)
        if search_results:
            messagebox.showinfo("Search Results", f"Drugs found: {', '.join(search_results)}")
        else:
            messagebox.showinfo("Search Results", "No drugs found matching the keyword.")

    def delete_drug(self):
        name = self.name_input.get()
        if name in drug_inventory:
            del drug_inventory[name]
            messagebox.showinfo("Drug Deleted", f"{name} deleted from the inventory.")
        else:
            messagebox.showinfo("Drug Not Found", "Drug not found in the inventory.")

    def generate_sales_report(self):
        total_sales = sum(drug['price'] * (drug['quantity'] - drug_inventory[name]['quantity'])
                          for name, drug in drug_inventory.items())
        messagebox.showinfo("Sales Report", f"Total Sales: ${total_sales:.2f}")

        sorted_drugs = sorted(drug_inventory.items(), key=lambda x: x[1]['quantity'], reverse=True)
        top_selling_drugs = "\n".join(f"Drug Name: {name}\nQuantity Sold: {drug['quantity'] - drug_inventory[name]['quantity']}"
                                      for name, drug in sorted_drugs[:5])  # Display top 5 selling drugs
        messagebox.showinfo("Top Selling Drugs", top_selling_drugs)

    def user_authentication(self):
        username = self.name_input.get()
        password = self.price_input.get()

        if username == "admin" and password == "password":
            messagebox.showinfo("Authentication Successful", "Access granted.")
        else:
            messagebox.showinfo("Authentication Failed", "Access denied.")

    def save_data(self):
        with open("drug_inventory.json", "w") as file:
            json.dump(drug_inventory, file)
        messagebox.showinfo("Data Saved", "Data saved successfully.")

    def load_data(self):
        try:
            with open("drug_inventory.json", "r") as file:
                drug_inventory.update(json.load(file))
            messagebox.showinfo("Data Loaded", "Data loaded successfully.")
        except FileNotFoundError:
            messagebox.showinfo("No Previous Data", "No previous data found.")


if __name__ == '__main__':
    drug_inventory = {}
    root = tk.Tk()
    app = PharmacyManagementSystem(root)
    root.mainloop()
