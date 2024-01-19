from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
)
from PyQt6.QtGui import QMouseEvent
import sys

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(100, 100, 200, 100)

        self.widget_8 = QWidget(self)
        self.widget_8.setGeometry(10, 10, 100, 100)

        self.widget_8.mousePressEvent = self.on_mouse_press

        self.setWindowTitle("Kiểm tra chuột có đang nhấn vào widget_8 hay không")
        self.show()

    def on_mouse_press(self, event: QMouseEvent):
        if self.widget_8.underMouse():  # Sử dụng phương thức underMouse()
            print("Chuột đang nhấn vào widget_8")
        else:
            print("Chuột không đang nhấn vào widget_8")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())
