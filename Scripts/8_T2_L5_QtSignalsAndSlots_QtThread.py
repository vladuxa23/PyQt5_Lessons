import time
from PySide2 import QtCore, QtWidgets


class MyApp(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.t = TestThread()
        self.initUi()

    def initUi(self):
        centralWidget = QtWidgets.QWidget()
        self.setCentralWidget(centralWidget)

        layout = QtWidgets.QVBoxLayout()

        self.button = QtWidgets.QPushButton("start")
        self.button.clicked.connect(self.t.start)

        self.button2 = QtWidgets.QPushButton("stop")
        # self.button.clicked.connect(self.myTimer)
        self.button2.clicked.connect(self.stopThread)

        self.lineEdit = QtWidgets.QLineEdit()
        self.lineEdit.setEnabled(False)

        self.prBar = QtWidgets.QProgressBar()
        self.prBar.setRange(0, 100)
        self.prBar.setValue(0)
        self.prBar.setTextVisible(True)

        layout.addWidget(self.button)
        layout.addWidget(self.button2)
        layout.addWidget(self.lineEdit)
        layout.addWidget(self.prBar)

        centralWidget.setLayout(layout)

        self.t.started.connect(lambda: print("Поток запущен"))
        self.t.finished.connect(lambda: print("Поток завершен"))

        self.t.mysignal.connect(self.setLineEditText, QtCore.Qt.QueuedConnection)

    def setLineEditText(self, text):
        self.lineEdit.setText(text)
        self.prBar.setValue(int(text))

    def stopThread(self):
        self.t.status = False

    @QtCore.Slot()
    def myTimer(self):
        for _ in range(5, 0, -1):
            self.lineEdit.setText(str(_))
            time.sleep(1)
            QtWidgets.QApplication.processEvents()


class TestThread(QtCore.QThread):
    mysignal = QtCore.Signal(str)

    def run(self) -> None:
        self.status = True
        count = 0
        while self.status:
            time.sleep(1)
            self.mysignal.emit(str(count))
            count += 1
            if count == 100:
                break


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    myapp = MyApp()
    myapp.show()
    app.exec_()
