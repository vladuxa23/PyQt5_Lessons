import sys
from PySide2 import QtWidgets

class MyWidgets(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.initUi()

        self.pushButton.clicked.connect(lambda: print("QPushButton is clicked"))  # Добавляем слот для сигнала нажатия

    def initUi(self):
        self.pushButton = QtWidgets.QPushButton("Кнопка", parent=self)  # Добавляем QPushButton на форму


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    myWindow = MyWidgets()
    myWindow.show()

    app.exec_()
