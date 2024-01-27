from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox
from PyQt6 import QtWidgets, QtGui, QtCore
import sys

class Login(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(652, 504)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(340, 190, 301, 51))
        self.lineEdit.setStyleSheet("QLineEdit{\n"
"    padding: 10px;\n"
"    border: 2px solid rgb(214, 214, 214);\n"
"    border-radius: 20px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"    padding: 10px;\n"
"    border: 2px solid gray;\n"
"    border-radius: 20px;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"    padding: 10px;\n"
"    border: 2px solid gray;\n"
"    border-radius: 20px;\n"
"}")
        self.lineEdit.setInputMask("")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(340, 300, 301, 51))
        self.lineEdit_2.setStyleSheet("QLineEdit{\n"
"    padding: 10px;\n"
"    border: 2px solid rgb(214, 214, 214);\n"
"    border-radius: 20px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"    padding: 10px;\n"
"    border: 2px solid gray;\n"
"    border-radius: 20px;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"    padding: 10px;\n"
"    border: 2px solid gray;\n"
"    border-radius: 20px;\n"
"}")
        self.lineEdit_2.setInputMask("")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(350, 160, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(False)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(350, 270, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(False)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 321, 511))
        self.label_3.setStyleSheet("background-color: rgb(116, 170, 156);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 100, 291, 291))
        self.label_4.setStyleSheet("border-image: url(:/ChatGPT icon/C:/Users/Windows/Downloads/download.png)")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(397, 60, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(430, 380, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
"    background-color: white;\n"
"    border: 1px solid rgb(116, 170, 156);\n"
"    border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: white;\n"
"    border: 2px solid rgb(116, 170, 156);\n"
"    border-radius: 20px;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(370, 470, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(515, 470, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(3, 148, 252);")
        self.label_7.setObjectName("label_7")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton.clicked.connect(self.the_button_was_clicked)
        self.label_7.mousePressEvent = lambda event: self.register()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "example@example.com"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Password"))
        self.label.setText(_translate("MainWindow", "Email"))
        self.label_2.setText(_translate("MainWindow", "Password"))
        self.label_5.setText(_translate("MainWindow", "Welcome back"))
        self.pushButton.setText(_translate("MainWindow", "Login"))
        self.label_6.setText(_translate("MainWindow", "Do not have an account?"))
        self.label_7.setText(_translate("MainWindow", "Register now"))

    def the_button_was_clicked(self):
        if self.lineEdit.text() == "admin@example.com" and self.lineEdit_2.text() == "admin":
                msg_box = QMessageBox()
                msg_box.setWindowTitle("Success")
                msg_box.setText("Đăng nhập thành công! \nE sẽ ko nói là e lười làm 1 cái màn hình khác đâu =))")
                msg_box.exec()
        else:
                msg_box = QMessageBox()
                msg_box.setWindowTitle("Lỗi")
                msg_box.setIcon(QMessageBox.Icon.Warning)
                msg_box.setText("Email hoặc mật khẩu sai")
                msg_box.exec()

    def register(self):
        ui = Register()
        ui.setupUi(MainWindow)


class Register(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(652, 504)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(340, 190, 301, 51))
        self.lineEdit.setStyleSheet("QLineEdit{\n"
"    padding: 10px;\n"
"    border: 2px solid rgb(214, 214, 214);\n"
"    border-radius: 20px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"    padding: 10px;\n"
"    border: 2px solid gray;\n"
"    border-radius: 20px;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"    padding: 10px;\n"
"    border: 2px solid gray;\n"
"    border-radius: 20px;\n"
"}")
        self.lineEdit.setInputMask("")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(340, 300, 301, 51))
        self.lineEdit_2.setStyleSheet("QLineEdit{\n"
"    padding: 10px;\n"
"    border: 2px solid rgb(214, 214, 214);\n"
"    border-radius: 20px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"    padding: 10px;\n"
"    border: 2px solid gray;\n"
"    border-radius: 20px;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"    padding: 10px;\n"
"    border: 2px solid gray;\n"
"    border-radius: 20px;\n"
"}")
        self.lineEdit_2.setInputMask("")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(350, 160, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(False)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(350, 270, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(False)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 321, 511))
        self.label_3.setStyleSheet("background-color: rgb(116, 170, 156);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 100, 291, 291))
        self.label_4.setStyleSheet("border-image: url(:/ChatGPT icon/C:/Users/Windows/Downloads/download.png)")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(397, 60, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(430, 380, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
"    background-color: white;\n"
"    border: 1px solid rgb(116, 170, 156);\n"
"    border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: white;\n"
"    border: 2px solid rgb(116, 170, 156);\n"
"    border-radius: 20px;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(370, 470, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(515, 470, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(3, 148, 252);")
        self.label_7.setObjectName("label_7")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton.clicked.connect(self.the_button_was_clicked)
        self.label_7.mousePressEvent = lambda event: self.login()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "example@example.com"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Password"))
        self.label.setText(_translate("MainWindow", "Email"))
        self.label_2.setText(_translate("MainWindow", "Password"))
        self.label_5.setText(_translate("MainWindow", "Welcome"))
        self.pushButton.setText(_translate("MainWindow", "Register"))
        self.label_6.setText(_translate("MainWindow", "Already have an account?"))
        self.label_7.setText(_translate("MainWindow", "Login now"))
    
    def the_button_was_clicked(self):
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Success")
        msg_text = f"Email: {self.lineEdit.text()}\nPassword: {self.lineEdit_2.text()}"
        msg_box.setText(msg_text)
        msg_box.exec()
    def login(self):
        ui = Login()
        ui.setupUi(MainWindow)

app = QApplication(sys.argv)
MainWindow = QMainWindow()
ui = Login()
ui.setupUi(MainWindow)
MainWindow.show()
app.exec()