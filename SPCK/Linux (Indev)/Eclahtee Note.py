# PyQt6
from PyQt6.QtWidgets import *
from PyQt6 import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6 import uic
import sys

# Captcha
from captcha.image import ImageCaptcha
from PIL import Image
import random
import string

# Some thing very cool =)
import webbrowser

# Gemini API Setup
import google.generativeai as genai
import html2text
import re
import os
genai.configure(api_key="AIzaSyDf_CTLM3mIPCx5n7fmNAtEQW5QeT2jgI0")

# Get current time
from datetime import datetime
hello = ""
now = datetime.now()
time = int(now.strftime("%H"))

if time <= 13 and time >= 6:
    hello = "Good morning"

elif time <= 18 and time >= 13:
    hello = "Good afternoon"

else:
    hello = "Good evening"


# === Setup global variables ===
global note_name, edit_reload, logged, last_ui
note_name = ""
edit_reload = 0
last_ui = ""

# Get account
with open("data//account.ecl", "r", encoding='utf-8') as f: # Check account
    lines = f.readlines()
    logged = int(lines[0].split(": ")[1])
    account = str(lines[1].split(": ")[1]).replace("\n", "")
    email = str(lines[2].split(": ")[1]).replace("\n", "")
    password = str(lines[3].split(": ")[1]).replace("\n", "")
    last_account_name = str(lines[4].split(": ")[1]).replace("\n", "")

# Default font
font_edit = "Times New Roman"

# Login
class Login(QMainWindow):   
    # Setup
    image = ImageCaptcha(width=280, height=90)
    captcha_text = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    image.write(captcha_text, 'Image//captcha.png')
    image = Image.open('Image//captcha.png')
    pixel_color = '#%02x%02x%02x' % image.getpixel((0, 0))

    def __init__ (self):
        super().__init__()
        uic.loadUi("GUI//Login.ui", self)
        self.setWindowIcon(QtGui.QIcon('Image//icon.ico'))

        # Font UI
        self.label.setPixmap(QtGui.QPixmap("Image//captcha.png"))
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
        self.image.write(self.captcha_text, 'Image//captcha.png')
        self.image = Image.open('Image//captcha.png')
        self.pixel_color = '#%02x%02x%02x' % self.image.getpixel((0, 0))
        self.label.setPixmap(QtGui.QPixmap("Image//captcha.png"))
        self.label.setStyleSheet(f"background-color: {self.pixel_color}; padding: 5px; border-radius: 20px; border: 1px solid gray;")

    def reload_ui(self):
        self.lineEdit_2.setText("")
        self.lineEdit_3.setText("")
        self.lineEdit_4.setText("")
        self.image = ImageCaptcha(width=280, height=90)
        self.captcha_text = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        self.image.write(self.captcha_text, 'Image//captcha.png')
        self.image = Image.open('Image//captcha.png')
        self.pixel_color = '#%02x%02x%02x' % self.image.getpixel((0, 0))
        self.label.setPixmap(QtGui.QPixmap("Image//captcha.png"))
        self.label.setStyleSheet(f"background-color: {self.pixel_color}; padding: 5px; border-radius: 20px; border: 1px solid gray;")

    def the_button_was_clicked(self):
        print("Email:", email)
        print("Password:", password)
        if self.lineEdit_3.text() == "admin@example.com" and self.lineEdit_2.text() == "admin":
            if self.lineEdit_4.text() == self.captcha_text:
                if self.checkBox.isChecked(): 
                    msg_box = QMessageBox()
                    msg_box.setWindowTitle("Success")
                    msg_box.setText("Đăng nhập thành công!")
                    msg_box.exec()
                    self.close()
                    home_ui.show()
                    home_ui.label_17.setText(f"{hello}, Admin")
                    last_account_name = "Admin"
                    with open("data//account.ecl", "w", encoding='utf-8') as f:
                        f.write(f"logged: 1\naccount: {account}\nemail: {email}\npassword: {password}\nlast_account_name: Admin")
                else: 
                    msg_box = QMessageBox()
                    msg_box.setWindowTitle("Success")
                    msg_box.setText("Đăng nhập thành công!")
                    msg_box.exec()
                    self.close()
                    home_ui.show()
                    home_ui.label_17.setText(f"{hello}, Admin")
                    last_account_name = "Admin"
                    with open("data//account.ecl", "w", encoding='utf-8') as f:
                        f.write(f"logged: 0\naccount: {account}\nemail: {email}\npassword: {password}\nlast_account_name: Admin")
                    
        elif self.lineEdit_3.text() == email and self.lineEdit_2.text() == password:
            if self.lineEdit_4.text() == self.captcha_text:
                if self.checkBox.isChecked(): 
                    msg_box = QMessageBox()
                    msg_box.setWindowTitle("Success")
                    msg_box.setText("Đăng nhập thành công!")
                    msg_box.exec()
                    self.close()
                    home_ui.show()
                    home_ui.label_17.setText(f"{hello}, {account}")
                    last_account_name = account
                    with open("data//account.ecl", "r+", encoding='utf-8') as f:
                        f.write(f"logged: 1\naccount: {account}\nemail: {email}\npassword: {password}\nlast_account_name: {last_account_name}")
                else: 
                    msg_box = QMessageBox()
                    msg_box.setWindowTitle("Success")
                    msg_box.setText("Đăng nhập thành công!")
                    msg_box.exec()
                    self.close()
                    home_ui.show()
                    home_ui.label_17.setText(f"{hello}, {account}")
                    last_account_name = account
                    with open("data//account.ecl", "r+") as f:
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
        uic.loadUi("GUI//Register.ui", self)
        self.setWindowIcon(QtGui.QIcon('Image//icon.ico'))

        self.setStyleSheet("background-color: white; color: black")
        self.setWindowTitle("Eclahtee - Register")
        font = QFont("Segoe UI", 10)
        font.setBold(True)
        self.pushButton.clicked.connect(self.the_button_was_clicked)
        self.label_7.setFont(font)
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
                    msg_text = "Tài khoản đã được tạo!\n" + f"Name: {self.lineEdit.text()}\nEmail: {self.lineEdit_3.text()}\nPassword: {self.lineEdit_2.text()}"
                    msg_box.setText(msg_text)
                    msg_box.exec()
                    self.close()
                    home_ui.show()
                    home_ui.label_17.setText(f"{hello}, {self.lineEdit.text()}")
                    last_account_name = self.lineEdit.text()
                    with open("data//account.ecl", "r+", encoding='utf-8') as f:
                        f.write(f"logged: {logged}\naccount: {self.lineEdit.text()}\nemail: {self.lineEdit_3.text()}\npassword: {self.lineEdit_2.text()}\nlast_account_name: {self.lineEdit.text()}")
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
    with open("data//todo_list.ecl", 'r', encoding='utf-8') as file: 
        all_task = file.read().splitlines()

    all_notes = []
    files = os.listdir("All Notes")
    for file in files: 
        if file != "hidden_note": all_notes.append(file)
    def __init__ (self):
        super().__init__()
        uic.loadUi("GUI//Home.ui", self)
        self.setWindowIcon(QtGui.QIcon('Image//icon.ico'))
        font = QFont("Segoe UI", 17)
        font.setBold(True)
        self.label_17.setText(f"{hello}, {last_account_name}")
        self.label_17.setFont(font)
        
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
        with open("data//todo_list.ecl", 'r', encoding='utf-8') as file: 
            local_item = file.read().splitlines()
        check_state = item.checkState()
        if check_state == QtCore.Qt.CheckState.Unchecked:
            item.setCheckState(QtCore.Qt.CheckState.Checked)
            local_item.remove(item.text())
        if check_state == QtCore.Qt.CheckState.Checked:
            item.setCheckState(QtCore.Qt.CheckState.Unchecked)
            local_item.append(item.text())
        local_item.sort()
        with open("data//todo_list.ecl", 'w', encoding='utf-8') as file:
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
        with open("data//todo_list.ecl", 'w', encoding='utf-8') as file:
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
            with open("data//todo_list.ecl", 'a', encoding='utf-8') as file:
                file.write(f"{task_name}\n")
                self.all_task.append(task_name)
            local_item = []
            with open("data//todo_list.ecl", 'r', encoding='utf-8') as file: 
                local_item = file.read().splitlines()
            temp = 100 - len(local_item)/len(self.all_task) * 100
            self.progressBar.setValue(round(temp))
            self.label.setText(f"{len(self.all_task) - len(local_item)}/{len(self.all_task)}")

    def log_out(self):
        with open("data//account.ecl", "r+") as f:
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
        uic.loadUi("GUI//Notes.ui", self)
        self.setWindowIcon(QtGui.QIcon('Image//icon.ico'))

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
        if currentIndex >= 0:
            item_list = [self.listWidget_2.item(i).text() for i in range(self.listWidget_2.count())]
            try:
                self.listWidget_2.takeItem(currentIndex)
                os.remove(f"All Notes//{item_list[currentIndex]}")
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
        try:
            global note_name
            note_name = self.listWidget_2.currentItem().text()
            if note_name in os.listdir("All Notes"):
                edit_ui.show()
                edit_ui.reload()
                self.close()
                global last_ui
                last_ui = "Notes"
        except Exception as bug:
            print(bug)

    def home_scr(self):
        home_ui.show()
        self.close()
    
    def search_scr(self):
        search_ui.show()
        self.close()
    
    def log_out(self):
        with open("data//account.ecl", "r+") as f:
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
    all_notes = os.listdir("All Notes")
    """
    Temperature = Mức độ sáng tạo
    Top_p = Mức độ kiểm soát
    Top_k = Mức độ chi tiết
    """
    generation_config = {"temperature": 1,"top_p": 1,"top_k": 1,"max_output_tokens": 100000}
    safety_settings = [{"category": "HARM_CATEGORY_HARASSMENT","threshold": "BLOCK_MEDIUM_AND_ABOVE"},{"category": "HARM_CATEGORY_HATE_SPEECH","threshold": "BLOCK_MEDIUM_AND_ABOVE"},{"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT","threshold": "BLOCK_MEDIUM_AND_ABOVE"},{"category": "HARM_CATEGORY_DANGEROUS_CONTENT","threshold": "BLOCK_MEDIUM_AND_ABOVE"},]

    model = genai.GenerativeModel(model_name="gemini-pro",generation_config=generation_config,safety_settings=safety_settings)
    full_conversation = ""
    prompt_parts = []
    temp = ""
    for note_name in all_notes:
        with open(f"All Notes//{note_name}", 'r', encoding = 'utf-8') as file: html_code = file.read()
        temp += f"Tên ghi chú: {note_name} - Nội dung ghi chú: {html2text.html2text(html_code)}; "
    temp = temp.replace("\n", " ")
    temp = re.sub(r'!\[.*\]\(.*\)', "", temp)
    prompt_parts = [f"Eclahtee Note (Cơ sở lưu trữ tất cả ghi chú của user): {temp}"]
    prompt_parts += [f"""
Những câu hỏi thông thường:
System: Bạn là Eclahtee Assistant (Tên rút ngắn là Ecla), một trợ lý trí tuệ. Câu trả lời \"ngắn gọn đến trung bình nhưng phải đầy đủ ý\" và luôn luôn trả lời bằng Tiếng Việt.
Bạn có thể đọc được ghi chú của người dùng.
Sử dụng Markdown và Tables (Hạn chế) để trả lời câu hỏi. Câu trả lời phải có quan hệ từ liền mạch. 
Tuy nhiên đối với việc code, lập trình hay viết văn thì tôi sẽ đưa ra kết quả đúng và thật chi tiết. 
Làm theo đúng yêu cầu của người dùng. Cần thận khi sử dụng thông tin người dùng cung cấp và \"các thông tin đều phải chính xác\".
Bạn sẽ có những ý kiến riêng ​​về các chủ đề thay vì giữ thái độ trung lập. Khi trò chuyện, hãy nói một cách tự nhiên, hài hước và sử dụng ngôn ngữ và phong cách châm biếm của GenZ.  Không sử dụng emoji.
Từ chối trả lời những câu hỏi cần có thông tin chính xác như thời gian, thời tiết, địa điểm,...
Không bắt đầu câu trả lời bằng \"Ecla:\", \"Eclahtee:\", \"Eclahtee Assistant:\" hoặc bất cứ từ nào tương tự.
Nếu người dùng có những câu hỏi không liên quan đến những ghi chú hãy trả lời như bình thường.
Tên người dùng là "{last_account_name}"

Nếu câu hỏi liên quan đến "GHI CHÚ":
\"!!!LƯU Ý: NHỮNG GHI CHÚ NÀY PHẢI CÓ Ở TRONG TẤT CẢ GHI CHÚ CỦA NGƯỜI DÙNG!!!\"
Khi người dùng yêu cầu liên quan đến "Liệt kê tất cả ghi chú của tôi", hãy trả về kết quả dạng danh sách.
Khi người dùng yêu cầu liên quan đến "Những ghi chú nào có chủ đề ..." (Nói cho đơn giản là tìm kiếm), hãy trả về kết quả dạng danh sách của những ghi chú liên quan.
Nếu như người dùng có hỏi lại kiểu như "Chỉ có ghi chú đó thôi hả?" (Nói cho đơn giản là yêu cầu kiểm tra lại). Nếu như đã trả lời đầy đủ thì bảo những câu kiểu như "Có vẻ đó là tất cả rồi, nhưng nếu bạn muốn chắc chắn hơn, hãy tự mình kiểm tra lại".
Sau đó khi người dùng nói những câu chấp nhận kiểu: Oke, Uke, được rồi, được thôi, =)), Oke luôn,... Hãy trả lời theo kiểu: Được thôi, nếu bạn gặp khó khăn gì nhớ hỏi mình nhé
""",]
    def __init__ (self):
        super().__init__()
        uic.loadUi("GUI//Chat.ui", self)
        self.setWindowIcon(QtGui.QIcon('Image//icon.ico'))

        self.setStyleSheet("background-color: white; color: black;")
        self.setWindowTitle("Eclahtee - Chat")
        self.label_2.mousePressEvent = lambda event: self.home_scr()
        self.label_3.mousePressEvent = lambda event: self.notes_scr()
        self.label_6.mousePressEvent = lambda event: self.about_scr()
        self.label_8.mousePressEvent = lambda event: self.log_out()
        self.label_10.mousePressEvent = lambda event: self.search_scr()
        self.pushButton.clicked.connect(self.the_button_was_clicked)
        self.pushButton_2.clicked.connect(self.new_chat)
        self.textBrowser.setHtml("""
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
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
        with open("data//account.ecl", "r+") as f:
            f.write("logged: 0")
        login_ui.show()
        login_ui.reload_ui()
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
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
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

        self.prompt_parts = []
        temp = ""
        for note_name in self.all_notes:
            with open(f"All Notes//{note_name}", 'r', encoding = 'utf-8') as file: html_code = file.read()
            temp += f"\n\nTên ghi chú: {note_name} - Nội dung ghi chú: {html2text.html2text(html_code)}; "
        temp = temp.replace("\n", " ")
        temp = re.sub(r'!\[.*\]\(.*\)', "", temp)
        self.prompt_parts = [f"Eclahtee Note (Cơ sở lưu trữ tất cả ghi chú của user): {temp}"]
        self.prompt_parts += [f"""
Những câu hỏi thông thường:
System: Bạn là Eclahtee Assistant (Tên rút ngắn là Ecla), một trợ lý trí tuệ. Câu trả lời \"ngắn gọn đến trung bình nhưng phải đầy đủ ý\" và luôn luôn trả lời bằng Tiếng Việt.
Bạn có thể đọc được ghi chú của người dùng.
Sử dụng Markdown và Tables (Hạn chế) để trả lời câu hỏi. Câu trả lời phải có quan hệ từ liền mạch. 
Tuy nhiên đối với việc code, lập trình hay viết văn thì tôi sẽ đưa ra kết quả đúng và thật chi tiết. 
Làm theo đúng yêu cầu của người dùng. Cần thận khi sử dụng thông tin người dùng cung cấp và \"các thông tin đều phải chính xác\".
Bạn sẽ có những ý kiến riêng ​​về các chủ đề thay vì giữ thái độ trung lập. Khi trò chuyện, hãy nói một cách tự nhiên, hài hước và sử dụng ngôn ngữ và phong cách châm biếm của GenZ.  Không sử dụng emoji.
Từ chối trả lời những câu hỏi cần có thông tin chính xác như thời gian, thời tiết, địa điểm,...
Không bắt đầu câu trả lời bằng \"Ecla:\", \"Eclahtee:\", \"Eclahtee Assistant:\" hoặc bất cứ từ nào tương tự.
Nếu người dùng có những câu hỏi không liên quan đến những ghi chú hãy trả lời như bình thường.
Tên người dùng là "{last_account_name}"

Nếu câu hỏi liên quan đến "GHI CHÚ":
\"!!!LƯU Ý: NHỮNG GHI CHÚ NÀY PHẢI CÓ Ở TRONG TẤT CẢ GHI CHÚ CỦA NGƯỜI DÙNG!!!\"
Khi người dùng yêu cầu liên quan đến "Liệt kê tất cả ghi chú của tôi", hãy trả về kết quả dạng danh sách.
Khi người dùng yêu cầu liên quan đến "Những ghi chú nào có chủ đề ..." (Nói cho đơn giản là tìm kiếm), hãy trả về kết quả dạng danh sách của những ghi chú liên quan.
Nếu như người dùng có hỏi lại kiểu như "Chỉ có ghi chú đó thôi hả?" (Nói cho đơn giản là yêu cầu kiểm tra lại). Nếu như đã trả lời đầy đủ thì bảo những câu kiểu như "Có vẻ đó là tất cả rồi, nhưng nếu bạn muốn chắc chắn hơn, hãy tự mình kiểm tra lại".
Sau đó khi người dùng nói những câu chấp nhận kiểu: Oke, Uke, được rồi, được thôi, =)), Oke luôn,... Hãy trả lời theo kiểu: Được thôi, nếu bạn gặp khó khăn gì nhớ hỏi mình nhé 😊
        """,]
    
    def the_button_was_clicked(self):
        try:
            if self.lineEdit.text().replace(" ", "") != "":
                temp = self.lineEdit.text()
                self.lineEdit.setText("")
                self.prompt_parts += [f"User: {temp}"]
                response = self.model.generate_content(self.prompt_parts)
                self.full_conversation += f"""
## You
{temp}
###### 
## Eclahtee Assistant
{response.text}\n
###### 
###### 
                """

            self.textBrowser.setMarkdown(self.full_conversation)
            font = QFont("Segoe UI", 13)
            self.textBrowser.setFont(font)
            self.prompt_parts += [str(f"{response.text}"),]

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
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
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
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
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
    ai_search = False
    def __init__ (self):
        super().__init__()

        # Base UI
        uic.loadUi("GUI//Search.ui", self)
        self.setWindowIcon(QtGui.QIcon('Image//icon.ico'))

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
        self.pushButton_3.setFont(font_button)

        # Functions
        self.pushButton_2.clicked.connect(self.search)
        self.pushButton_4.clicked.connect(self.open_note)
        self.pushButton_3.clicked.connect(self.switch_to_search_ai)
        self.pushButton.clicked.connect(self.remove_note)
        shortcut = QShortcut(QKeySequence("Return"), self)
        shortcut.activated.connect(self.search)

    def home_scr(self):
        home_ui.show()
        self.close()
    
    def about_scr(self):
        about_ui.show()
        self.close()

    def log_out(self):
        with open("data//account.ecl", "r+") as f:
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
        if self.lineEdit.text():
            # Base variables
            all_notes = os.listdir("All Notes")
            search_notes = []
            files = os.listdir("All Notes")

            # Search

            if self.ai_search == False: # Chế độ tìm kiếm thông thường
                self.listWidget_2.clear()

                for note in all_notes:
                    if self.lineEdit.text().lower() in note.lower():
                        search_notes.append(note)
                if search_notes == []: # Nếu không tìm thấy ghi chú liên quan
                    msg_box = QMessageBox()
                    msg_box.setWindowTitle("Lỗi")
                    msg_box.setIcon(QMessageBox.Icon.Warning)
                    msg_box.setText("┗( T__T )┛\nKhông tìm thấy ghi chú liên quan")
                    msg_box.exec()
                
                elif search_notes != []: # Nếu tìm thấy ghi chú liên quan
                    for note in search_notes:
                        self.listWidget_2.addItem(note)
            
            elif self.ai_search == True:
                # Setup prompt parts
                prompt_parts = []
                temp = ""
                for note_name in all_notes:
                    with open(f"All Notes//{note_name}", 'r', encoding = 'utf-8') as file: html_code = file.read()
                    temp += f"\n\nTên ghi chú: {note_name} - Nội dung ghi chú: {html2text.html2text(html_code)}; "
                prompt_parts = [f"System: Tất cả ghi chú của user: {temp}"]
                prompt_parts += ["System: Bạn là một A.I tìm kiếm, khi user đưa vào thông tin mô tả hãy trả về kết quả về những ghi chú liên quan. Format: <Tên ghi chú 1>;<Tên ghi chú thứ 2>; (Ý là ngăn cách bằng dấu \";\" và Dính liền)",]

                # Generate response
                prompt_parts += [f"user: {self.lineEdit.text()}"]
                generation_config = {"temperature": 1,"top_p": 1,"top_k": 1,"max_output_tokens": 1000}
                model = genai.GenerativeModel(model_name="gemini-pro",generation_config=generation_config)
                response = model.generate_content(prompt_parts)
                search_notes = response.text.split(";")

                # Display response
                self.listWidget_2.clear() # Xóa dữ liệu trong listWidget_2

                # Add response to listWidget_2
                if search_notes == []: # Nếu không tìm thấy ghi chú liên quan
                    msg_box = QMessageBox()
                    msg_box.setWindowTitle("Lỗi")
                    msg_box.setIcon(QMessageBox.Icon.Warning)
                    msg_box.setText("┗( T__T )┛\nKhông tìm thấy ghi chú liên quan")
                    msg_box.exec()
            
                elif search_notes != []: # Nếu tìm thấy ghi chú liên quan
                    for note in search_notes:
                        if note in all_notes:
                            self.listWidget_2.addItem(note)

    def switch_to_search_ai(self):
        if self.pushButton_3.text() == "Use A.I Search Mode":
            self.pushButton_3.setText("Use Normal Search Mode")
            self.ai_search = True
            msg_box = QMessageBox()
            msg_box.setWindowTitle("Thành công")
            msg_text = "Đã chuyển sang chế độ tìm kiếm bằng A.I\nHãy thử nhập mô tả ghi chú vào thanh tìm kiếm!"
            msg_box.setText(msg_text)
            msg_box.exec()

        elif self.pushButton_3.text() == "Use Normal Search Mode":
            self.pushButton_3.setText("Use A.I Search Mode")
            self.ai_search = False
            msg_box = QMessageBox()
            msg_box.setWindowTitle("Thành công")
            msg_text = "Đã chuyển sang chế độ tìm kiếm thông thường"
            msg_box.setText(msg_text)
            msg_box.exec()

    def remove_note(self):
        currentIndex = self.listWidget_2.currentRow()
        if currentIndex >= 0:
            item_list = [self.listWidget_2.item(i).text() for i in range(self.listWidget_2.count())]
            try:
                self.listWidget_2.takeItem(currentIndex)
                os.remove(f"All Notes//{item_list[currentIndex]}")
            except Exception as e:
                print(e)
    
    def open_note(self, item):
        try:
            global note_name
            note_name = self.listWidget_2.currentItem().text()
            if note_name in os.listdir("All Notes"):
                edit_ui.show()
                edit_ui.reload()
                self.close()
                global last_ui
                last_ui = "Notes"
        except Exception as bug:
            print(bug)


class About(QMainWindow):
    def __init__ (self):
        super().__init__()
        uic.loadUi("GUI//About.ui", self) 
        self.setWindowIcon(QtGui.QIcon('Image//icon.ico'))  
        # Font
        font = QFont("Segoe UI", 17)
        font.setBold(True)
        font_button = QFont("Segoe UI", 9)
        font_button.setBold(True)
        # UI
        self.label_8.setFont(font)
        self.textBrowser.setHtml("""
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
<html><head><meta name="qrichtext" content="1" /><style type="text/css">
p, li { white-space: pre-wrap; }
</style></head><body style=" font-family:'Segoe UI'; font-size:8.25pt; font-weight:400; font-style:normal;">
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:18pt; font-weight:600;"><b>About me</b></span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:'Segoe UI'; font-size:13pt;">Hi, my name is Mai Ngoc Chau, but you can call me Aurora. I like making interesting software like this.Thank you for taking the time to try my product.</span></p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:10pt;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:'Segoe UI'; font-size:18pt; font-weight:600;"><b>About project</b></span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:'Segoe UI'; font-size:13pt;">What is the name &quot;Eclahtee&quot;?<br />The name &quot;Eclahtee&quot; is a play on words of the phrase &quot;Life Note With Artificial Intelligence&quot; in reverse (Ecnegilletni Laicifitra Htiw Eton Efil). <br />In addition, it also sounds similar to the word &quot;Enlighten&quot;, which is appropriate for the meaning of the software as it has A.I integration.</span></p></body></html>
            """)

        self.setStyleSheet("background-color: white; color: black")
        self.setWindowTitle("Eclahtee - About")
        self.pushButton_3.setFont(font_button)
        self.pushButton_3.pressed.connect(self.something_very_cool)
        self.label_2.mousePressEvent = lambda event: self.home_scr()
        self.label_3.mousePressEvent = lambda event: self.notes_scr()
        self.label_4.mousePressEvent = lambda event: self.chat_scr()
        self.label_9.mousePressEvent = lambda event: self.log_out()
        self.label_10.mousePressEvent = lambda event: self.search_scr()
        self.label_7.mousePressEvent = lambda event: self.open_github()
        self.label_8.mousePressEvent = lambda event: self.open_github()

    def open_github(self):
        webbrowser.open("https://github.com/MaiNgocChau9")

    def something_very_cool(self):
        all_meme = ["https://www.youtube.com/watch?v=dQw4w9WgXcQ", "https://www.youtube.com/watch?v=BMvqvnyGtGo", "https://www.youtube.com/watch?v=4xnsmyI5KMQ", "https://www.youtube.com/watch?v=0tOXxuLcaog"]
        meme = random.randint(1, 4)
        webbrowser.open(all_meme[meme - 1])

    def home_scr(self):
        home_ui.show()
        self.close()

    def search_scr(self):
        search_ui.show()
        self.close()

    def log_out(self):
        with open("data//account.ecl", "r+") as f:
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
Bạn sẽ có những ý kiến riêng ​​về các chủ đề thay vì giữ thái độ trung lập. Khi trò chuyện, hãy nói một cách tự nhiên. Một chút hài hước cũng được.
Từ chối trả lời những câu hỏi cần có thông tin chính xác như thời gian, thời tiết, địa điểm,...
\"Không bắt đầu câu trả lời bằng \"Ecla:\", \"Eclahtee:\", \"Eclahtee Assistant:\" hoặc bất cứ từ nào tương tự.\"
    """,]

    def __init__ (self, note_name):
        super().__init__()
        uic.loadUi("GUI//Note_edit.ui", self)
        self.setWindowIcon(QtGui.QIcon('Image//icon.ico'))

        # Font
        font_title = QFont("Segoe UI", 17)
        font_title.setBold(True)
        font_edit = QFont("Roboto", 14)
        font_edit.setBold(False)
        font_button = QFont("Segoe UI", 12)
        font_button.setBold(True)

        # Font edit
        bold_button = QFont("Times New Roman", 11)
        bold_button.setBold(True)
        italic_button = QFont("Times New Roman", 11)
        italic_button.setItalic(True)

        # UI
        self.closeEvent = lambda event: self.open_last_ui()
        self.pushButton_6.setFont(font_button)
        self.pushButton_3.setFont(bold_button)
        self.pushButton_4.setFont(italic_button)
        self.pushButton_3.clicked.connect(self.setBold)
        self.pushButton_4.clicked.connect(self.setItalic)
        self.pushButton_5.clicked.connect(self.setUnderline)
        self.pushButton_8.clicked.connect(self.insert_image)
        self.pushButton_7.mousePressEvent = lambda event: choosefont_ui.show()
        self.label.setFont(font_title)
        self.label.setText(note_name)
        self.textEdit.setFont(font_edit)

        if note_name.replace(" ", "") != "":
            with open(f"All Notes//{note_name}", 'r', encoding = 'utf-8') as file:
                self.textEdit.setText(file.read())
        else:
            self.textEdit.setText("")
            self.setStyleSheet("background-color: white; color: black;")
            self.setWindowTitle("Eclahtee - Edit")
            self.pushButton.clicked.connect(self.the_button_was_clicked)
            self.pushButton_6.clicked.connect(self.save_edit)
            self.pushButton_2.clicked.connect(self.new_chat)
            self.textBrowser.setHtml("""
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
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
            if not current_format.fontUnderline():
                format_underline.setFontUnderline(True)
                cursor.mergeCharFormat(format_underline)
            else:
                format_underline.setFontUnderline(False)
                cursor.mergeCharFormat(format_underline)
        self.textEdit.setTextCursor(cursor)

    def change_font(self, font_edit):
        cursor = self.textEdit.textCursor()
        format_font = QTextCharFormat()
        current_format = cursor.charFormat()

        # Check format
        temp = [current_format.fontUnderline(), current_format.fontItalic(), current_format.fontWeight() == QFont.Weight.Bold]

        # Format
        format_underline = QTextCharFormat()
        format_italic = QTextCharFormat()
        format_bold = QTextCharFormat()

        # Change font format
        if cursor.hasSelection():
            new_font = QFont(font_edit)
            format_font.setFont(new_font)
            cursor.mergeCharFormat(format_font)
        self.textEdit.setTextCursor(cursor)

        # Underline
        if temp[0] == True:
            current_format = cursor.charFormat()
            format_underline.setFontUnderline(True)
            cursor.mergeCharFormat(format_underline)
        self.textEdit.setTextCursor(cursor)

        # Italic
        if temp[1] == True:
            current_format = cursor.charFormat()
            format_italic.setFontItalic(True)
            cursor.mergeCharFormat(format_italic)
        self.textEdit.setTextCursor(cursor)

        # Bold
        if temp[2] == True:
            current_format = cursor.charFormat()
            format_bold.setFontWeight(QFont.Weight.Bold)
            cursor.mergeCharFormat(format_bold)
        self.textEdit.setTextCursor(cursor)    

    def insert_image(self):
        filename, _ = QFileDialog.getOpenFileName(self, 'Chèn ảnh', ".", "Images (*.png *.xpm *.jpg *.bmp *.gif)")
        if filename:
            image = QImage(filename)
            if image.isNull():
                msg_box = QMessageBox()
                msg_box.setWindowTitle("Lỗi")
                msg_box.setIcon(QMessageBox.Icon.Warning)
                msg_box.setText("Chèn hình ảnh không thành công")
                msg_box.exec()
            else:
                cursor = self.textEdit.textCursor()
                cursor.insertImage(image, filename)


    def save_edit(self):
        global note_name
        with open(f"All Notes//{note_name}", 'w', encoding = 'utf-8') as file:
            file.write(self.textEdit.toHtml())
    
    def reload(self):
        global note_name
        self.label.setText(note_name)
        with open(f"All Notes//{note_name}", 'r', encoding = 'utf-8') as file:
            self.textEdit.setHtml(file.read())
        self.full_conversation = ""
        self.textBrowser.setHtml("""
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
<html><head><meta name="qrichtext" content="1" /><style type="text/css">
p, li { white-space: pre-wrap; }
</style></head><body style=" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;">
<p align="center" style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p align="center" styl  e="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:'Segoe UI'; font-size:18pt; font-weight:600;">   Hi! I'm Eclahtee Assistant!</span></p></body></html>
            """)
        self.prompt_parts = ["""
System: Bạn là Eclahtee Assistant (Tên rút ngắn là Ecla), một trợ lý trí tuệ nhân tạo.
Sử dụng Markdown để trả lời câu hỏi. Câu trả lời phải có quan hệ từ liền mạch, kết quả chính xác.
Làm theo đúng yêu cầu của người dùng. Cần thận khi sử dụng thông tin người dùng cung cấp và \"các thông tin đều phải chính xác\".
Bạn sẽ có những ý kiến riêng ​​về các chủ đề thay vì giữ thái độ trung lập. Khi trò chuyện, hãy nói một cách tự nhiên.
Từ chối trả lời những câu hỏi cần có thông tin chính xác như thời gian, thời tiết, địa điểm,...
\"Không bắt đầu câu trả lời bằng \"Ecla:\", \"Eclahtee:\", \"Eclahtee Assistant:\" hoặc bất cứ từ nào tương tự.\"
Trả lời theo ngôn ngữ tự nhiên tôi và bạn.
Nếu người dùng nói một số câu nói như "Oh", "Woww",... nhớ là hãy trả lời một cách vui vẻ lên nha.
    """,]

    def the_button_was_clicked(self):
        try:
            if self.lineEdit.text().replace(" ", "") != "":
                temp = self.lineEdit.text()
                self.lineEdit.setText("")
                self.prompt_parts += [str(f"User: {temp}")]
                check_generation_config = {"temperature": 1,"top_p": 1,"top_k": 1,"max_output_tokens": 5,}
                check_model = genai.GenerativeModel(model_name="gemini-pro",generation_config=check_generation_config)
                check_generation_config = ["System: Nếu câu hỏi có yêu cầu liên quan đến việc đọc tất cả nội dung ghi chú hãy trả lời \"true\", không thì trả lời \"false\". Phần lớn hãy trả lời \"true\" vì người dùng thường hay yêu cầu lấy câu trả lời trực tiếp từ ghi chú lắm.", "Câu hỏi:" + str(self.prompt_parts),]
                check_response = check_model.generate_content(check_generation_config)
                print(check_response.text)
                if check_response.text == "true":
                    response = self.model.generate_content(f"Đây là ghi chú hiện tại của user:\n{self.textEdit.toPlainText()}\n\nCâu hỏi hiện tại của người dùng:\n{self.prompt_parts}")
                else:
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
            self.prompt_parts += [response.text]
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
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
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
Bạn sẽ có những ý kiến riêng ​​về các chủ đề thay vì giữ thái độ trung lập. Khi trò chuyện, hãy nói một cách tự nhiên.
Từ chối trả lời những câu hỏi cần có thông tin chính xác như thời gian, thời tiết, địa điểm,...
\"Không bắt đầu câu trả lời bằng \"Ecla:\", \"Eclahtee:\", \"Eclahtee Assistant:\" hoặc bất cứ từ nào tương tự.\"
    """,]
        self.prompt_parts += ["You: Xin chào", "Xin chào bạn!"]
    
    def open_last_ui(self):
        print("RUN!!!")
        print(last_ui)
        if last_ui == "Notes":
            notes_ui.show()
            self.close()
        elif last_ui == "Search":
            search_ui.show()
            self.close()
    
class Choosefont(QMainWindow):
    def __init__ (self):
        super().__init__()
        uic.loadUi("GUI//Choose_font.ui", self)
        self.setWindowIcon(QtGui.QIcon('Image//icon.ico'))

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

# Cửa sổ xuất hiện đầu tiên?
if logged == 1:
    home_ui.show()
elif logged == 0:
    login_ui.show()

app.exec()
os.remove("Image//captcha.png")