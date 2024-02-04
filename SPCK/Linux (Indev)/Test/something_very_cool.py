from PyQt6.QtWidgets import QWidget, QCloseEvent

app = QApplication([])

widget = QWidget()
widget.closeEvent = lambda event: print("Chương trình bị tắt")

widget.show()
app.exec()
