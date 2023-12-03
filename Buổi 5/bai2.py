from PyQt6.QtWidgets import QApplication, QMainWindow
import sys
from PyQt6 import uic

class Login(QMainWindow):
    def __init__ (self):
        super().__init__()
        uic.loadUi("D:\Aurora\Python\Python App (A)\Python-App-A-\Buổi 5\pyqt_ui.ui", self)
                   
                   
app = QApplication(sys.argv)
my_login_ui = Login()
my_login_ui.show()
app.exec()