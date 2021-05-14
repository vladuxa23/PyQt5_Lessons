import sys
from PySide2 import QtCore, QtWidgets, QtGui


class MyEventHandler(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)

        self.button1 = QtWidgets.QPushButton("1", self)
        self.button2 = QtWidgets.QPushButton("2", self)
        self.button2.move(0, 50)

        self.button2.installEventFilter(self)

    # def closeEvent(self, event):
    #     reply = QtWidgets.QMessageBox.question(self, "Закрыть окно?",
    #                                            "Вы действительно хотите закрыть окно?",
    #                                            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
    #                                            QtWidgets.QMessageBox.No)
    #     if reply == QtWidgets.QMessageBox.Yes:
    #         event.accept()
    #     else:
    #         event.ignore()

    # def event(self, event: QtCore.QEvent) -> bool:
    #     # print(event.type())
    #     if event.type() == QtCore.QEvent.Type.Wheel:
    #         print(event.angleDelta())
            # print(f"Ширина: {event.size().width()}")
            # print(f"Старая ширина: {event.oldSize().width()}")
            # print(f"Высота: {self.size().height()}")

        # return QtWidgets.QWidget.event(self, event)

    def eventFilter(self, watched: QtCore.QObject, event: QtCore.QEvent) -> bool:
        if watched == self.button2 and event.type() == QtCore.QEvent.KeyPress:
            print("key pressed")
        if watched == self.button2 and event.type() == QtCore.QEvent.MouseButtonDblClick:
            print("mouse pressed")

        return super(MyEventHandler, self).eventFilter(watched, event)

    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None:
        print(event.text())

    def mouseDoubleClickEvent(self, event: QtGui.QMouseEvent) -> None:
        print(event.type())




if __name__ == "__main__":
    app = QtWidgets.QApplication()

    myapp = MyEventHandler()
    myapp.show()
    app.exec_()
