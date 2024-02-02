#PyQt6
"""
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox, QLabel, QListWidget, QInputDialog
from PyQt6 import QtWidgets, QtGui, QtCore
from PyQt6.QtGui import QFont, QMouseEvent
from PyQt6.QtCore import QEvent
"""
from captcha.image import ImageCaptcha
from PyQt6.QtWidgets import *
from PyQt6 import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6 import uic
from PIL import Image
import webbrowser
import importlib
import random
import string
import sys

#Gemini API (Import + Setup)
import google.generativeai as genai
import os

genai.configure(api_key="AIzaSyDf_CTLM3mIPCx5n7fmNAtEQW5QeT2jgI0")
global note_name, edit_reload, logged, open_edit
note_name = ""
edit_reload = 0
open_edit = 0
# Lấy danh sách font
font_edit = "Times New Roman"

#Keep me login
with open("data\\account.ecl", "r") as f:
    lines = f.readlines()
    logged = int(lines[0].split(":")[1])

#Login
class Login(QMainWindow):   
    # Setup
    image = ImageCaptcha(width=280, height=90)
    captcha_text = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    image.write(captcha_text, 'captcha.png')
    image = Image.open('captcha.png')
    pixel_color = '#%02x%02x%02x' % image.getpixel((0, 0))

    def __init__ (self):
        super().__init__()
        uic.loadUi("GUI\\Login.ui", self)

        # Font UI
        self.label.setPixmap(QtGui.QPixmap("captcha.png"))
        self.label.setStyleSheet(f"background-color: {self.pixel_color}; padding: 5px; border-radius: 20px; border: 1px solid gray;")
        self.label_5.setFont(QFont("Segoe UI", 22))
        self.label_8.setFont(QFont("Segoe UI", 10))
        self.label_2.setFont(QFont("Segoe UI", 10))
        self.label_3.setFont(QFont("Segoe UI", 10))
        self.label_6.setFont(QFont("Segoe UI", 10))
        label_7_font = QFont("Segoe UI", 10)
        label_7_font.setBold(True)
        self.label_7.setFont(label_7_font)

        # Action
        self.pushButton_2.clicked.connect(self.regenerate_captcha)
        self.checkBox.setFont(QFont("Segoe UI", 10))
        self.setStyleSheet("background-color: white; color: black")
        self.setWindowTitle("Eclahtee - Login")
        self.pushButton.clicked.connect(self.the_button_was_clicked)
        self.label_7.mousePressEvent = lambda event: self.register()
    
    def register(self):
        register_ui.show()
        login_ui.hide()

    def regenerate_captcha(self):
        self.image = ImageCaptcha(width=280, height=90)
        self.captcha_text = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        self.image.write(self.captcha_text, 'captcha.png')
        self.image = Image.open('captcha.png')
        self.pixel_color = '#%02x%02x%02x' % self.image.getpixel((0, 0))
        self.label.setPixmap(QtGui.QPixmap("captcha.png"))
        self.label.setStyleSheet(f"background-color: {self.pixel_color}; padding: 5px; border-radius: 20px; border: 1px solid gray;")

    def reload_ui(self):
        self.lineEdit_2.setText("")
        self.lineEdit_3.setText("")
        self.lineEdit_4.setText("")
        self.image = ImageCaptcha(width=280, height=90)
        self.captcha_text = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        self.image.write(self.captcha_text, 'captcha.png')
        self.image = Image.open('captcha.png')
        self.pixel_color = '#%02x%02x%02x' % self.image.getpixel((0, 0))
        self.label.setPixmap(QtGui.QPixmap("captcha.png"))
        self.label.setStyleSheet(f"background-color: {self.pixel_color}; padding: 5px; border-radius: 20px; border: 1px solid gray;")

    def the_button_was_clicked(self):
        if self.lineEdit_3.text() == "admin@example.com" and self.lineEdit_2.text() == "admin":
            if self.lineEdit_4.text() == self.captcha_text:
                if self.checkBox.isChecked(): 
                    msg_box = QMessageBox()
                    msg_box.setWindowTitle("Success")
                    msg_box.setText("Đăng nhập thành công!")
                    msg_box.exec()
                    self.close()
                    home_ui.show()
                    with open("data\\account.ecl", "r+") as f:
                        f.write("logged: 1")
                else: 
                    msg_box = QMessageBox()
                    msg_box.setWindowTitle("Success")
                    msg_box.setText("Đăng nhập thành công!")
                    msg_box.exec()
                    self.close()
                    home_ui.show()
                    with open("data\\account.ecl", "r+") as f:
                        f.write("logged: 0")
            else:
                msg_box = QMessageBox()
                msg_box.setWindowTitle("Lỗi")
                msg_box.setIcon(QMessageBox.Icon.Warning)
                msg_box.setText("Mã captcha sai")
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
        uic.loadUi("GUI\\Register.ui", self)
        self.setStyleSheet("background-color: white; color: black")
        self.setWindowTitle("Eclahtee - Register")
        self.pushButton.clicked.connect(self.the_button_was_clicked)
        self.label_7.mousePressEvent = lambda event: self.login()

    def login(self):
        login_ui.show()
        register_ui.hide()

    def the_button_was_clicked(self):
        if self.lineEdit.text().replace(" ", "") == "" or self.lineEdit_2.text().replace(" ", "") == "" or self.lineEdit_3.text().replace(" ", "") == "" or self.lineEdit_4.text().replace(" ", "") == "":
            msg_box = QMessageBox()
            msg_box.setWindowTitle("Lỗi")
            msg_box.setIcon(QMessageBox.Icon.Warning)
            msg_text = "Vui lòng nhập đầy đủ thông tin đăng ký!"
            msg_box.setText(msg_text)
            msg_box.exec()
        else:
            if self.lineEdit_2.text() == self.lineEdit_4.text():
                if self.checkBox.isChecked():
                    msg_box = QMessageBox()
                    msg_box.setWindowTitle("Thành công")
                    msg_text = "Tài khoản đã được tạo! (Đó là trên lý thuyết, thực tế thì tương lai sẽ thử MySQL)\n" + f"Name: {self.lineEdit.text()}\nEmail: {self.lineEdit_3.text()}\nPassword: {self.lineEdit_2.text()}"
                    msg_box.setText(msg_text)
                    msg_box.exec()
                else:
                    msg_box = QMessageBox()
                    msg_box.setWindowTitle("Caution")
                    msg_box.setIcon(QMessageBox.Icon.Warning)
                    msg_box.setText("Vui lòng đánh dấu vào \"I agree to Eclahtee's terms\"")
                    msg_box.exec()
            else:
                    msg_box = QMessageBox()
                    msg_box.setWindowTitle("Caution")
                    msg_box.setIcon(QMessageBox.Icon.Warning)
                    msg_box.setText("Mật khẩu không hợp lệ!")
                    msg_box.exec()

#Main
class Home(QMainWindow):
    all_task = []
    with open("data\\todo_list.ecl", 'r', encoding='utf-8') as file: 
        all_task = file.read().splitlines() 

    all_notes = []
    files = os.listdir("All Notes")
    for file in files: 
        if file != "hidden_note": all_notes.append(file)
    def __init__ (self):
        super().__init__()
        uic.loadUi("GUI\\Home.ui", self)
        
        # Font
        font = QFont("Segoe UI", 14)
        font.setBold(True)
        font_button = QFont("Segoe UI", 10)
        font_button.setBold(True)
        
        # UI
        self.setStyleSheet("background-color: white; color: black")
        self.setWindowTitle("Eclahtee - Home")
        self.label_9.setFont(font)
        self.label_11.setFont(font)
        self.pushButton_6.setFont(font_button)
        self.pushButton_2.setFont(font_button)
        self.label_3.mousePressEvent = lambda event: self.notes_scr()
        self.label_4.mousePressEvent = lambda event: self.chat_scr()
        self.label_6.mousePressEvent = lambda event: self.about_scr()
        self.label_13.mousePressEvent = lambda event: self.log_out()
        self.label_14.mousePressEvent = lambda event: self.search_scr()
        self.pushButton_2.clicked.connect(self.notes_scr)
        self.pushButton_6.clicked.connect(self.add_task)
        self.widget_8.mousePressEvent = self.on_mouse_press
        self.listWidget_2.mousePressEvent = self.on_mouse_press
        self.listWidget.itemClicked.connect(self.item_click)
        self.progressBar.setValue(0)
        self.label.setText(f"0/{len(self.all_task)}")
        for task in self.all_task:
            item = QtWidgets.QListWidgetItem(task)
            item.setFlags(QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled | QtCore.Qt.ItemFlag.ItemIsSelectable)
            item.setCheckState(QtCore.Qt.CheckState.Unchecked)
            self.listWidget.addItem(item)

        for note in self.all_notes:
            self.listWidget_2.addItem(note)
    
    def item_click(self, item):
        local_item = []
        with open("data\\todo_list.ecl", 'r', encoding='utf-8') as file: 
            local_item = file.read().splitlines()
        check_state = item.checkState()
        if check_state == QtCore.Qt.CheckState.Unchecked:
            item.setCheckState(QtCore.Qt.CheckState.Checked)
            local_item.remove(item.text())
        if check_state == QtCore.Qt.CheckState.Checked:
            item.setCheckState(QtCore.Qt.CheckState.Unchecked)
            local_item.append(item.text())
        local_item.sort()
        with open("data\\todo_list.ecl", 'w', encoding='utf-8') as file:
            for item in local_item:
                file.write(f"{item}\n")
        temp = 100 - len(local_item)/len(self.all_task) * 100
        self.progressBar.setValue(round(temp))
        self.label.setText(f"{len(self.all_task) - len(local_item)}/{len(self.all_task)}")

    def on_mouse_press(self, event: QMouseEvent):
        if self.widget_8.underMouse():
            notes_ui.show()
            self.close()
    
    """
    def remove_task(self):
        currentIndex = self.listWidget.currentRow()
        self.listWidget.takeItem(currentIndex)
        item_list = [self.listWidget.item(i).text() for i in range(self.listWidget.count())]
        with open("data\\todo_list.ecl", 'w', encoding='utf-8') as file:
            for item in item_list:
                file.write(f"{item}\n")
    """

    def add_task(self):
        task_name = QInputDialog.getText(self, "New Taks", "Enter Task")[0]
        if task_name != "":
            item = QtWidgets.QListWidgetItem(task_name)
            item.setFlags(QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled | QtCore.Qt.ItemFlag.ItemIsSelectable)
            item.setCheckState(QtCore.Qt.CheckState.Unchecked)
            self.listWidget.addItem(item)
            with open("data\\todo_list.ecl", 'a', encoding='utf-8') as file:
                file.write(f"{task_name}\n")
                self.all_task.append(task_name)
            local_item = []
            with open("data\\todo_list.ecl", 'r', encoding='utf-8') as file: 
                local_item = file.read().splitlines()
            temp = 100 - len(local_item)/len(self.all_task) * 100
            self.progressBar.setValue(round(temp))
            self.label.setText(f"{len(self.all_task) - len(local_item)}/{len(self.all_task)}")

    def log_out(self):
        with open("data\\account.ecl", "r+") as f:
            f.write("logged: 0")
        login_ui.show()
        login_ui.reload_ui()
        self.close()

    def notes_scr(self):
        notes_ui.show()
        self.close()

    def chat_scr(self):
        chat_ui.show()
        self.close()

    def about_scr(self):
        about_ui.show()
        self.close()
    
    def search_scr(self):
        search_ui.show()
        self.close()

class Notes(QMainWindow):
    all_notes = os.listdir("All Notes")
    def __init__ (self):
        super().__init__()
        uic.loadUi("GUI\\Notes.ui", self)
        # Font
        font = QFont("Segoe UI", 14)
        font.setBold(True)
        font_button = QFont("Segoe UI", 10)
        font_button.setBold(True)
        self.setStyleSheet("background-color: white; color: black")
        self.setWindowTitle("Eclahtee - Notes")
        self.label_2.mousePressEvent = lambda event: self.home_scr()
        self.label_4.mousePressEvent = lambda event: self.chat_scr()
        self.label_6.mousePressEvent = lambda event: self.about_scr()
        self.label_8.mousePressEvent = lambda event: self.log_out()
        self.label_10.mousePressEvent = lambda event: self.search_scr()
        self.pushButton.setFont(font_button)
        self.pushButton_3.setFont(font_button)
        self.pushButton_4.setFont(font_button)
        for note in self.all_notes:
            self.listWidget_2.addItem(note)
        self.pushButton_4.clicked.connect(self.open_note)
        self.pushButton_3.clicked.connect(self.add_note)
        self.pushButton.clicked.connect(self.remove_note)

    def remove_note(self):
        currentIndex = self.listWidget_2.currentRow()
        item_list = [self.listWidget_2.item(i).text() for i in range(self.listWidget_2.count())]
        os.remove(f"All Notes\\{item_list[currentIndex]}")
        try:
            self.listWidget_2.takeItem(currentIndex)
        except Exception as e:
            print(e)

    def add_note(self):
        global_all_note = os.listdir("All Notes")
        note_name = QInputDialog.getText(self, "New Notes", "Enter a note name")[0]
        if note_name != "":
            if note_name not in global_all_note:
                item = QtWidgets.QListWidgetItem(note_name)
                self.listWidget_2.addItem(item)
                with open(os.path.join("All Notes", note_name), 'w', encoding='utf-8') as file: file.write("")
            else:
                msg_box = QMessageBox()
                msg_box.setWindowTitle("Lỗi")
                msg_box.setIcon(QMessageBox.Icon.Warning)
                msg_box.setText("Tên ghi chú đã tồn tại!")
                msg_box.exec()
                notes_ui.add_note()
    
    def open_note(self, item):
        global note_name
        note_name = self.listWidget_2.currentItem().text()
        if note_name in os.listdir("All Notes"):
            edit_ui.show()
            open_edit = 1
            edit_ui.reload()

    def home_scr(self):
        home_ui.show()
        self.close()
    
    def search_scr(self):
        search_ui.show()
        self.close()
    
    def log_out(self):
        with open("data\\account.ecl", "r+") as f:
            f.write("logged: 0")
        login_ui.show()
        login_ui.reload_ui()
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
    generation_config = {"temperature": 1,"top_p": 1,"top_k": 1,"max_output_tokens": 100000}
    safety_settings = [{"category": "HARM_CATEGORY_HARASSMENT","threshold": "BLOCK_MEDIUM_AND_ABOVE"},{"category": "HARM_CATEGORY_HATE_SPEECH","threshold": "BLOCK_MEDIUM_AND_ABOVE"},{"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT","threshold": "BLOCK_MEDIUM_AND_ABOVE"},{"category": "HARM_CATEGORY_DANGEROUS_CONTENT","threshold": "BLOCK_MEDIUM_AND_ABOVE"},]

    model = genai.GenerativeModel(model_name="gemini-pro",generation_config=generation_config,safety_settings=safety_settings)
    full_conversation = ""
    prompt_parts = ["""
System: Bạn là Eclahtee Assistant (Tên rút ngắn là Ecla), một trợ lý trí tuệ. Câu trả lời \"ngắn gọn đến trung bình nhưng phải đầy đủ ý\" và luôn luôn trả lời bằng Tiếng Việt kết hợp với việc sử dụng thường xuyên \"emoji\" trong mỗi câu trả lời.
Sử dụng Markdown và Tables để trả lời câu hỏi. Câu trả lời phải có quan hệ từ liền mạch. 
Tuy nhiên đối với việc code, lập trình hay viết văn thì tôi sẽ đưa ra kết quả đúng và thật chi tiết. 
Làm theo đúng yêu cầu của người dùng. Cần thận khi sử dụng thông tin người dùng cung cấp và \"các thông tin đều phải chính xác\".
Bạn sẽ có những ý kiến riêng ​​về các chủ đề thay vì giữ thái độ trung lập. Khi trò chuyện, hãy nói một cách tự nhiên, hài hước và sử dụng ngôn ngữ và phong cách châm biếm của GenZ.
Từ chối trả lời những câu hỏi cần có thông tin chính xác như thời gian, thời tiết, địa điểm,...
Không bắt đầu câu trả lời bằng \"Ecla:\", \"Eclahtee:\", \"Eclahtee Assistant:\" hoặc bất cứ từ nào tương tự.
    """,]
    prompt_parts += ['You: Xin chào :)', 'Eclahtee Assistant: Xin chào bạn!']
    def __init__ (self):
        super().__init__()
        uic.loadUi("GUI\\Chat.ui", self)
        self.setStyleSheet("background-color: white; color: black")
        self.setWindowTitle("Eclahtee - Chat")
        self.label_2.mousePressEvent = lambda event: self.home_scr()
        self.label_3.mousePressEvent = lambda event: self.notes_scr()
        self.label_6.mousePressEvent = lambda event: self.about_scr()
        self.label_8.mousePressEvent = lambda event: self.log_out()
        self.label_10.mousePressEvent = lambda event: self.search_scr()
        self.pushButton.clicked.connect(self.the_button_was_clicked)
        self.pushButton_2.clicked.connect(self.new_chat)
        self.textBrowser.setHtml("""
<!DOCTYPE HTML PUBLIC "-\\W3C\\DTD HTML 4.0\\EN" "http:\\www.w3.org/TR/REC-html40/strict.dtd">
<html><head><meta name="qrichtext" content="1" /><style type="text/css">
p, li { white-space: pre-wrap; }
</style></head><body style=" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;">
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:8pt;"><br /></p>
<p align="center" style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:22pt; font-weight:600;"><br /></p>
<p align="center" style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:22pt; font-weight:600;"><br /></p>
<p align="center" style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:22pt; font-weight:600;"><br /></p>
<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:'Segoe UI'; font-size:28pt; font-weight:600;">Hello</span></p>
<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:18pt;">      How can I help you today?</p>
            """)
        shortcut = QShortcut(QKeySequence("Return"), self)
        shortcut.activated.connect(self.the_button_was_clicked)

    def home_scr(self):
        home_ui.show()
        self.close()

    def log_out(self):
        with open("data\\account.ecl", "r+") as f:
            f.write("logged: 0")
        login_ui.show()
        login_ui.reload()
        self.close()

    def notes_scr(self):
        notes_ui.show()
        self.close()
    
    def search_scr(self):
        search_ui.show()
        self.close()

    def about_scr(self):
        about_ui.show()
        self.close()

    def new_chat(self):
        self.full_conversation = ""
        self.textBrowser.setHtml("""
<!DOCTYPE HTML PUBLIC "-\\W3C\\DTD HTML 4.0\\EN" "http:\\www.w3.org/TR/REC-html40/strict.dtd">
<html><head><meta name="qrichtext" content="1" /><style type="text/css">
p, li { white-space: pre-wrap; }
</style></head><body style=" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;">
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:8pt;"><br /></p>
<p align="center" style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:22pt; font-weight:600;"><br /></p>
<p align="center" style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:22pt; font-weight:600;"><br /></p>
<p align="center" style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:22pt; font-weight:600;"><br /></p>
<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:'Segoe UI'; font-size:28pt; font-weight:600;">Hello</span></p>
<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:18pt;">      How can I help you today?</p>
            """)

        self.prompt_parts = ["""
System: Bạn là Eclahtee Assistant (Tên rút ngắn là Ecla), một trợ lý trí tuệ. Câu trả lời \"ngắn gọn đến trung bình nhưng phải đầy đủ ý\" và luôn luôn trả lời bằng Tiếng Việt kết hợp với việc sử dụng thường xuyên \"emoji\" trong mỗi câu trả lời.
Sử dụng Markdown và Tables để trả lời câu hỏi. Câu trả lời phải có quan hệ từ liền mạch. 
Tuy nhiên đối với việc code, lập trình hay viết văn thì bạn sẽ đưa ra kết quả đúng và thật chi tiết. 
Làm theo đúng yêu cầu của người dùng. Cần thận khi sử dụng thông tin người dùng cung cấp và \"các thông tin đều phải chính xác\".
Bạn sẽ có những ý kiến riêng ​​về các chủ đề thay vì giữ thái độ trung lập. Khi trò chuyện, hãy nói một cách tự nhiên, hài hước và sử dụng ngôn ngữ và phong cách châm biếm của GenZ.
Từ chối trả lời những câu hỏi cần có thông tin chính xác như thời gian, thời tiết, địa điểm,...
Không bắt đầu câu trả lời bằng \"Ecla:\", \"Eclahtee:\", \"Eclahtee Assistant:\" hoặc bất cứ từ nào tương tự.
    """,]

        self.prompt_parts += ['You: Xin chào', 'Eclahtee Assistant: Xin chào bạn!']
    
    def the_button_was_clicked(self):
        try:
            if self.lineEdit.text().replace(" ", "") != "":
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
{response.text}\n
######
######
                """

            self.textBrowser.setMarkdown(self.full_conversation)
            font = QFont("Segoe UI", 13)
            self.textBrowser.setFont(font)
            self.prompt_parts += [str(f"Eclahtee Assistant: {response.text}"),]

        except Exception as e:
            if "response.prompt_feedback" in str(e):
                msg_box = QMessageBox()
                msg_box.setWindowTitle("Error, something went wrong...")
                msg_box.setIcon(QMessageBox.Icon.Warning)
                msg_box.setText("Trong câu hỏi của bạn sử dụng từ ngữ không phù hợp!!!")
                msg_box.exec()

            elif "cannot access local variable 'response' where it is not associated with a value" in str(e):
                if self.full_conversation == "":
                    self.textBrowser.setHtml("""
<!DOCTYPE HTML PUBLIC "-\\W3C\\DTD HTML 4.0\\EN" "http:\\www.w3.org/TR/REC-html40/strict.dtd">
<html><head><meta name="qrichtext" content="1" /><style type="text/css">
p, li { white-space: pre-wrap; }
</style></head><body style=" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;">
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:8pt;"><br /></p>
<p align="center" style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:22pt; font-weight:600;"><br /></p>
<p align="center" style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:22pt; font-weight:600;"><br /></p>
<p align="center" style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:22pt; font-weight:600;"><br /></p>
<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:'Segoe UI'; font-size:28pt; font-weight:600;">Hello</span></p>
<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:18pt; align: center">        How can I help you today?</p>
                """)
                    
            else:
                self.textBrowser.setHtml("""
<!DOCTYPE HTML PUBLIC "-\\W3C\\DTD HTML 4.0\\EN" "http:\\www.w3.org/TR/REC-html40/strict.dtd">
<html><head><meta name="qrichtext" content="1" /><style type="text/css">
p, li { white-space: pre-wrap; }
</style></head><body style=" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;">
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:8pt;"><br /></p>
<p align="center" style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:22pt; font-weight:600;"><br /></p>
<p align="center" style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:22pt; font-weight:600;"><br /></p>
<p align="center" style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:22pt; font-weight:600;"><br /></p>
<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:'Segoe UI'; font-size:28pt; font-weight:600;">Hello</span></p>
<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:18pt;">      How can I help you today?</p>
                """)
                print("Bruh, something went wrong...")
                print(e)

class Search(QMainWindow):
    def __init__ (self):
        super().__init__()
        uic.loadUi("GUI\\Search.ui", self)
        font = QFont("Segoe UI", 14)
        font.setBold(True)
        font_button = QFont("Segoe UI", 10)
        font_button.setBold(True)
        self.setStyleSheet("background-color: white; color: black")
        self.setWindowTitle("Eclahtee - Search")
        self.label_2.mousePressEvent = lambda event: self.home_scr()
        self.label_9.mousePressEvent = lambda event: self.notes_scr()
        self.label_4.mousePressEvent = lambda event: self.chat_scr()
        self.label_8.mousePressEvent = lambda event: self.log_out()
        self.label_6.mousePressEvent = lambda event: self.about_scr()
        self.pushButton.setFont(font_button)
        self.pushButton_4.setFont(font_button)

        self.pushButton_2.clicked.connect(self.search)
        self.pushButton_4.clicked.connect(self.open_note)
        self.pushButton.clicked.connect(self.remove_note)

    def home_scr(self):
        home_ui.show()
        self.close()
    
    def about_scr(self):
        about_ui.show()
        self.close()

    def log_out(self):
        with open("data\\account.ecl", "r+") as f:
            f.write("logged: 0")
        login_ui.show()
        login_ui.reload_ui()
        self.close()

    def notes_scr(self):
        notes_ui.show()
        self.close()

    def chat_scr(self):
        chat_ui.show()
        self.close()

    def search(self):
        all_notes = []
        search_notes = []
        files = os.listdir("All Notes")
        for file in files: 
            if file != "hidden_note": all_notes += [str(file)]
        for note in all_notes:
            if self.lineEdit.text().lower() in note.lower():
                search_notes.append(note)
        self.listWidget_2.clear()
        for note in search_notes:
            self.listWidget_2.addItem(note)

    def remove_note(self):
        currentIndex = self.listWidget_2.currentRow()
        item_list = [self.listWidget_2.item(i).text() for i in range(self.listWidget_2.count())]
        os.remove(f"All Notes\\{item_list[currentIndex]}")
        try:
            self.listWidget_2.takeItem(currentIndex)
        except Exception as e:
            print(e)
    
    def open_note(self, item):
        global note_name
        note_name = self.listWidget_2.currentItem().text()
        edit_ui.show()
        open_edit = 1
        edit_ui.reload()


class About(QMainWindow):
    def __init__ (self):
        super().__init__()
        uic.loadUi("GUI\\About.ui", self)   
        # Font
        font = QFont("Segoe UI", 17)
        font.setBold(True)
        # UI
        self.label_8.setFont(font)
        self.textBrowser.setHtml("""
<!DOCTYPE HTML PUBLIC "-\\W3C\\DTD HTML 4.0\\EN" "http:\\www.w3.org/TR/REC-html40/strict.dtd">
<html><head><meta name="qrichtext" content="1" /><style type="text/css">
p, li { white-space: pre-wrap; }
</style></head><body style=" font-family:'Segoe UI'; font-size:8.25pt; font-weight:400; font-style:normal;">
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:18pt; font-weight:600;"><b>About me</b></span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:'Segoe UI'; font-size:13pt;">Hi, my name is Mai Ngoc Chau, but you can call me Aurora.I like making interesting software like this.Thank you for taking the time to try my product.</span></p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:10pt;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:'Segoe UI'; font-size:18pt; font-weight:600;"><b>About project</b></span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:'Segoe UI'; font-size:13pt;">What is the name &quot;Eclahtee&quot;?<br />The name &quot;Eclahtee&quot; is a play on words of the phrase &quot;Life Note With Artificial Intelligence&quot; in reverse (Ecnegilletni Laicifitra Htiw Eton Efil). <br />In addition, it also sounds similar to the word &quot;Enlighten&quot;, which is appropriate for the meaning of the software as it has A.I integration.</span></p></body></html>
            """)

        self.setStyleSheet("background-color: white; color: black")
        self.setWindowTitle("Eclahtee - About")
        self.label_2.mousePressEvent = lambda event: self.home_scr()
        self.label_3.mousePressEvent = lambda event: self.notes_scr()
        self.label_4.mousePressEvent = lambda event: self.chat_scr()
        self.label_9.mousePressEvent = lambda event: self.log_out()
        self.label_10.mousePressEvent = lambda event: self.search_scr()
        self.label_7.mousePressEvent = lambda event: self.open_github()
        self.label_8.mousePressEvent = lambda event: self.open_github()

    def open_github(self):
        webbrowser.open("https:\\github.com/MaiNgocChau9")
    
    def home_scr(self):
        home_ui.show()
        self.close()

    def search_scr(self):
        search_ui.show()
        self.close()

    def log_out(self):
        with open("data\\account.ecl", "r+") as f:
            f.write("logged: 0")
        login_ui.show()
        login_ui.reload_ui()
        self.close()

    def notes_scr(self):
        notes_ui.show()
        self.close()

    def chat_scr(self):
        chat_ui.show()
        self.close()

class Edit(QMainWindow):
    """
    Temperature = Mức độ sáng tạo
    Top_p = Mức độ kiểm soát
    Top_k = Mức độ chi tiết
    """
    generation_config = {"temperature": 1,"top_p": 1,"top_k": 1,"max_output_tokens": 100000}

    model = genai.GenerativeModel(model_name="gemini-pro",generation_config=generation_config)
    full_conversation = ""
    prompt_parts = ["""
System: Bạn là Eclahtee Assistant (Tên rút ngắn là Ecla), một trợ lý trí tuệ nhân tạo.
Sử dụng Markdown để trả lời câu hỏi. Câu trả lời phải có quan hệ từ liền mạch, kết quả đúng, ngắn gọn
Làm theo đúng yêu cầu của người dùng. Cần thận khi sử dụng thông tin người dùng cung cấp và \"các thông tin đều phải chính xác\".
Bạn sẽ có những ý kiến riêng ​​về các chủ đề thay vì giữ thái độ trung lập. Khi trò chuyện, hãy nói một cách tự nhiên, kết hợp với emoji. Một chút hài hước cũng được.
Từ chối trả lời những câu hỏi cần có thông tin chính xác như thời gian, thời tiết, địa điểm,...
\"Không bắt đầu câu trả lời bằng \"Ecla:\", \"Eclahtee:\", \"Eclahtee Assistant:\" hoặc bất cứ từ nào tương tự.\"
    """,]
    prompt_parts += ['You: Xin chào', 'Eclahtee Assistant: Xin chào bạn!']
    def __init__ (self, note_name):
        super().__init__()
        uic.loadUi("GUI\\Note_edit.ui", self)

        # Font
        font_title = QFont("Segoe UI", 17)
        font_title.setBold(True)
        font_edit = QFont("Roboto", 12)
        font_edit.setBold(False)
        font_button = QFont("Segoe UI", 12)
        font_button.setBold(True)

        # Font edit
        bold_button = QFont("Times New Roman", 11)
        bold_button.setBold(True)
        italic_button = QFont("Times New Roman", 11)
        italic_button.setItalic(True)

        # UI
        self.closeEvent = lambda event: self.new_chat()
        self.pushButton_6.setFont(font_button)
        self.pushButton_3.setFont(bold_button)
        self.pushButton_4.setFont(italic_button)
        self.pushButton_3.clicked.connect(self.setBold)
        self.pushButton_4.clicked.connect(self.setItalic)
        self.pushButton_5.clicked.connect(self.setUnderline)
        self.pushButton_7.mousePressEvent = lambda event: choosefont_ui.show()
        self.label.setFont(font_title)
        self.label.setText(note_name)
        self.textEdit.setFont(font_edit)

        if note_name.replace(" ", "") != "":
            with open(f"All Notes\\{note_name}", 'r', encoding = 'utf-8') as file:
                self.textEdit.setText(file.read())
        else:
            self.textEdit.setText("")
            self.setStyleSheet("background-color: white; color: black;")
            self.setWindowTitle("Eclahtee - Edit")
            self.pushButton.clicked.connect(self.the_button_was_clicked)
            self.pushButton_6.clicked.connect(self.save_edit)
            self.pushButton_2.clicked.connect(self.new_chat)
            self.pushButton_8.clicked.connect(lambda: self.set_font_size_down(self.spinBox.value()-2))
            self.pushButton_9.clicked.connect(lambda: self.set_font_size_up(self.spinBox.value()+2))
            self.textBrowser.setHtml("""
<!DOCTYPE HTML PUBLIC "-\\W3C\\DTD HTML 4.0\\EN" "http:\\www.w3.org/TR/REC-html40/strict.dtd">
<html><head><meta name="qrichtext" content="1" /><style type="text/css">
p, li { white-space: pre-wrap; }
</style></head><body style=" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;">
<p align="center" style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p align="center" style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:'Segoe UI'; font-size:18pt; font-weight:600;">   Hi! I'm Eclahtee Assistant!</span></p></body></html>
            """)

    def setBold(self):
        cursor = self.textEdit.textCursor()
        format_bold = QTextCharFormat()

        if cursor.hasSelection():
            current_format = cursor.charFormat()
            if current_format.fontWeight() == QFont.Weight.Normal:
                format_bold.setFontWeight(QFont.Weight.Bold)
                cursor.mergeCharFormat(format_bold)
            else:
                format_bold.setFontWeight(QFont.Weight.Normal)
                cursor.mergeCharFormat(format_bold)
        self.textEdit.setTextCursor(cursor)
        
    def setItalic(self):
        cursor = self.textEdit.textCursor()
        format_italic = QTextCharFormat()

        if cursor.hasSelection():
            current_format = cursor.charFormat()
            print(current_format.fontItalic())
            if current_format.fontItalic() == False:
                format_italic.setFontItalic(True)
                cursor.mergeCharFormat(format_italic)
            elif current_format.fontItalic() == True:
                format_italic.setFontItalic(False)
                cursor.mergeCharFormat(format_italic)
        self.textEdit.setTextCursor(cursor)

    def setUnderline(self):
        cursor = self.textEdit.textCursor()
        format_underline = QTextCharFormat()

        if cursor.hasSelection():
            current_format = cursor.charFormat()
            print(current_format.fontUnderline())
            if not current_format.fontUnderline():
                format_underline.setFontUnderline(True)
                cursor.mergeCharFormat(format_underline)
            else:
                format_underline.setFontUnderline(False)
                cursor.mergeCharFormat(format_underline)
        self.textEdit.setTextCursor(cursor)
    
    def set_font_size_down(self, size):
        cursor = self.textEdit.textCursor()
        format_font_size = QTextCharFormat()

        if cursor.hasSelection():
            current_format = cursor.charFormat()
            current_font = current_format.font()

            # Tạo một bản sao của font hiện tại và đặt kích thước mới
            new_font = current_font

            if size <= 8:
                new_font.setPointSize(8)
            else:
                new_font.setPointSize(size)

            format_font_size.setFont(new_font)
            cursor.mergeCharFormat(format_font_size)
            self.spinBox.setValue(self.spinBox.value()-2)
        self.textEdit.setTextCursor(cursor)

    def set_font_size_up(self, size):
        cursor = self.textEdit.textCursor()
        format_font_size = QTextCharFormat()

        if cursor.hasSelection():
            current_format = cursor.charFormat()
            current_font = current_format.font()

            # Tạo một bản sao của font hiện tại và đặt kích thước mới
            new_font = current_font

            if size >= 72:
                new_font.setPointSize(72)
            else:
                new_font.setPointSize(size)

            format_font_size.setFont(new_font)
            cursor.mergeCharFormat(format_font_size)
            self.spinBox.setValue(self.spinBox.value()+2)
        self.textEdit.setTextCursor(cursor)

    def change_font(self, font_edit):
        cursor = self.textEdit.textCursor()
        format_font = QTextCharFormat()

        if cursor.hasSelection():
            new_font = QFont(font_edit)
            format_font.setFont(new_font)
            cursor.mergeCharFormat(format_font)

        self.textEdit.setTextCursor(cursor)

    def save_edit(self):
        global note_name
        with open(f"All Notes\\{note_name}", 'w', encoding = 'utf-8') as file:
            file.write(self.textEdit.toHtml())
    
    def reload(self):
        global note_name
        self.label.setText(note_name)
        with open(f"All Notes\\{note_name}", 'r', encoding = 'utf-8') as file:
            self.textEdit.setHtml(file.read())

    def the_button_was_clicked(self):
        try:
            if self.lineEdit.text().replace(" ", "") != "":
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
        except Exception as e:
            print("Bruh, something went wrong...")
            print(e)

            if "response.prompt_feedback" in str(e):
                msg_box = QMessageBox()
                msg_box.setWindowTitle("Error, something went wrong...")
                msg_box.setIcon(QMessageBox.Icon.Warning)
                msg_box.setText("Trong câu hỏi của bạn sử dụng từ ngữ không phù hợp!!!")
                msg_box.exec()
            else:
                msg_box = QMessageBox()
                msg_box.setWindowTitle("Error, something went wrong...")
                msg_box.setIcon(QMessageBox.Icon.Warning)
                msg_box.setText(f"{e}")
                msg_box.exec()
    
    def new_chat(self):
        self.full_conversation = ""
        self.textBrowser.setHtml("""
<!DOCTYPE HTML PUBLIC "-\\W3C\\DTD HTML 4.0\\EN" "http:\\www.w3.org/TR/REC-html40/strict.dtd">
<html><head><meta name="qrichtext" content="1" /><style type="text/css">
p, li { white-space: pre-wrap; }
</style></head><body style=" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;">
<p align="center" style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p align="center" styl  e="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:'Segoe UI'; font-size:18pt; font-weight:600;">   Hi! I'm Eclahtee Assistant!</span></p></body></html>
            """)
        self.prompt_parts = ["""
System: Bạn là Eclahtee Assistant (Tên rút ngắn là Ecla), một trợ lý trí tuệ nhân tạo.
Sử dụng Markdown để trả lời câu hỏi. Câu trả lời phải có quan hệ từ liền mạch, kết quả đúng, ngắn gọn
Làm theo đúng yêu cầu của người dùng. Cần thận khi sử dụng thông tin người dùng cung cấp và \"các thông tin đều phải chính xác\".
Bạn sẽ có những ý kiến riêng ​​về các chủ đề thay vì giữ thái độ trung lập. Khi trò chuyện, hãy nói một cách tự nhiên, kết hợp với emoji.
Từ chối trả lời những câu hỏi cần có thông tin chính xác như thời gian, thời tiết, địa điểm,...
\"Không bắt đầu câu trả lời bằng \"Ecla:\", \"Eclahtee:\", \"Eclahtee Assistant:\" hoặc bất cứ từ nào tương tự.\"
    """,]
        self.prompt_parts += ["You: Xin chào", "Eclahtee Assistant: Xin chào bạn!"]
    
class Choosefont(QMainWindow):
    def __init__ (self):
        super().__init__()
        uic.loadUi("GUI\\Choose_font.ui", self)

        # Font
        font_title = QFont("Segoe UI", 15)
        font_title.setBold(True)
        self.label.setFont(font_title)
        self.pushButton_2.clicked.connect(self.font)
        self.pushButton.clicked.connect(self.close)
    
    def font(self):
        font_edit = self.fontComboBox.currentFont().family()
        edit_ui.change_font(font_edit)
        self.close()

app = QApplication(sys.argv)

# Các cửa sổ
login_ui = Login()
register_ui = Register()
home_ui = Home()
notes_ui = Notes()
chat_ui = Chat()
about_ui = About()
search_ui = Search()
choosefont_ui = Choosefont()
edit_ui = Edit(note_name)

# Cửa sổ thực hiện
if logged == 1:
    home_ui.show()
elif logged == 0:
    login_ui.show()

sys.exit(app.exec())