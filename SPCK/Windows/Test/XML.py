import sys
from PyQt6.QtWidgets import *
from PyQt6 import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *

class NoteApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.text_edit = QTextEdit(self)
        self.setCentralWidget(self.text_edit)

        # Tạo menu
        menubar = self.menuBar()
        file_menu = menubar.addMenu('File')
        edit_menu = menubar.addMenu('Edit')
        format_menu = menubar.addMenu('Format')

        # Tạo các action
        save_action = QAction('Save', self)
        save_action.triggered.connect(self.saveNote)
        file_menu.addAction(save_action)

        bold_action = QAction('Bold', self)
        bold_action.triggered.connect(self.setBold)
        edit_menu.addAction(bold_action)

        italic_action = QAction('Italic', self)
        italic_action.triggered.connect(self.setItalic)
        edit_menu.addAction(italic_action)

        font_action = QAction('Font', self)
        font_action.triggered.connect(self.chooseFont)
        format_menu.addAction(font_action)

        self.setWindowTitle('Note App')
        self.setGeometry(100, 100, 800, 600)
        self.show()

    def saveNote(self):
        options = QFileDialog.options()
        options |= QFileDialog.ReadOnly
        file_name, _ = QFileDialog.getSaveFileName(self, "Save Note", "", "Text Files (*.txt);;All Files (*)", options=options)

        if file_name:
            with open(file_name, 'w') as file:
                file.write(self.text_edit.toPlainText())
                print(self.text_edit.toPlainText())

    def setBold(self):
        cursor = self.text_edit.textCursor()
        format_bold = QTextCharFormat()
        format_bold.setFontWeight(QFont.Weight.Bold)

        if cursor.hasSelection():
            cursor.mergeCharFormat(format_bold)
        else:
            current_format = cursor.charFormat()
            if current_format.fontWeight() == QFont.Weight.Normal:
                cursor.mergeCharFormat(format_bold)
            else:
                format_bold.setFontWeight(QFont.Weight.Normal)
                cursor.mergeCharFormat(format_bold)
        self.text_edit.setTextCursor(cursor)

    def setItalic(self):
        cursor = self.text_edit.textCursor()
        format_italic = QTextCharFormat()
        format_italic.setFontItalic(True)

        if cursor.hasSelection():
            cursor.mergeCharFormat(format_italic)
        else:
            current_format = cursor.charFormat()
            if current_format.fontItalic():
                cursor.mergeCharFormat(format_italic)
            else:
                format_italic.setFontItalic(False)
                cursor.mergeCharFormat(format_italic)
        self.text_edit.setTextCursor(cursor)

    def chooseFont(self):
        font, ok = QFontDialog.getFont(self.text_edit.currentFont(), self)
        if ok:
            self.text_edit.setCurrentFont(font)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    note_app = NoteApp()
    sys.exit(app.exec())
