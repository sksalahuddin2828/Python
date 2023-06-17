# pip install PyQt5

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QGridLayout, QPushButton, QLineEdit
from PyQt5.QtCore import Qt
import math

class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Scientific Calculator")
        self.setMinimumSize(300, 400)
        self.setFixedSize(self.size())
        self.generalLayout = QVBoxLayout()
        self.centralWidget = QWidget(self)
        self.centralWidget.setLayout(self.generalLayout)
        self.setCentralWidget(self.centralWidget)
        self.createDisplay()
        self.createButtons()

def createDisplay(self):
    self.display = QLineEdit()
    self.display.setFixedHeight(35)
    self.display.setAlignment(Qt.AlignRight)
    self.generalLayout.addWidget(self.display)

def createButtons(self):
    self.buttonsLayout = QGridLayout()
    buttons = [
        ['7', '8', '9', '/'],
        ['4', '5', '6', '*'],
        ['1', '2', '3', '-'],
        ['0', '.', '=', '+'],
        ['sin', 'cos', 'tan', 'sqrt'],
        ['(', ')', 'log', 'exp']
    ]
    for row, buttonRow in enumerate(buttons):
        for col, buttonLabel in enumerate(buttonRow):
            button = QPushButton(buttonLabel)
            button.setFixedSize(60, 40)
            self.buttonsLayout.addWidget(button, row, col)
    self.generalLayout.addLayout(self.buttonsLayout)

def connectButtons(self):
    buttons = self.buttonsLayout.findChildren(QPushButton)
    for button in buttons:
        buttonText = button.text()
        if buttonText == '=':
            button.clicked.connect(self.calculateResult)
        else:
            button.clicked.connect(self.appendToDisplay)

def appendToDisplay(self):
    clickedButton = self.sender()
    self.display.setText(self.display.text() + clickedButton.text())

def calculateResult(self):
    expression = self.display.text()
    try:
        result = eval(expression)
        self.display.setText(str(result))
    except Exception:
        self.display.setText("Error")

if __name__ == "__main__":
    app = QApplication([])
    calculator = Calculator()
    calculator.show()
    app.exec()
