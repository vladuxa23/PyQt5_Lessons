import sys
from PySide2 import QtWidgets  # Импорт класса, который содержит элементы окна


class MyFirstWindow(QtWidgets.QMainWindow):  # Наследуемся от QWidget

    def __init__(self, parent=None):                 # Создаем конструктор класса
        super(MyFirstWindow, self).__init__(parent)  # Передаем конструктору ссылку на родительский компонент
        QtWidgets.qApp.argv()


if __name__ == "__main__":
    app = QtWidgets.QApplication()  # Создаем  объект приложения
    # app = QtWidgets.QApplication(sys.argv)  # Если PyQt

    myWindow = MyFirstWindow()  # Создаём объект окна
    myWindow.show()  # Показываем окно

    app.exec_()  # Если exit, то код дальше не исполняется

    print(1)
