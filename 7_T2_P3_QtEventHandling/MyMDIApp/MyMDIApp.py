import sys
from PySide2 import QtWidgets
import MyMDIApp_design

class MyMDIApp(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.ui = MyMDIApp_design.Ui_MainWindow()
        self.ui.setupUi(self)

        self.leftPanel = QtWidgets.QDockWidget("Наши приложения", self)

        w = QtWidgets.QWidget(self.leftPanel)
        self.leftPanel.setWidget(w)

        lay = QtWidgets.QVBoxLayout(w)
        lay.setSpacing(1)
        lay.setContentsMargins(1,1,1,1)
        w.setLayout(lay)
        self.listWidgets = QtWidgets.QListWidget(self.leftPanel)
        lay.addWidget(self.listWidgets)
        self.listWidgets.addItems(["1", "2"])

        # w = QtWidgets.QWidget(self.tre)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    myapp = MyMDIApp()
    myapp.show()

    app.exec_()
