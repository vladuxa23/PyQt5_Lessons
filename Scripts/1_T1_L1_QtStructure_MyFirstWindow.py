import sys
from PySide2 import QtWidgets


class MyFirstWindow(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    myWindow = MyFirstWindow()
    myWindow.show()

    app.exec_()
