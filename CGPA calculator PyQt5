# CGPA (Cumulative Grade Point Average)

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QFormLayout, QLabel, QLineEdit, QPushButton

class CGPACalculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CGPA Calculator")
        self.setMinimumSize(300, 200)
        
        self.centralWidget = QWidget(self)
        self.setCentralWidget(self.centralWidget)
        
        self.generalLayout = QVBoxLayout()
        self.centralWidget.setLayout(self.generalLayout)
        
        self.createForm()
        self.createButton()
        
    def createForm(self):
        self.formLayout = QFormLayout()
        
        self.subjectsLabel = QLabel("Number of Subjects:")
        self.subjectsLineEdit = QLineEdit()
        
        self.gradeLabel = QLabel("Grades (Separated by comma):")
        self.gradeLineEdit = QLineEdit()
        
        self.formLayout.addRow(self.subjectsLabel, self.subjectsLineEdit)
        self.formLayout.addRow(self.gradeLabel, self.gradeLineEdit)
        
        self.generalLayout.addLayout(self.formLayout)
    
    def createButton(self):
        self.calculateButton = QPushButton("Calculate CGPA")
        self.calculateButton.clicked.connect(self.calculateCGPA)
        self.generalLayout.addWidget(self.calculateButton)
    
    def calculateCGPA(self):
        subjects = self.subjectsLineEdit.text()
        grades = self.gradeLineEdit.text()
        
        try:
            subjects = int(subjects)
            grade_list = [int(grade) for grade in grades.split(",")]
            
            total_grade_points = sum(grade_list)
            cgpa = total_grade_points / subjects
            
            result = f"CGPA: {cgpa:.2f}"
        except (ValueError, ZeroDivisionError):
            result = "Invalid input!"
        
        self.resultLabel = QLabel(result)
        self.generalLayout.addWidget(self.resultLabel)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    calculator = CGPACalculator()
    calculator.show()
    sys.exit(app.exec_())
