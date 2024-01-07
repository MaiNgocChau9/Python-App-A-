from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox
from PyQt6 import QtWidgets, QtGui, QtCore
from PyQt6 import uic
import sys

class Login(QMainWindow):
    def __init__ (self):
        super().__init__()
        uic.loadUi("D:\Aurora\Python\Python App (A)\Python-App-A-\Buổi 7\Dev\Login.ui", self)
        self.pushButton.clicked.connect(self.the_button_was_clicked)

    def the_button_was_clicked(self):
        if self.lineEdit.text() == "admin@example.com" and self.lineEdit_2.text() == "admin":
                msg_box = QMessageBox()
                msg_box.setWindowTitle("Success")
                msg_box.setText("Đăng nhập thành công!")
                msg_box.exec()
                login_ui.hide()
                main_ui.show()
        else:
                msg_box = QMessageBox()
                msg_box.setWindowTitle("Lỗi")
                msg_box.setIcon(QMessageBox.Icon.Warning)
                msg_box.setText("Email hoặc mật khẩu sai")
                msg_box.exec()

class Register(QMainWindow):
    def __init__ (self):
        super().__init__()
        uic.loadUi("D:\Aurora\Python\Python App (A)\Python-App-A-\Buổi 7\Dev\Register.ui", self)
        self.pushButton.clicked.connect(self.the_button_was_clicked)

    def the_button_was_clicked(self):
        if self.lineEdit.text() == "" or self.lineEdit_2.text() == "":
            msg_box = QMessageBox()
            msg_box.setWindowTitle("Lỗi")
            msg_box.setIcon(QMessageBox.Icon.Warning)
            msg_text = "Vui lòng nhập đầy đủ thông tin đăng ký!"
            msg_box.setText(msg_text)
            msg_box.exec()
        else:
            msg_box = QMessageBox()
            msg_box.setWindowTitle("Thành công")
            msg_text = "Tài khoản đã được tạo! (Đó là trên lý thuyết, thực tế thì tương lai sẽ thử MySQL)\n" + f"Email: {self.lineEdit.text()}\nPassword: {self.lineEdit_2.text()}"
            msg_box.setText(msg_text)
            msg_box.exec()

class Main(QMainWindow):
    def __init__ (self):
        super().__init__()
        uic.loadUi("D:\Aurora\Python\Python App (A)\Python-App-A-\Buổi 7\Dev\Main.ui", self)
        self.pushButton.clicked.connect(self.the_button_was_clicked)

    def the_button_was_clicked(self):
        print("Clicked!")


app = QApplication(sys.argv)

# Các cửa sổ
login_ui = Login()
register_ui = Register()
main_ui = Main()

# Cửa sổ thực hiện
login_ui.show()
app.exec()