import sys
import json
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QLineEdit, QPushButton, QMessageBox


class PharmacyManagementSystem(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pharmacy Management System")
        self.setGeometry(100, 100, 400, 200)

        # Create labels, text inputs, and buttons
        self.name_label = QLabel("Drug Name:")
        self.name_input = QLineEdit()
        self.price_label = QLabel("Price:")
        self.price_input = QLineEdit()
        self.quantity_label = QLabel("Quantity:")
        self.quantity_input = QLineEdit()
        self.add_button = QPushButton("Add Drug", self)
        self.add_button.clicked.connect(self.add_drug)
        self.search_button = QPushButton("Search Drug", self)
        self.search_button.clicked.connect(self.search_drug)
        self.delete_button = QPushButton("Delete Drug", self)
        self.delete_button.clicked.connect(self.delete_drug)
        self.save_button = QPushButton("Save Data", self)
        self.save_button.clicked.connect(self.save_data)
        self.load_button = QPushButton("Load Data", self)
        self.load_button.clicked.connect(self.load_data)
        self.sales_report_button = QPushButton("Generate Sales Report", self)
        self.sales_report_button.clicked.connect(self.generate_sales_report)
        self.auth_button = QPushButton("User Authentication", self)
        self.auth_button.clicked.connect(self.user_authentication)

        # Create a layout and add widgets to it
        layout = QVBoxLayout()
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_input)
        layout.addWidget(self.price_label)
        layout.addWidget(self.price_input)
        layout.addWidget(self.quantity_label)
        layout.addWidget(self.quantity_input)
        layout.addWidget(self.add_button)
        layout.addWidget(self.search_button)
        layout.addWidget(self.delete_button)
        layout.addWidget(self.save_button)
        layout.addWidget(self.load_button)
        layout.addWidget(self.sales_report_button)
        layout.addWidget(self.auth_button)

        # Create a central widget and set the layout
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Load data from file
        self.load_data()

    def add_drug(self):
        name = self.name_input.text()
        price = float(self.price_input.text())
        quantity = int(self.quantity_input.text())
        drug_inventory[name] = {'price': price, 'quantity': quantity}
        QMessageBox.information(self, "Drug Added", "Drug added successfully!")

    def search_drug(self):
        keyword = self.name_input.text()
        search_results = []
        for name in drug_inventory:
            if keyword.lower() in name.lower():
                search_results.append(name)
        if search_results:
            QMessageBox.information(self, "Search Results", f"Drugs found: {', '.join(search_results)}")
        else:
            QMessageBox.information(self, "Search Results", "No drugs found matching the keyword.")

    def delete_drug(self):
        name = self.name_input.text()
        if name in drug_inventory:
            del drug_inventory[name]
            QMessageBox.information(self, "Drug Deleted", f"{name} deleted from the inventory.")
        else:
            QMessageBox.information(self, "Drug Not Found", "Drug not found in the inventory.")

    def generate_sales_report(self):
        total_sales = sum(drug['price'] * (drug['quantity'] - drug_inventory[name]['quantity'])
                          for name, drug in drug_inventory.items())
        QMessageBox.information(self, "Sales Report", f"Total Sales: ${total_sales:.2f}")

        sorted_drugs = sorted(drug_inventory.items(), key=lambda x: x[1]['quantity'], reverse=True)
        top_selling_drugs = "\n".join(f"Drug Name: {name}\nQuantity Sold: {drug['quantity'] - drug_inventory[name]['quantity']}"
                                      for name, drug in sorted_drugs[:5])  # Display top 5 selling drugs
        QMessageBox.information(self, "Top Selling Drugs", top_selling_drugs)

    def user_authentication(self):
        username = self.name_input.text()
        password = self.price_input.text()

        if username == "admin" and password == "password":
            QMessageBox.information(self, "Authentication Successful", "Access granted.")
        else:
            QMessageBox.information(self, "Authentication Failed", "Access denied.")

    def save_data(self):
        with open("drug_inventory.json", "w") as file:
            json.dump(drug_inventory, file)
        QMessageBox.information(self, "Data Saved", "Data saved successfully.")

    def load_data(self):
        try:
            with open("drug_inventory.json", "r") as file:
                drug_inventory.update(json.load(file))
            QMessageBox.information(self, "Data Loaded", "Data loaded successfully.")
        except FileNotFoundError:
            QMessageBox.information(self, "No Previous Data", "No previous data found.")


if __name__ == '__main__':
    drug_inventory = {}
    app = QApplication(sys.argv)
    window = PharmacyManagementSystem()
    window.show()
    sys.exit(app.exec_())
