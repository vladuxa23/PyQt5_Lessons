import sys
from PySide2 import QtCore, QtWidgets, QtGui


class MyEventHandler(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)

        self.button1 = QtWidgets.QPushButton("1", self)
        self.button2 = QtWidgets.QPushButton("2", self)
        self.button2.move(0, 50)

        self.someButton.installEventFilter(self)


        self.button2.installEventFilter(self)

    def closeEvent(self, event):
        print("work closeEvent")
        # event.accept()

    def event(self, event: QtCore.QEvent) -> bool:
        if event.type() == QtCore.QEvent.Type.Close:
            event.setAccepted(False)
        return QtWidgets.QWidget.event(self, event)

        # reply = QtWidgets.QMessageBox.question(self, "Привет",
        #                                        "Ура",
        #                                        QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
        #                                        QtWidgets.QMessageBox.No)
        # if reply == QtWidgets.QMessageBox.Yes:
        #     event.accept()
        # else:
        #     event.ignore()

    def eventFilter(self, watched: QtCore.QObject, event: QtCore.QEvent) -> bool:

        return super(MyEventHandler, self).eventFilter(watched, event)

    # def mouseDoubleClickEvent(self, event: QtGui.QMouseEvent) -> None:
    #     print(event)
    #


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    myapp = MyEventHandler()
    myapp.show()
    app.exec_()
