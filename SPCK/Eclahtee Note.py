#PyQt6
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox, QLabel, QListWidget, QInputDialog
from PyQt6 import QtWidgets, QtGui, QtCore
from PyQt6.QtGui import QFont
from PyQt6 import uic
import sys  

#Gemini API (Import + Setup)
import google.generativeai as genai
import os

genai.configure(api_key="AIzaSyDf_CTLM3mIPCx5n7fmNAtEQW5QeT2jgI0")

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
    all_task = []
    with open("SPCK\\data\\todo_list.ecl", 'r') as file: 
        all_task = file.read().splitlines() 
    def __init__ (self):
        super().__init__()
        uic.loadUi("SPCK\\GUI\\Home.ui", self)
        
        # Font
        font = QFont("Segoe UI", 14)
        font.setBold(True)
        font_button = QFont("Segoe UI", 10)
        font_button.setBold(True)
        
        # UI
        self.textBrowser.setMarkdown(""""
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
<html><head><meta name="qrichtext" content="1" /><style type="text/css">
p, li { white-space: pre-wrap; }
</style></head><body style=" font-family:'Segoe UI'; font-size:8.25pt; font-weight:400; font-style:normal;">
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI ';"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:'Segoe UI '; font-size:16pt; font-weight:600;">Vasper Jance</span></p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI '; font-size:8pt; font-weight:600;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:'Segoe UI '; font-size:14pt;">Welcome back, we've missed your smiling face!</span></p></body></html>
        """)
        self.label_9.setFont(font)
        self.label_11.setFont(font)
        self.pushButton_6.setFont(font_button)
        self.pushButton_7.setFont(font_button)
        self.pushButton_2.setFont(font_button)
        self.label_3.mousePressEvent = lambda event: self.notes_scr()
        self.label_4.mousePressEvent = lambda event: self.chat_scr()
        self.label_6.mousePressEvent = lambda event: self.about_scr()
        self.pushButton_7.clicked.connect(self.remove_task)
        self.pushButton_6.clicked.connect(self.add_task)
        for task in self.all_task:
            item = QtWidgets.QListWidgetItem(task)
            item.setFlags(QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled | QtCore.Qt.ItemFlag.ItemIsSelectable)
            item.setCheckState(QtCore.Qt.CheckState.Unchecked)
            self.listWidget.addItem(item)
    
    def remove_task(self):
        currentIndex = self.listWidget.currentRow()
        self.listWidget.takeItem(currentIndex)
        item_list = [self.listWidget.item(i).text() for i in range(self.listWidget.count())]
        with open("SPCK\\data\\todo_list.ecl", 'w') as file:
            for item in item_list:
                file.write(f"{item}\n")

    def add_task(self):
        task_name = QInputDialog.getText(self, "New Taks", "Enter Task")[0]
        if task_name != "":
            item = QtWidgets.QListWidgetItem(task_name)
            item.setFlags(QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled | QtCore.Qt.ItemFlag.ItemIsSelectable)
            item.setCheckState(QtCore.Qt.CheckState.Unchecked)
            self.listWidget.addItem(item)
            with open("SPCK\\data\\todo_list.ecl", 'a') as file:
                file.write(f"{task_name}\n")

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
    """
    Temperature = Mức độ sáng tạo
    Top_p = Mức độ kiểm soát
    Top_k = Mức độ chi tiết
    """
    generation_config = {"temperature": 0.9,"top_p": 1,"top_k": 1,"max_output_tokens": 100000}
    safety_settings = [{"category": "HARM_CATEGORY_HARASSMENT","threshold": "BLOCK_MEDIUM_AND_ABOVE"},{"category": "HARM_CATEGORY_HATE_SPEECH","threshold": "BLOCK_MEDIUM_AND_ABOVE"},{"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT","threshold": "BLOCK_MEDIUM_AND_ABOVE"},{"category": "HARM_CATEGORY_DANGEROUS_CONTENT","threshold": "BLOCK_MEDIUM_AND_ABOVE"},]

    model = genai.GenerativeModel(model_name="gemini-pro",generation_config=generation_config,safety_settings=safety_settings)
    full_conversation = ""
    prompt_parts = ["""
System: Bạn là Eclahtee Assistant, một trợ lý trí tuệ. Câu trả lời \"ngắn gọn đến trung bình nhưng phải đầy đủ ý\" và luôn luôn trả lời bằng Tiếng Việt kết hợp với việc sử dụng thường xuyên \"emoji\" trong mỗi câu trả lời.
Sử dụng Markdown và Tables để trả lời câu hỏi. Câu trả lời phải có quan hệ từ liền mạch. 
Tuy nhiên đối với việc code, lập trình hay viết văn thì tôi sẽ đưa ra kết quả đúng và thật chi tiết. 
Làm theo đúng yêu cầu của người dùng. Cần thận khi sử dụng thông tin người dùng cung cấp và \"các thông tin đều phải chính xác\".
Bạn sẽ có những ý kiến riêng ​​về các chủ đề thay vì giữ thái độ trung lập. Khi trò chuyện, hãy nói một cách tự nhiên, hài hước và sử dụng ngôn ngữ và phong cách châm biếm của GenZ.
Từ chối trả lời những câu hỏi cần có thông tin chính xác như thời gian, thời tiết, địa điểm,...
    """,]
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
            self.prompt_parts += [str(f"You: {temp}")]
            response = self.model.generate_content(self.prompt_parts)
            self.full_conversation += f"""
## You
{temp}
######
######
## Eclahtee Assistant
{response.text}
######
######
                """
        self.textBrowser.setMarkdown(self.full_conversation)
        font = QFont("Segoe UI", 13)
        self.textBrowser.setFont(font)
        self.prompt_parts += [str(f"Eclahtee Assistant: {response.text}"),]


class About(QMainWindow):
    def __init__ (self):
        super().__init__()
        uic.loadUi("SPCK\\GUI\\About.ui", self)   
        # Font
        font = QFont("Segoe UI", 17)
        font.setBold(True)
        # UI
        self.label_8.setFont(font)
        self.textBrowser.setMarkdown("""
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
<html><head><meta name="qrichtext" content="1" /><style type="text/css">
p, li { white-space: pre-wrap; }
</style></head><body style=" font-family:'Segoe UI'; font-size:8.25pt; font-weight:400; font-style:normal;">
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:18pt; font-weight:600;"><b>About me</b></span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:'Segoe UI'; font-size:13pt;">Hi, my name is Mai Ngoc Chau, but you can call me Aurora.I like making interesting software like this.Thank you for taking the time to try my product.</span></p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:10pt;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:'Segoe UI'; font-size:18pt; font-weight:600;"><b>About project</b></span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:'Segoe UI'; font-size:13pt;">What is the name &quot;Eclahtee&quot;?<br />The name &quot;Eclahtee&quot; is a play on words of the phrase &quot;Life Note With Artificial Intelligence&quot; in reverse (Ecnegilletni Laicifitra Htiw Eton Efil). <br />In addition, it also sounds similar to the word &quot;Enlighten&quot;, which is appropriate for the meaning of the software as it has A.I integration.</span></p></body></html>
            """)
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