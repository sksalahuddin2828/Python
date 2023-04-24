import requests
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Sk. Salahuddin Morning 01 Batch')
        self.setFixedSize(550, 300)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.title_label = QLabel('আবহাওয়ার তথ্য')
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.setFont(QFont('Arial', 18))
        self.layout.addWidget(self.title_label)
        self.input_layout = QHBoxLayout()
        self.input_label = QLabel('শহরের নাম লিখুন:')      
        self.input_label.setFont(QFont('Arial', 12))
        self.input_edit = QLineEdit()
        self.input_edit.setPlaceholderText('ইংরেজিতে দিন')
        self.input_edit.setStyleSheet('padding: 5px; border: 1px solid gray; border-radius: 5px')
        self.input_edit.setFont(QFont('Arial', 12))
        self.input_layout.addWidget(self.input_label)
        self.input_layout.addWidget(self.input_edit)
        self.layout.addLayout(self.input_layout)
        self.submit_button = QPushButton('অনুসন্ধান')
        self.submit_button.setFont(QFont('Arial', 12))
        self.submit_button.clicked.connect(self.update_weather)
        self.layout.addWidget(self.submit_button)
        self.weather_layout = QVBoxLayout()
        self.temperature_label = QLabel()
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.temperature_label.setFont(QFont('Arial', 14))
        self.weather_layout.addWidget(self.temperature_label)
        self.description_label = QLabel()
        self.description_label.setAlignment(Qt.AlignCenter)
        self.description_label.setFont(QFont('Arial', 14))
        self.weather_layout.addWidget(self.description_label)
        self.layout.addLayout(self.weather_layout)
    def update_weather(self):
        city = self.input_edit.text()
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&units=metric'
        response = requests.get(url)
        data = response.json()
        if data.get('main') is None:
            self.temperature_label.setText('City not found')
            self.description_label.setText('')
        else:
            temp = data['main']['temp']
            description = data['weather'][0]['description']
            self.temperature_label.setText(f'Temperature: {temp} °C')
            self.description_label.setText(f'Description: {description.title()}')
if __name__ == '__main__':
    app = QApplication([])
    weather_app = WeatherApp()
    weather_app.show()
    app.exec_()
