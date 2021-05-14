import sys
from PySide2 import QtCore, QtWidgets, QtGui
from functools import partial

def print_something():
    print("Ссылка на функцию")


class MySignalsExample(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        self.setFixedSize(200, 200)

        layout = QtWidgets.QVBoxLayout()
        self.button1 = QtWidgets.QPushButton("1", self)
        self.button2 = QtWidgets.QPushButton("2", self)

        self.cmbbx = QtWidgets.QComboBox(self)
        self.cmbbx.addItems(["1", "2", "3"])

        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        layout.addWidget(self.cmbbx)

        self.setLayout(layout)


        # Ссылка на функцию
        # self.button1.clicked.connect(print_something)

        # Метод класса
        self.button2.clicked.connect(partial(self.print_name, "12345"))

        # Ссылка на класс с методом __call__
        # self.button2.clicked.connect(Test("Вася"))

        # Анонимная функция
        # self.cmbbx.currentTextChanged.connect(
        #     lambda: print(f"Установлено значение {self.cmbbx.currentText()}"))
        # self.button1.clicked.connect(lambda: print(f"button1 отправлен сигнал"))

        # Ссылка на слот
        # self.button1.clicked.connect(Test2.some_function)

    @QtCore.Slot()
    def print_name(self, some_param):
        print(f"Метод класса с параметром {some_param}")


class Test:
    def __init__(self, name):
        self.name = name

    def __call__(self, *args, **kwargs):
        print(f"Привет {self.name}")


class Test2:
    @QtCore.Slot()
    def some_function(self):
        print("12345")


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    myapp = MySignalsExample()
    myapp.show()
    app.exec_()
