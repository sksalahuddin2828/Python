import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import QTimer, Qt, QDateTime
class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sk. Salahuddin Morning 01 Batch >> Digital Clock")
        self.layout = QVBoxLayout(self)
        #self.setStyleSheet("background-color: #272727;")
        self.date_label = QLabel()
        self.date_label.setAlignment(Qt.AlignCenter)
        self.date_label.setStyleSheet("font-size: 60px;")
        self.layout.addWidget(self.date_label)
        self.time_label = QLabel()
        self.time_label.setAlignment(Qt.AlignCenter)
        self.time_label.setStyleSheet("font-size: 200px;")
        self.layout.addWidget(self.time_label)
        self.temperature_label = QLabel()
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.temperature_label.setStyleSheet("font-size: 45px;")
        self.layout.addWidget(self.temperature_label)
        self.unit_button = QPushButton("Switch to Fahrenheit")
        self.unit_button.clicked.connect(self.toggle_units)
        self.layout.addWidget(self.unit_button)
        #self.unit_button.setStyleSheet("background-color: orange; font-weight:bold; color: #ffffff;")
        self.units = "metric"
        self.toggle_units()
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_clock)
        self.timer.start(1000)
    def get_temperature(self):
        api_key = "{key}"
        city = "{city}"
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&units={self.units}"
        response = requests.get(url)
        data = response.json()
        temperature = data["main"]["temp"]
        return temperature
    def update_clock(self):
        now = QDateTime.currentDateTime()
        date = now.toString("dddd, MMMM dd, yyyy") # Format the date as Month day, Year
        time = now.toString("hh:mm:ss AP") # Format the time as hh:mm:ss AM/PM
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
