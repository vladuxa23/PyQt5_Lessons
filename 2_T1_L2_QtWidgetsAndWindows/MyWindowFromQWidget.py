import sys
from PySide2 import QtWidgets


class MyWidgets(QtWidgets.QWidget):

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        # layout = QtWidgets.QHBoxLayout()
        # self.abc = QtWidgets.QPushButton("abc")
        # layout.addWidget(self.abc)
        # self.setLayout(layout)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    myWindow = MyWidgets()
    myWindow.show()

    app.exec_()
