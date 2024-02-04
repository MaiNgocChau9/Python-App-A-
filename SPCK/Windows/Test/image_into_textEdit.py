from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
import sys

class ImageTextEdit(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.text_edit = QTextEdit(self)
        self.setCentralWidget(self.text_edit)

        # Thêm nút chèn ảnh vào thanh công cụ
        insert_image_action = QAction(QIcon('path_to_image_icon.png'), 'Chèn ảnh', self)
        insert_image_action.triggered.connect(self.insert_image)

        toolbar = self.addToolBar('Toolbar')
        toolbar.addAction(insert_image_action)

        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('Image in QTextEdit')
        self.show()

    def insert_image(self):
        filename, _ = QFileDialog.getOpenFileName(self, 'Chèn ảnh', ".", "Images (*.png *.xpm *.jpg *.bmp *.gif)")
        if filename:
            image = QImage(filename)
            if image.isNull():
                popup = QMessageBox(QMessageBox.Critical,
                                    "Lỗi khi tải ảnh",
                                    "Không thể tải được tệp ảnh!",
                                    QMessageBox.Ok,
                                    self)
                popup.show()
            else:
                cursor = self.text_edit.textCursor()
                cursor.insertImage(image, filename)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ImageTextEdit()
    sys.exit(app.exec())
