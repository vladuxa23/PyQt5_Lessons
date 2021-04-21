import sys
from PySide2 import QtCore, QtWidgets, QtGui


def print_something():
    print("Ссылка на функцию")


class MySignalsExample(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)

        t = Test()

        self.setFixedSize(200, 200)

        self.button1 = QtWidgets.QPushButton("1", self)
        self.button2 = QtWidgets.QPushButton("2", self)
        self.button2.move(0, 50)
        self.cmbbx = QtWidgets.QComboBox(self)
        self.cmbbx.addItems(["1", "2", "3"])
        self.cmbbx.move(0, 100)

        # Ссылка на функцию
        # self.button1.clicked.connect(print_something)

        # Метод класса
        # self.button2.clicked.connect(self.print_name)

        # Ссылка на класс с методом __call__
        # self.button2.clicked.connect(Test())

        # Анонимная функция
        # self.cmbbx.currentTextChanged.connect(
        #     lambda: print(f"Установлено значение {self.cmbbx.currentText()}"))
        # self.button1.clicked.connect(lambda: print(f"button1 отправлен сигнал"))

    def print_name(self):
        print("Метод класса")


class Test:
    def __call__(self, *args, **kwargs):
        print(f"Отработал __call__")


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    myapp = MySignalsExample()
    myapp.show()
    app.exec_()
