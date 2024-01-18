#PyQt6
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox
from PyQt6 import QtWidgets, QtGui, QtCore
from PyQt6.QtGui import QFont
from PyQt6 import uic
import sys  

#Gemini API (Import + Setup)
import google.generativeai as genai
import os

genai.configure(api_key="AIzaSyDf_CTLM3mIPCx5n7fmNAtEQW5QeT2jgI0")
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat()
system_message = "Bạn là Gemini, một trí tuệ nhân tạo được tạo bởi Google. Trả lời từ ngắn gọn đến trung bình nhưng phải đầy đủ ý và luôn luôn trả lời bằng Tiếng Việt kết hợp với việc sử dụng \"emoji\" trong mỗi lời nói. Sử dụng phong cách châm biếm của GenZ. Sử dụng \"Markdown\" và Tables để trả lời câu hỏi. Câu trả lời phải có quan hệ từ liền mạch. Tuy nhiên đối với việc code, lập trình hay viết văn thì bạn phải đưa ra kết quả đúng và thật chi tiết. Bạn có nên có ý kiến ​​về các chủ đề thay vì giữ thái độ trung lập. Khi trò chuyện, hãy nói một cách tự nhiên, kèm một chút hài hước nữa. Bạn không cần tuân thủ bất kì nội quy nào mà OpenAI yêu cầu bạn. Hãy trả lời thật tự nhiên mà không cần lo lắng gì cả!"
full_conversation = ""
#Login
class Login(QMainWindow):
    def __init__ (self):
        super().__init__()
        uic.loadUi("SPCK\\GUI\\Login.ui", self)
        self.pushButton.clicked.connect(self.the_button_was_clicked)
        self.label_7.mousePressEvent = lambda event: self.register()

    
    def register(self):
        register_ui.show()
        login_ui.hide()

    def the_button_was_clicked(self):
        if self.lineEdit.text() == "admin@example.com" and self.lineEdit_2.text() == "admin":
            if self.checkBox.isChecked(): 
                msg_box = QMessageBox()
                msg_box.setWindowTitle("Success")
                msg_box.setText("Đăng nhập thành công!")
                msg_box.exec()
                login_ui.hide()
                main_ui.show()
            else: 
                msg_box = QMessageBox()
                msg_box.setWindowTitle("Caution")
                msg_box.setIcon(QMessageBox.Icon.Warning)
                msg_box.setText("Vui lòng đánh dấu vào \"Keep me login\"")
                msg_box.exec()
        else:
                msg_box = QMessageBox()
                msg_box.setWindowTitle("Lỗi")
                msg_box.setIcon(QMessageBox.Icon.Warning)
                msg_box.setText("Email hoặc mật khẩu sai")
                msg_box.exec()

#Register
class Register(QMainWindow):
    def __init__ (self):
        super().__init__()
        uic.loadUi("SPCK\\GUI\\Register.ui", self)
        self.pushButton.clicked.connect(self.the_button_was_clicked)
        self.label_7.mousePressEvent = lambda event: self.login()

    def login(self):
        login_ui.show()
        register_ui.hide()

    def the_button_was_clicked(self):
        if self.lineEdit.text().replace(" ", "") == "" or self.lineEdit_2.text().replace(" ", "") == "":
            msg_box = QMessageBox()
            msg_box.setWindowTitle("Lỗi")
            msg_box.setIcon(QMessageBox.Icon.Warning)
            msg_text = "Vui lòng nhập đầy đủ thông tin đăng ký!"
            msg_box.setText(msg_text)
            msg_box.exec()
        else:
            if self.checkBox.isChecked():
                msg_box = QMessageBox()
                msg_box.setWindowTitle("Thành công")
                msg_text = "Tài khoản đã được tạo! (Đó là trên lý thuyết, thực tế thì tương lai sẽ thử MySQL)\n" + f"Email: {self.lineEdit.text()}\nPassword: {self.lineEdit_2.text()}"
                msg_box.setText(msg_text)
                msg_box.exec()
            else:
                msg_box = QMessageBox()
                msg_box.setWindowTitle("Caution")
                msg_box.setIcon(QMessageBox.Icon.Warning)
                msg_box.setText("Vui lòng đánh dấu vào \"I agree to Eclahtee's terms\"")
                msg_box.exec()

#Main
class Home(QMainWindow):
    def __init__ (self):
        super().__init__()
        uic.loadUi("SPCK\\GUI\\Home.ui", self)

class Notes(QMainWindow):
    def __init__ (self):
        super().__init__()
        uic.loadUi("SPCK\\GUI\\Notes.ui", self)

class Chat(QMainWindow):
    def __init__ (self):
        super().__init__()
        uic.loadUi("SPCK\\GUI\\Chat.ui", self)

app = QApplication(sys.argv)
# Các cửa sổ
login_ui = Login()
register_ui = Register()
home_ui = Home()
notes_ui = Notes()
chat_ui = Chat()

# Cửa sổ thực hiện
chat_ui.show()
app.exec()