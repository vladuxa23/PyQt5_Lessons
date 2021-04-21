import sys
from PySide2 import QtWidgets

class MyWidgets(QtWidgets.QWidget):

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.initUi()

        # self.pushButton.clicked.connect(lambda: print("QPushButton is clicked"))  # Добавляем слот для сигнала нажатия

    def initUi(self):
        # self.pushButton = QtWidgets.QPushButton("Кнопка", parent=self)  # Добавляем QPushButton на форму
        layout = QtWidgets.QVBoxLayout()
        tb = QtWidgets.QTabWidget()
        tb.addTab(QtWidgets.QLabel("1234"), "123")
        tb.setTabPosition(QtWidgets.QTabWidget.West)
        layout.addWidget(tb)

        self.setLayout(layout)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    myWindow = MyWidgets()
    myWindow.show()

    app.exec_()
