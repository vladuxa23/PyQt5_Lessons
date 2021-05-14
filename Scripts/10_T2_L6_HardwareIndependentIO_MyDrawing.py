import time
from PySide2 import QtCore, QtWidgets, QtGui


class MyDrawing(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)

    def paintEvent(self, event: QtGui.QPaintEvent) -> None:
        painter = QtGui.QPainter(self)

        # p1 = QtCore.QPoint(10, 10)
        # p2 = QtCore.QPoint(100, 60)

        # painter.drawLine(p1, p2)
        pen = QtGui.QPen()
        pen.setWidth(5)
        pen.setStyle(QtCore.Qt.DashLine)
        brush = QtGui.QBrush(QtCore.Qt.red)
        brush.setStyle(QtCore.Qt.VerPattern)
        pen.setBrush(brush)
        painter.setPen(pen)

        rects = [QtCore.QRect(10, 10, 100, 60),
                 QtCore.QRect(20, 20, 100, 60)]
        painter.drawRects(rects)

        # painter.drawArc(50, 20, 100, 70, 16*0, 16*211)


        # painter.drawRect(10, 10, 100, 60)
        # painter.drawLines([QtCore.QLine(10, 10, 100, 60),
        #                    QtCore.QLine(100, 60, 20, 30)])
        # x1, y1 = 10, 10
        # x2, y2 = 100, 60
        # painter.drawLines(x1, y1, x2, y2)
        # p1 = QtCore.QPoint(10, 10)
        # p2 = QtCore.QPoint(100, 60)
        # painter.drawLine(p1, p2)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    myapp = MyDrawing()
    myapp.show()

    app.exec_()
