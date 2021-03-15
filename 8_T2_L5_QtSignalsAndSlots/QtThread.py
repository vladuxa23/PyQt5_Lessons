import time
from PySide2 import QtCore, QtWidgets


class MyApp(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)

        self.t = TestThread()

        self.button = QtWidgets.QPushButton("start", self)
        self.button.move(0, 30)
        # self.button.clicked.connect(self.myTimer)
        self.button.clicked.connect(self.t.start)

        self.button2 = QtWidgets.QPushButton("stop", self)
        self.button2.move(0, 60)
        # self.button.clicked.connect(self.myTimer)
        self.button2.clicked.connect(self.stopThread)

        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setEnabled(False)

        self.t.started.connect(lambda: print("Поток запущен"))
        self.t.finished.connect(lambda: print("Поток завершен"))

        self.t.mysignal.connect(self.setLineEditText, QtCore.Qt.QueuedConnection)

    # def setLineEditText(self, text):
    #     self.lineEdit.setText(text)

    @QtCore.Slot()
    def myTimer(self):
        for _ in range(1000, 0, -1):
            self.lineEdit.setText(str(_))
            time.sleep(1)
            QtWidgets.QApplication.processEvents()
    # def stopThread(self):
    #     self.t.status = False


class TestThread(QtCore.QThread):
    mysignal = QtCore.Signal(str)

    def run(self) -> None:
        self.status = True
        count = 1000
        while self.status:
            time.sleep(1)
            self.mysignal.emit(str(count))
            count -= 1


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    myapp = MyApp()
    myapp.show()
    app.exec_()
