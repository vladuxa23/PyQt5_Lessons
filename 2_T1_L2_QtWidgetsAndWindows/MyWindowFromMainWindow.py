import sys
from PySide2 import QtWidgets


class MyWidgets(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        # # menuBar отсутствует у QWidgets
        # self.fileMenu = self.menuBar().addMenu('File')
        # self.fileMenu.addAction("Open")
        # # toolBar отсутствует у QWidgets
        # self.toolBar = self.addToolBar("Edit")
        # self.toolBar.addAction("Edit")
        # # statusBar отсутствует у QWidgets
        # self.appStatusBar = self.statusBar()
        # self.appStatusBar.showMessage("Status: Ok!")
        #
        # centralWidget = QtWidgets.QWidget()
        # self.setCentralWidget(centralWidget)
        # layout = QtWidgets.QHBoxLayout()
        # self.abc = QtWidgets.QPushButton("abc")
        # layout.addWidget(self.abc)
        #
        # centralWidget.setLayout(layout)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    myWindow = MyWidgets()
    myWindow.show()

    app.exec_()
