from PyQt6.QtWidgets import QApplication, QTextBrowser, QVBoxLayout, QWidget

app = QApplication([])

window = QWidget()
layout = QVBoxLayout(window)

text_browser = QTextBrowser()
layout.addWidget(text_browser)
temp = "ABC"
text = "DEF"

# Sử dụng HTML và CSS để đặt kích thước chữ khác nhau
html_content = """
    <p style="font-size: 22px;"><b>You</b></p>
    <p style="font-size: 14px;"><b>{temp}</b></p>
    <p style="font-size: 14px;"></p>
    <p style="font-size: 14px;"></p>
    <p style="font-size: 22px;"><b>Gemini</b></p>
    <p style="font-size: 14px;"><b>{text}</b></p>
    <p style="font-size: 14px;"></p>
    <p style="font-size: 14px;"></p>
"""

text_browser.setHtml(html_content)

window.show()
app.exec()
