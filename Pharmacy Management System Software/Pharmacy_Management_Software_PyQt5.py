# Pharmacy Management Software implemented using PyQt5:

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QLineEdit, QPushButton

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
        self.add_button = QPushButton("Add Drug")
        self.add_button.clicked.connect(self.add_drug)

        # Create a layout and add widgets to it
        layout = QVBoxLayout()
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_input)
        layout.addWidget(self.price_label)
        layout.addWidget(self.price_input)
        layout.addWidget(self.quantity_label)
        layout.addWidget(self.quantity_input)
        layout.addWidget(self.add_button)

        # Create a central widget and set the layout
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def add_drug(self):
        name = self.name_input.text()
        price = float(self.price_input.text())
        quantity = int(self.quantity_input.text())
        # Add the drug to the inventory or perform necessary actions
        print(f"Drug added: Name={name}, Price={price}, Quantity={quantity}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PharmacyManagementSystem()
    window.show()
    sys.exit(app.exec_())
