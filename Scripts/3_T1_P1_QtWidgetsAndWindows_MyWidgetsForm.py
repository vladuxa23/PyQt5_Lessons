from PySide2 import QtCore, QtWidgets, QtGui
from ui import mainTestForm
import ui.my_resources
import time

class MyWidgetsForm(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.ui = mainTestForm.Ui_MainWindow()
        self.ui.setupUi(self)

    def loadGUI(self, sp):
        self.setWindowIcon(QtGui.QIcon(QtGui.QPixmap(":/ico/ico/Desktop.ico")))
        self.ui.pushButton_2.setIcon(QtGui.QIcon(QtGui.QPixmap(":/ico/ico/Backup.ico")))

        for _ in range(100):
            time.sleep(0.05)
            if (_ % 10) == 0:
                sp.showMessage(f"Загрузка данных... {_}%", QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter,
                               QtCore.Qt.white)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    splash = QtWidgets.QSplashScreen(QtGui.QPixmap(":/img/img/pyside_logo.png"))
    splash.showMessage("Загрузка данных... 0%", QtCore.Qt.AlignHCenter | QtCore.Qt.AlignBottom, QtCore.Qt.white)
    splash.show()

    myapp = MyWidgetsForm()
    myapp.loadGUI(splash)
    splash.finish(myapp)
    myapp.show()

    app.exec_()
