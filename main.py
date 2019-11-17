import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from random import randint


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.f)
        self.flag = False

    def f(self):  # Обновление флага
        self.flag = True
        self.update()

    def paintEvent(self, event):  # Функция рисования
        x = randint(30, 750)
        y = randint(30, 550)
        size = randint(50, 350)
        if self.flag:
            painter = QPainter(self)
            painter.setBrush(QColor(255, 255, 0))
            painter.drawEllipse(x, y, size, size)  # Рисование окружности

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
