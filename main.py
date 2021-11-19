import sys
from random import randint

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QLabel
from PyQt5.QtGui import QPainter, QColor, QPolygon
from PyQt5 import uic


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.pushButton.clicked.connect(self.click)
        self.button_clicked = None

    def initUI(self):
        uic.loadUi('UI.ui', self)
        self.setWindowTitle('main')
        self.do_paint = False
        self.setMouseTracking(True)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()
        self.do_paint = False

    def mousePressEvent(self, event):
        self.mouse_x, self.mouse_y = event.x(), event.y()
        self.button_clicked = event.button()

    def click(self):
        self.paint()

    def draw_circle(self, qp):
        qp.setBrush(QColor(246, 255, 0))
        diameter = randint(5, 100)
        qp.drawEllipse(0, 0,
                       diameter, diameter)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
