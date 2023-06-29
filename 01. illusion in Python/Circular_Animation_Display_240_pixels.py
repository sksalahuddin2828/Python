# Rotating Pattern Viewer
# Circular Animation Display

import sys
import math
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt, QTimer

class RotatingPatternWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.pi = math.pi
        self.circle = self.pi * 2
        self.length = 12
        self.half_length = self.length // 2
        self.cx = 115
        self.cy = 115
        self.w = 90.0
        self.h = 90.0
        self.step = 0.0

        self.setWindowTitle("Rotating Pattern")
        self.resize(240, 240)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateAnimation)
        self.timer.start(100)

    def updateAnimation(self):
        self.step -= 0.09
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Clear the background
        painter.fillRect(self.rect(), Qt.black)

        for i in range(self.length):
            a = (i / self.length) * self.circle
            x = self.cx + round(math.cos(a) * self.w)
            y = self.cy + round(math.sin(a) * self.h)
            self.drawCircle(painter, x, y, 'white')

            if i < self.half_length:
                continue

            range_val = math.cos(a + self.step)
            x = self.cx + round(math.cos(a) * (self.w - 1) * range_val)
            y = self.cy + round(math.sin(a) * (self.h - 1) * range_val)
            self.drawCircle(painter, x, y, 'white')

    def drawCircle(self, painter, x, y, color):
        painter.setPen(QPen(QColor(color)))
        painter.setBrush(QColor(color))
        painter.drawEllipse(x - 5, y - 5, 10, 10)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = RotatingPatternWidget()
    window.show()
    sys.exit(app.exec_())
