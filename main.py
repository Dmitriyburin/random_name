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
        uic.loadUi('untitled.ui', self)
        self.setWindowTitle('Супрематизм')
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

    def draw_square(self, qp):
        qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
        side = randint(5, 100)
        qp.drawRect(self.mouse_x - side // 2, self.mouse_y - side // 2, side, side)

    def draw_circle(self, qp):
        qp.setBrush(QColor(246, 255, 0))
        diameter = randint(5, 100)
        qp.drawEllipse(0, 0,
                       diameter, diameter)

    def draw_triangle(self, qp):
        print('yep')
        qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
        side = randint(5, 100)
        points = QPolygon([self.mouse_x, int(self.mouse_y - side * 0.6),
                           int(self.mouse_x + side // 2), int(self.mouse_y + side * 0.3),
                           int(self.mouse_x - side // 2), int(self.mouse_y + side * 0.3)])
        qp.drawPolygon(points)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
