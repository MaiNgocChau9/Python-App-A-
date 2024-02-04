#PyQt6
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox, QLabel, QListWidget, QInputDialog
from PyQt6 import QtWidgets, QtGui, QtCore
from PyQt6.QtGui import QFont, QMouseEvent
from PyQt6.QtCore import QEvent
from PyQt6 import uic
import webbrowser
import importlib
import sys

class Main(QMainWindow):
    def __init__ (self):
        super().__init__()
        uic.loadUi("SPCK\\Test\\markdown.ui", self)

        self.textBrowser.setMarkdown("""

[Google] (https://www.google.com)\n
[Google] (https://www.google.com/search?q={thứ người dùng yêu cầu})
https://www.google.com/search?q=abc\n
https://www.facebook.com/search/top/?q=\n
https://www.youtube.com/results?search_query=\n
https://open.spotify.com/search/\n

        """)
        print(self.textBrowser.toPlainText())

    
app = QApplication(sys.argv)
main_ui = Main()
main_ui.show()
sys.exit(app.exec())