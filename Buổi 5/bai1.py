from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton
import sys
app = QApplication(sys.argv)
window = QWidget()
button = QPushButton("OK", window)
button.setGeometry(200,200, 100, 50)
window.show()
app.exec()