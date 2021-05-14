import sys
from PySide2 import QtCore, QtWidgets, QtGui
import my_res

class MyWindowType(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        # self.setWindowFlags(QtCore.Qt.Tool)
        self.setWindowIcon(QtGui.QIcon(":/ico/Resources/ui/ico/Address Book.ico"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    myWindow = MyWindowType()
    # myWindow.setWindowFlag(QtCore.Qt.Popup)
    # myWindow.move(100, 100)
    myWindow.show()

    app.exec_()
