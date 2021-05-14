from PySide2 import QtWidgets, QtCore, QtGui
import MainForm

class MainTestWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainTestWindow, self).__init__(parent)

        self.ui = MainForm.Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = MainTestWindow()
    window.show()

    app.exec_()