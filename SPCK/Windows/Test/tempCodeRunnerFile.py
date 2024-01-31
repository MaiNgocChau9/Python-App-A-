def saveNote(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_name, _ = QFileDialog.getSaveFileName(self, "Save Note", "", "Text Files (*.txt);;All Files (*)", options=options)

        if file_name:
            with open(file_name, 'w') as file:
                file.write(self.text_edit.toPlainText())
                print(self.text_edit.toPlainText())