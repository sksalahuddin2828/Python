from math import pi, cos, sin
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QGraphicsView
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QBrush, QColor, QPen

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Rotating Pattern")
        self.setGeometry(100, 100, 1020, 1020)  
        self.scene = QGraphicsScene()
        self.view = QGraphicsView(self.scene, self)
        self.view.setGeometry(0, 0, 1020, 1020) 
        self.view.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.view.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.view.setBackgroundBrush(QBrush(QColor(0, 0, 0)))
        self.timer = QTimer(self)
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.animateWorld)
        self.timer.start()
        self.angle = 0  

    def animateWorld(self):
        self.scene.clear()
        self.createBase()
        self.angle += 0.15  
        circle = pi * 2
        length = 10                                       
        half_length = length // 2
        cx = 510  
        cy = 510  
        w = 450  
        h = 450  

        for i in range(length):
            a = (i / length) * circle
            x = cx + round(cos(a) * w)
            y = cy + round(sin(a) * h)
            self.drawCircle(x, y, 15, QColor(255, 255, 255))  

            if i >= half_length:
                inner_angle = a + self.angle  
                range_val = cos(inner_angle)
                x = cx + round(cos(a) * (w - 1) * range_val)
                y = cy + round(sin(a) * (h - 1) * range_val)
                self.drawCircle(x, y, 15, QColor(255, 255, 255))  

    def createBase(self):
        cx = 510  
        cy = 510  
        radius = 480  
        pen = QPen(QColor(255, 255, 255))
        pen.setWidth(2)                                  

        self.drawCircle(cx, cy, radius, QColor(0, 0, 0))
        for i in range(10):       
            angle = (i / 10) * 2 * pi                      
            x = cx + radius * cos(angle)
            y = cy + radius * sin(angle)
            self.scene.addLine(cx, cy, x, y, pen)

    def drawCircle(self, x, y, radius, color):
        pen = QPen(color)
        pen.setWidth(0)
        brush = QBrush(color)
        self.scene.addEllipse(x - radius, y - radius, radius * 2, radius * 2, pen, brush)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
