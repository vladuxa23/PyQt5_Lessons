import sys
from PySide2 import QtWidgets, QtCore
from functools import partial
from sub_window.MediaPlayer import MediaPlayer


class MyMDIApp(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)

        self.initUI()

        self.programListWidget.itemDoubleClicked.connect(self.addSubWidget)

    def initUI(self):
        # создаем центральный виджет
        self.mdiArea = QtWidgets.QMdiArea()
        self.setCentralWidget(self.mdiArea)

        self.programListWidget = QtWidgets.QListWidget()

        self.widgetPanel = QtWidgets.QDockWidget("Программы", self)
        self.widgetPanel.setWidget(self.programListWidget)

        self.programListWidget.addItems(["Плеер"])

        self.addDockWidget(QtCore.Qt.LeftDockWidgetArea, self.widgetPanel)

    def addSubWidget(self):
        self.player = MediaPlayer()
        print(self.player)

        self.PROGRAMM_LIST = {"Плеер": self.player}

        self.mdiArea.addSubWindow(self.PROGRAMM_LIST[self.programListWidget.currentItem().text()])
        self.PROGRAMM_LIST[self.programListWidget.currentItem().text()].show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    myapp = MyMDIApp()
    myapp.show()

    app.exec_()
