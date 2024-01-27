from PyQt6.QtWidgets import QApplication, QMainWindow
import sys
from PyQt6 import uic

class Login(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("D:\Aurora\Python\Python App (A)\Python-App-A-\Buổi 7\BTVN\Register.ui", self)
        self.button.clicked.connect(self.the_button_was_clicked)  # Indent this line

    def the_button_was_clicked(self):  # Indent this line
        print("Clicked!")

class Regíter(QMainWindow):
    def __init__ (self):
        super().__init__()
        uic.loadUi("D:\Aurora\Python\Python App (A)\Python-App-A-\Buổi 7\BTVN\Register.ui", self)
                   
app = QApplication(sys.argv)
my_login_ui = Login()
my_login_ui.show()
app.exec()