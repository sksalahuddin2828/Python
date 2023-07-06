# Pharmacy Management Software implemented using Tkinter:

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

        # Layout using grid
        self.name_label.grid(row=0, column=0)
        self.name_input.grid(row=0, column=1)
        self.price_label.grid(row=1, column=0)
        self.price_input.grid(row=1, column=1)
        self.quantity_label.grid(row=2, column=0)
        self.quantity_input.grid(row=2, column=1)
        self.add_button.grid(row=3, column=0, columnspan=2)

    def add_drug(self):
        name = self.name_input.get()
        price = float(self.price_input.get())
        quantity = int(self.quantity_input.get())
        # Add the drug to the inventory or perform necessary actions
        messagebox.showinfo("Drug Added", f"Drug added: Name={name}, Price={price}, Quantity={quantity}")

if __name__ == '__main__':
    root = tk.Tk()
    app = PharmacyManagementSystem(root)
    root.mainloop()
