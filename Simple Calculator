import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QGridLayout, QPushButton, QLineEdit

class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setMinimumSize(250, 300)
        
        self.centralWidget = QWidget(self)
        self.setCentralWidget(self.centralWidget)
        
        self.generalLayout = QVBoxLayout()
        self.centralWidget.setLayout(self.generalLayout)
        
        self.createDisplay()
        self.createButtons()
    
    def createDisplay(self):
        self.display = QLineEdit()
        self.display.setFixedHeight(35)
        self.generalLayout.addWidget(self.display)
    
    def createButtons(self):
        self.buttonsLayout = QGridLayout()
        
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]
        
        row, col = 0, 0
        
        for button in buttons:
            buttonObj = QPushButton(button)
            buttonObj.setFixedSize(40, 40)
            self.buttonsLayout.addWidget(buttonObj, row, col)
            
            col += 1
            if col > 3:
                col = 0
                row += 1
        
        self.generalLayout.addLayout(self.buttonsLayout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec_())
