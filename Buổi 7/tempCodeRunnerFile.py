import sys
from PyQt6.QtWidgets import QApplication, QMessageBox

app = QApplication(sys.argv)
msg_box = QMessageBox()
#msg_box.setWindowTitle("Lỗi")
#msg_box.setIcon(QMessageBox.Icon.Warning)
#msg_box.setText("Vui lòng nhập email hoặc số điện thoại!")
#msg_box.setStyleSheet("background-color: #F8F2EC; color: #356a9c")
sys.exit(msg_box.exec())