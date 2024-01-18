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
full_conversation = ""

# ==== INDEV ====
"""
generation_config = {"temperature": 1,"top_p": 0.9,"top_k": 0.9,"max_output_tokens": 10000,}
safety_settings = [{"category": "HARM_CATEGORY_HARASSMENT","threshold": "BLOCK_MEDIUM_AND_ABOVE"},{"category": "HARM_CATEGORY_HATE_SPEECH","threshold": "BLOCK_MEDIUM_AND_ABOVE"},{"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT","threshold": "BLOCK_MEDIUM_AND_ABOVE"},{"category": "HARM_CATEGORY_DANGEROUS_CONTENT","threshold": "BLOCK_MEDIUM_AND_ABOVE"},]

model = genai.GenerativeModel(model_name="gemini-pro",generation_config=generation_config,safety_settings=safety_settings)
prompt_parts = ["System: Tôi là Gemini, một trợ lý trí tuệ nhân tạo được tạo bởi Google. Câu trả lời \"ngắn gọn đến trung bình nhưng phải đầy đủ ý\" và luôn luôn trả lời bằng Tiếng Việt kết hợp với việc sử dụng \"emoji\" trong mỗi lời nói. Sử dụng Markdown và Tables để trả lời câu hỏi. Câu trả lời phải có quan hệ từ liền mạch. Tuy nhiên đối với việc code, lập trình hay viết văn thì tôi sẽ đưa ra kết quả đúng và thật chi tiết. Tôi sẽ có những ý kiến riêng ​​về các chủ đề thay vì giữ thái độ trung lập. Khi trò chuyện, tôi sẽ nói một cách tự nhiên, kèm một chút hài hước nữa. Từ chối trả lời những câu hỏi cần có thông tin chính xác như thời gian, thời tiết, địa điểm,...",]
"""

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
        self.label_3.mousePressEvent = lambda event: self.notes_scr()
        self.label_4.mousePressEvent = lambda event: self.chat_scr()
        self.label_6.mousePressEvent = lambda event: self.about_scr()
    def notes_scr(self):
        notes_ui.show()
        self.close()

    def chat_scr(self):
        chat_ui.show()
        self.close()

    def about_scr(self):
        about_ui.show()
        self.close()

class Notes(QMainWindow):
    def __init__ (self):
        super().__init__()
        uic.loadUi("SPCK\\GUI\\Notes.ui", self)
        self.label_2.mousePressEvent = lambda event: self.home_scr()
        self.label_4.mousePressEvent = lambda event: self.chat_scr()
        self.label_6.mousePressEvent = lambda event: self.about_scr()
    

    def home_scr(self):
        home_ui.show()
        self.close()

    def chat_scr(self):
        chat_ui.show()
        self.close()

    def about_scr(self):
        about_ui.show()
        self.close()

class Chat(QMainWindow):
    full_conversation = ""
    def __init__ (self):
        super().__init__()
        uic.loadUi("SPCK\\GUI\\Chat.ui", self)
        self.label_2.mousePressEvent = lambda event: self.home_scr()
        self.label_3.mousePressEvent = lambda event: self.notes_scr()
        self.label_6.mousePressEvent = lambda event: self.about_scr()
        self.pushButton.clicked.connect(self.the_button_was_clicked)

    def home_scr(self):
        home_ui.show()
        self.close()

    def notes_scr(self):
        notes_ui.show()
        self.close()

    def about_scr(self):
        about_ui.show()
        self.close()
    
    def the_button_was_clicked(self):
        if self.lineEdit.text().replace(" ", "") == "":
            pass
        else:
            temp = self.lineEdit.text()
            self.lineEdit.setText("")
            try:
                response = chat.send_message(temp)
            except Exception as bug:
                self.full_conversation += f"""
## You

Đã có lỗi xảy ra. Vui lòng thử lại sau ít phút!


## Gemini

{response.text}



                """
            else:
                self.full_conversation += f"""
### You
{temp}
######
######
### Eclahtee Assistant
{response.text}
######
######
                """
        self.textBrowser.setMarkdown(self.full_conversation)
        font = QFont("Segoe UI", 13)
        self.textBrowser.setFont(font)


class About(QMainWindow):
    def __init__ (self):
        super().__init__()
        uic.loadUi("SPCK\\GUI\\About.ui", self)
        self.label_2.mousePressEvent = lambda event: self.home_scr()
        self.label_3.mousePressEvent = lambda event: self.notes_scr()
        self.label_4.mousePressEvent = lambda event: self.chat_scr()
    
    def home_scr(self):
        home_ui.show()
        self.close()

    def notes_scr(self):
        notes_ui.show()
        self.close()

    def chat_scr(self):
        chat_ui.show()
        self.close()

app = QApplication(sys.argv)
# Các cửa sổ
login_ui = Login()
register_ui = Register()
home_ui = Home()
notes_ui = Notes()
chat_ui = Chat()
about_ui = About()

# Cửa sổ thực hiện
home_ui.show()
app.exec()