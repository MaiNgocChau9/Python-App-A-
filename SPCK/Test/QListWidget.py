import sys
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QListWidget,
    QListWidgetItem,
)
from PyQt6.QtCore import Qt


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.list_widget = QListWidget()
        self.list_widget.setObjectName("list_widget")
        self.list_widget.setGeometry(10, 10, 200, 100)

        # Thêm item vào QListWidget
        for i in range(10):
            item = QListWidgetItem(str(i))
            item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
            self.list_widget.addItem(item)

        self.setWindowTitle("Thêm check box vào QListWidget")
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())
