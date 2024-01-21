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