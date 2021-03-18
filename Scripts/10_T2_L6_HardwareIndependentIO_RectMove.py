import sys, os
from PySide2 import QtCore, QtWidgets, QtGui
# from PySide2.QtCore import Qt, QRect
# from PySide2.QtGui import QPainter, QPen, QMouseEvent, QHoverEvent
# from PySide2.QtWidgets import QApplication, QWidget


class MyWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.capture = False
        self.rect = QtCore.QRect(10, 10, 200, 100)

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        pen = QtGui.QPen()
        pen.setWidth(5)
        pen.setStyle(QtCore.Qt.DashDotLine)
        painter.setPen(pen)
        painter.drawRect(self.rect)

    def mousePressEvent(self, event: QtGui.QMouseEvent):
        x, y = event.pos().x(), event.pos().y()
        valid = x > self.rect.x() and y > self.rect.y()
        valid = valid and x < (self.rect.x() + self.rect.width())
        valid = valid and y < (self.rect.y() + self.rect.height())
        if valid:
            self.capture = True
            self.rect = QtCore.QRect(x, y, 200, 100)
            self.repaint()

    def mouseReleaseEvent(self, event: QtGui.QMouseEvent):
        self.capture = False

    def mouseMoveEvent(self, event: QtGui.QMouseEvent):
        if self.capture:
            x, y = event.pos().x(), event.pos().y()
            self.rect = QtCore.QRect(x, y, 200, 100)
            self.repaint()


if __name__ == '__main__':
    app = QtWidgets.QApplication()

    w = MyWidget()
    w.show()

    app.exec_()





