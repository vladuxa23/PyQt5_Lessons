import time
from PySide2 import QtCore, QtWidgets, QtGui
import ui.my_resources


class MySpalshExample(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)

    @staticmethod
    def loadGUI(sp):
        for _ in range(100):
            time.sleep(0.05)
            if (_ % 10) == 0:
                sp.showMessage(f"Загрузка данных... {_}%", QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter, QtCore.Qt.white)


if __name__ == "__main__":
    app = QtWidgets.QApplication()
    res = my_resources
    splash = QtWidgets.QSplashScreen(QtGui.QPixmap(":/img/img/pyside_logo.png"))
    splash.showMessage("Загрузка данных... 0%", QtCore.Qt.AlignHCenter | QtCore.Qt.AlignBottom, QtCore.Qt.white)
    splash.show()
    QtWidgets.QApplication.processEvents()

    myapp = MySpalshExample()
    myapp.loadGUI(splash)
    myapp.show()

    splash.finish(myapp)

    app.exec_()
