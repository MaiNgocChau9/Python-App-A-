from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QGraphicsBlurEffect
from PyQt6.QtGui import QPixmap, QColor, QBrush, QPainter
from PyQt6.QtCore import Qt

class BlurredWidget(QWidget):
    def __init__(self):
        super().__init__()

        # Tạo widget chính
        main_widget = QWidget(self)
        main_layout = QVBoxLayout(main_widget)

        # Tạo label hoặc widget bạn muốn áp dụng hiệu ứng blur
        content_label = QLabel("Nội dung của widget", main_widget)
        content_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Thêm widget vào layout chính
        main_layout.addWidget(content_label)

        # Áp dụng hiệu ứng blur cho widget chính
        blur = QGraphicsBlurEffect(self)
        blur.setBlurRadius(10)  # Điều chỉnh độ mờ ở đây
        main_widget.setGraphicsEffect(blur)

        # Đặt nền cho widget chính (phần phía sau blur)
        background = self.capture_widget_background(main_widget)
        palette = main_widget.palette()
        palette.setBrush(palette.ColorRole.Window, QBrush(QColor(255, 255, 255, 128)))
        main_widget.setPalette(palette)

        # Thiết lập thuộc tính về việc xóa độ mờ khi widget mất focus (nếu cần)
        main_widget.setFocusPolicy(Qt.FocusPolicy.ClickFocus)

        # Thiết lập layout chính cho cửa sổ
        self.setLayout(main_layout)
        self.setWindowTitle("Blurred Widget")
        self.setGeometry(100, 100, 400, 300)

    def capture_widget_background(self, widget):
        # Chụp nền của widget
        pixmap = QPixmap(widget.size())
        widget.render(pixmap)
        return pixmap.toImage()

if __name__ == "__main__":
    app = QApplication([])
    window = BlurredWidget()
    window.show()
    app.exec()
