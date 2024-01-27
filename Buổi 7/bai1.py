from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys
from PyQt6 import uic

class Login(QMainWindow):
    def __init__ (self):
        super().__init__()
        # uic.loadUi("D:\Aurora\Python\Python App (A)\Python-App-A-\Buổi 7\Login.ui", self)
        self.setWindowTitle("ChatGPT")

        button = QPushButton("Press Me")
        self.setCentralWidget(button)

        button.setCheckable(True)
        button.clicked.connect(self.the_button_was_clicked)
        
        button1 = QPushButton("Button 1")
        self.setCentralWidget(button1)
        button1.setGeometry(200, 200, 100, 30)

        button1.setCheckable(True)
        button1.clicked.connect(self.the_button_was_clicked)
        button1.clicked.connect(self.the_button_was_toggled)

    def the_button_was_clicked(self):
        print("Clicked!")

    def the_button_was_toggled(self, checked):
        print("Checked?", checked)
                   
app = QApplication(sys.argv)
my_login_ui = Login()
my_login_ui.show()
app.exec()