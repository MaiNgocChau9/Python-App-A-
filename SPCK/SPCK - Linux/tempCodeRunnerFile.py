    self.setStyleSheet("background-color: white; color: black;")
            self.setWindowTitle("Eclahtee - Edit")
            self.pushButton.clicked.connect(self.the_button_was_clicked)
            self.pushButton_6.clicked.connect(self.save_edit)
            self.pushButton_2.clicked.connect(self.new_chat)
            self.pushButton_3.clicked.connect(self.reload)
            self.textBrowser.setHtml("""