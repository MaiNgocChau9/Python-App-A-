import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import *


class Pinricpal(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)


        self.resize(97,98)
        self.verticalLayout = QVBoxLayout(self)
        self.verticalLayout.setObjectName("Verticallayout")
        self.label = QLabel(self)
        self.label.setText("Nuevo")
        self.label.setFont(QFont("Arial", 20))

        self.shadow = QGraphicsDropShadowEffect()
        self.shadow.setBlurRadius(20)
        self.label.setGraphicsEffect(self.shadow)

        self.verticalLayout.addWidget(self.label)



app = QApplication([])
principal = Pinricpal()
principal.show()
app.exec_()