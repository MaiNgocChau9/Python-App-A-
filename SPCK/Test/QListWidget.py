from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox, QLabel, QListWidget
from PyQt6 import QtWidgets, QtGui, QtCore
from PyQt6.QtGui import QFont
from PyQt6 import uic
import sys


class Example(QMainWindow):
    def __init__(self):
        super().__init__()

        self.list_widget = QListWidget()
        self.list_widget.setObjectName("list_widget")
        self.list_widget.setGeometry(10, 10, 200, 100)

        # Thêm item vào QListWidget
        for i in range(10):
            item = QListWidget(str(i))
            item.setFlags(item.flags() | Qt.ItemIsUserCheckable | Qt.ItemIsEnabled | Qt.ItemIsSelectable)
            item.setFrame(False)
            self.list_widget.addItem(item)

        self.setWindowTitle("Tắt viền xung quanh các mục được chọn")
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())
