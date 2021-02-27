import sys
from PySide2 import QtWidgets


class MyWidgets(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.initUi()

        self.pushButton.clicked.connect(lambda: print("Button is clicked"))

    def initUi(self):
        self.pushButton = QtWidgets.QPushButton("Кнопка", parent=self)  # Добавляем кнопку на форму


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    myWindow = MyWidgets()
    myWindow.show()

    app.exec_()
