from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
class MyWebBrowser():
    def __init__(self):  
        self.window = QWidget()
        self.window.setWindowTitle("Sk. Salahuddin - Morning 01 Batch")
        self.layout = QVBoxLayout()
        self.horizontal = QHBoxLayout()
        self.search_bar = QLineEdit()
        self.search_bar.setPlaceholderText("Search Google")
        self.search_bar.setMinimumHeight(50)
        self.search_bar.setStyleSheet("""
            QLineEdit {
                border: 2px solid #4a4a4a;
                border-radius: 25px;
                padding-left: 15px;
                padding-right: 50px;
                font-size: 18px;
                font-family: Arial;
            }
            QLineEdit:focus {
                border: 2px solid #0080ff;
            }
        """)
        self.go_btn = QPushButton("GO")
        self.go_btn.setIcon(QIcon("go.png"))
        self.go_btn.setIconSize(QSize(32, 32))
        self.go_btn.setMinimumHeight(50)
        self.go_btn.setFixedSize(50, 50)
        self.go_btn.setStyleSheet("""
            QPushButton {
                border: none;
                background-color: #0080ff;
                border-radius: 25px;
            }
            QPushButton:hover {
                background-color: #005ce6;
            }
            QPushButton:pressed {
                background-color: #0047b3;
            }
        """)
        self.back_btn = QPushButton("<")
        self.back_btn.setIcon(QIcon("back.png"))
        self.back_btn.setIconSize(QSize(32, 32))
        self.back_btn.setMinimumHeight(50)
        self.back_btn.setFixedSize(50, 50)
        self.back_btn.setStyleSheet("""
            QPushButton {
                border: none;
                background-color: #4a4a4a;
                border-radius: 25px;
            }
            QPushButton:hover {
                background-color: #333333;
            }
            QPushButton:pressed {
                background-color: #1a1a1a;
            }
        """)
        self.forward_btn = QPushButton(">")
        self.forward_btn.setIcon(QIcon("forward.png"))
        self.forward_btn.setIconSize(QSize(32, 32))
        self.forward_btn.setMinimumHeight(50)
        self.forward_btn.setFixedSize(50, 50)
        self.forward_btn.setStyleSheet("""
            QPushButton {
                border: none;
                background-color: #4a4a4a;
                border-radius: 25px;
            }
            QPushButton:hover {
                background-color: #333333;
            }
            QPushButton:pressed {
                background-color: #1a1a1a;
            }
        """)
        self.horizontal.addWidget(self.search_bar)
        self.horizontal.addWidget(self.go_btn)
        self.horizontal.addWidget(self.back_btn)
        self.horizontal.addWidget(self.forward_btn)
        self.browser = QWebEngineView()
        self.go_btn.clicked.connect(lambda: self.navigate(self.search_bar.text()))
        self.back_btn.clicked.connect(self.browser.back)
        self.forward_btn.clicked.connect(self.browser.forward)
        self.search_bar.returnPressed.connect(lambda: self.navigate(self.search_bar.text()))
        self.layout.addLayout(self.horizontal)
        self.layout.addWidget(self.browser)
        self.browser.setUrl(QUrl("https://www.google.com/"))
        self.window.setLayout(self.layout)
        self.window.show()
    def navigate(self, url):
        if not url.startswith("http"):
            url = "https://www.google.com/search?q=" + url
            self.search_bar.setText(url)
        self.browser.setUrl(QUrl(url))
app = QApplication([])
window = MyWebBrowser()
app.exec_()
