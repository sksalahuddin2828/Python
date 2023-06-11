import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import QTimer, Qt, QDateTime, QPropertyAnimation, QRect
class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sk. Salahuddin Morning 01 Batch >> Digital Clock")
        self.layout = QVBoxLayout(self)
        self.setStyleSheet("background-color: #272727;")
        self.date_label = QLabel()
        self.date_label.setAlignment(Qt.AlignCenter)
        self.date_label.setStyleSheet("font-size: 60px; background-color: #272727; color: #ffffff;")
        self.layout.addWidget(self.date_label)
        self.time_label = QLabel()
        self.time_label.setAlignment(Qt.AlignCenter)
        self.time_label.setStyleSheet("font-size: 200px; background-color: #272727; color: #F39C12;")
        self.layout.addWidget(self.time_label)
        self.temperature_label = QLabel()
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.temperature_label.setStyleSheet("font-size: 45px; background-color: #272727; color: #ffffff;")
        self.layout.addWidget(self.temperature_label)
        self.unit_button = QPushButton("Switch to Fahrenheit")
        self.unit_button.clicked.connect(self.toggle_units)
        self.layout.addWidget(self.unit_button)
        self.unit_button.setStyleSheet("background-color: #3498DB; font-weight:bold; color: #ffffff;")
        gradient = "background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #3498DB, stop:1 #E74C3C);"
        self.setStyleSheet(f"QWidget {{ {gradient} }}")
        self.units = "metric"
        self.toggle_units()
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_clock)
        self.timer.start(1000)
        self.time_animation = QPropertyAnimation(self.time_label, b"geometry")
        self.time_animation.setDuration(1000)
        self.time_animation.setStartValue(QRect(0, 0, 0, self.time_label.height()))
        self.time_animation.setEndValue(QRect(0, 0, self.width(), self.time_label.height()))
        self.time_animation.start()
        self.date_animation = QPropertyAnimation(self.date_label, b"geometry")
        self.date_animation.setDuration(1000)
        self.date_animation.setStartValue(QRect(0, self.time_label.height(), 0, self.date_label.height()))
        self.date_animation.setEndValue(QRect(0, self.time_label.height(), self.width(), self.date_label.height()))
        self.date_animation.start()
        self.temperature_animation = QPropertyAnimation(self.temperature_label, b"geometry")
        self.temperature_animation.setDuration(1000)
        self.temperature_animation.setStartValue(QRect(0, self.time_label.height() + self.date_label.height(), 0, self.temperature_label.height()))
        self.temperature_animation.setEndValue(QRect(0, self.time_label.height() + self.date_label.height(), self.width(), self.temperature_label.height()))
        self.temperature_animation.start()
    def get_temperature(self):
        api_key = "API KEY" 
        city = "Khulna"
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&units={self.units}"
        response = requests.get(url)
        data = response.json()
        temperature = data["main"]["temp"]
        return temperature
    def update_clock(self):
        now = QDateTime.currentDateTime()
        date = now.toString("dddd, MMMM dd, yyyy") 
        time = now.toString("hh:mm:ss AP") 
        temperature = self.get_temperature()
        temperature_celsius = f"{temperature:.1f} °C" 
        temperature_fahrenheit = f"{temperature * 9/5 + 32:.1f} °F" 
        temperature_str = f"{temperature_celsius} / {temperature_fahrenheit}" 
        self.date_label.setText(date)
        self.time_label.setText(time)
        self.temperature_label.setText(temperature_str)
    def toggle_units(self):
        if self.units == "metric":
            self.units = "imperial"
            self.unit_button.setText("Switch to Celsius")
        else:
            self.units = "metric"
            self.unit_button.setText("Switch to Fahrenheit")
app = QApplication(sys.argv)
window = DigitalClock()
window.show()
sys.exit(app.exec_())
