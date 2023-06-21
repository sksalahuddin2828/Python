import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QPixmap

class NetflixLogo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 300, 300)
        self.setWindowTitle('Netflix Logo')

        # Create a QLabel to display the logo image
        self.logo_label = QLabel(self)
        self.logo_label.setGeometry(50, 50, 200, 200)

        # Load the Netflix logo image
        pixmap = QPixmap('netflix_logo.png')

        # Set the scaled logo image to the QLabel
        self.logo_label.setPixmap(pixmap.scaled(200, 200))

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    netflix_logo = NetflixLogo()
    sys.exit(app.exec_())
