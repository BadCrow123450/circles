from PyQt6 import QtWidgets, uic
import io
import sys
import random
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtCore import QPointF
from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(507, 435)
        self.pushButton = QtWidgets.QPushButton(parent=Form)
        self.pushButton.setGeometry(QtCore.QRect(370, 400, 131, 31))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "push to create circle"))


class MainW(QtWidgets.QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.random_circle)
        self.need_draw = False

    def random_circle(self):
        self.update()

    def paintEvent(self, a0):
        if self.need_draw:
            painter = QPainter()
            painter.begin(self)
            painter.setBrush(QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
            radius = random.randint(20, 200)
            painter.drawEllipse(QPointF(250, 250), radius, radius)
            painter.end()
        else:
            self.need_draw = True



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = MainW()
    ex.show()
    sys.exit(app.exec())
