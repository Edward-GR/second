import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt
import random

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Yellow Circles')
        self.button = QPushButton('Draw Circle', self)
        self.button.move(100, 150)
        self.button.clicked.connect(self.drawCircle)
        self.show()


    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawCircles(qp)
        qp.end()


    def drawCircles(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        diameter = random.randint(10, 100)
        x = random.randint(0, self.width() - diameter)
        y = random.randint(0, self.height() - diameter)
        qp.drawEllipse(x, y, diameter, diameter)


    def drawCircle(self):
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
