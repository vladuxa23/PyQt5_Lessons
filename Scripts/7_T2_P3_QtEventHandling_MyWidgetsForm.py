from PySide2 import QtCore, QtWidgets, QtGui
from ui import mainTestForm
from functools import partial


class MyWidgetsForm(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.ui = mainTestForm.Ui_MainWindow()
        self.ui.setupUi(self)

        self.setMouseTracking(True)

        self.ui.pushButton.clicked.connect(self.getScreenInfo)
        self.ui.pushButton_2.clicked.connect(partial(self.editPosition, self.ui.pushButton_2.text()))
        self.ui.pushButton_3.clicked.connect(partial(self.editPosition, self.ui.pushButton_3.text()))
        self.ui.pushButton_4.clicked.connect(partial(self.editPosition, self.ui.pushButton_4.text()))
        self.ui.pushButton_5.clicked.connect(partial(self.editPosition, self.ui.pushButton_5.text()))
        self.ui.pushButton_6.clicked.connect(partial(self.editPosition, self.ui.pushButton_6.text()))

        self.ui.checkBox_2.setShortcut(QtGui.QKeySequence("Ctrl+T"))

        self.ui.lineEdit.installEventFilter(self)
        self.ui.checkBox_2.installEventFilter(self)
        self.ui.dial.installEventFilter(self)


    @QtCore.Slot()
    def getScreenInfo(self):
        screens_count = QtWidgets.QApplication.screens()
        print(f"\n{30*'='} SystemInfo {30*'='}")
        print(f"Кол-во экранов:           {len(screens_count)}")
        print(f"Основное окно:            {QtWidgets.QApplication.primaryScreen().name()}")
        for _ in screens_count:
            print(f"Разрешение экрана         {_.name()} составляет {_.size().width()} на {_.size().height()}")
        print(f"Окно находится на экране  {QtWidgets.QApplication.screenAt(self.pos()).name()}")
        print(f"Размеры окна:             Ширина {self.size().width()} Высота {self.size().height()}")
        print(f"Минимальные размеры окна: Ширина {self.minimumWidth()} Высота {self.minimumHeight()}")
        print(f"Текущее положение:        x = {self.pos().x()} y = {self.pos().y()}")
        print(f"Центр приложения:         x = {self.pos().x() + self.width()/2} y = {self.pos().y() + self.height()/2}")
        print(f"{72 * '='}\n")

    def editPosition(self, buttonText):
        screenWidth = QtWidgets.QApplication.screenAt(self.pos()).size().width()
        screenHeight = QtWidgets.QApplication.screenAt(self.pos()).size().height()

        position = {"Лево/Верх":(0, 0),
                    "Лево/Низ": (0, screenHeight-self.height()-75),
                    "Центр": (screenWidth/2 - self.width()/2, screenHeight/2 - self.height()/2),
                    "Право/Верх": (screenWidth - self.width(), 0),
                    "Право/Низ": (screenWidth- self.width(), screenHeight-self.height()-75)}
        self.move(position.get(buttonText)[0], position.get(buttonText)[1])

    def changeEvent(self, event: QtCore.QEvent) -> None:
        if event.type() == QtCore.QEvent.WindowStateChange:
            if self.isMinimized():
                print("Окно свёрнуто")
            elif self.isMaximized():
                print("Окно развёрнуто")
            elif self.isActiveWindow():
                print("Окно в фокусе ввода")
        QtWidgets.QWidget.changeEvent(self, event)

    def showEvent(self, event:QtGui.QShowEvent) -> None:
        print("Окно отображено")
        QtWidgets.QWidget.showEvent(self, event)

    def hideEvent(self, event:QtGui.QHideEvent) -> None:
        print("Окно скрыто")
        QtWidgets.QWidget.hideEvent(self, event)

    def moveEvent(self, event:QtGui.QMoveEvent) -> None:
        print(f"moveEvent:   x = {event.pos().x()}, y = {event.pos().y()}")
        QtWidgets.QWidget.moveEvent(self, event)

    def resizeEvent(self, event:QtGui.QResizeEvent) -> None:
        print(f"resizeEvent: w = {event.size().width()}, h = {event.size().height()}")
        QtWidgets.QWidget.resizeEvent(self, event)

    def closeEvent(self, event):
        print("work closeEvent")
        # event.accept()

    def event(self, event: QtCore.QEvent) -> bool:
        if event.type() == QtCore.QEvent.Type.Close:
            event.setAccepted(False)

            # reply = QtWidgets.QMessageBox.question(self, "Закрыть окно",
            #                                        "Вы хотите закрыть окно?",
            #                                        QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
            #                                        QtWidgets.QMessageBox.No)
            # if reply == QtWidgets.QMessageBox.Yes:
            #     event.accept()
            # else:
            #     event.ignore()

        if event.type() == QtCore.QEvent.KeyPress:
            print("Клавиша клавиатуры нажата")

        if event.type() == QtCore.QEvent.KeyRelease:
            print("Клавиша клавиатуры отпущена")

        if event.type() == QtCore.QEvent.MouseButtonDblClick:
            print("Двойной щелчок мыши")

        if event.type() == QtCore.QEvent.MouseButtonPress:
            print("Кнопка мыши нажата")

        if event.type() == QtCore.QEvent.MouseButtonRelease:
            print("Кнопка мыши отпущена")

        if event.type() == QtCore.QEvent.MouseMove:
            print(event.pos())

        if event.type() == QtCore.QEvent.Wheel:
            print("Колёсико мыши активно")
            print(event.angleDelta())

        return QtWidgets.QWidget.event(self, event)

    def mouseDoubleClickEvent(self, event: QtGui.QMouseEvent) -> None:
        print(f"event =  {event}")

    def eventFilter(self, watched: QtCore.QObject, event: QtCore.QEvent) -> bool:
        if watched == self.ui.lineEdit:
            if event.type() == QtCore.QEvent.FocusIn:
                print("Окно в фокусе")
            elif event.type() == QtCore.QEvent.FocusOut:
                print("Фокус убран")

        if watched == self.ui.checkBox_2:
            if event.type() == QtCore.QEvent.Shortcut:
                print("Комбинация горячих клавиш нажата")

        if watched == self.ui.dial:
            if event.type() == QtCore.QEvent.Enter:
                print("Указатель наведён на QDial")
            elif event.type() == QtCore.QEvent.Leave:
                print("Указатель убран с QDial")

        return super(MyWidgetsForm, self).eventFilter(watched, event)




if __name__ == "__main__":
    app = QtWidgets.QApplication()

    myapp = MyWidgetsForm()
    myapp.show()

    app.exec_()
