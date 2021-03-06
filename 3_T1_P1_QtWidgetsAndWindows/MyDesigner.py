import sys
from PySide2 import QtCore, QtWidgets, QtGui
from functools import partial
import MyDesigner_design
import MyDesigner_resources

class MyDesigner(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.ui = MyDesigner_design.Ui_MainWindow()
        self.res = MyDesigner_resources
        self.ui.setupUi(self)

        self.translator = QtCore.QTranslator()

        self.ui.dockWidget_6.setWindowTitle("Панель виджетов")

        self.ui.actionTranslateToEn.triggered.connect(partial(self.setLocalization, "en"))
        self.ui.actionTranslateToRu.triggered.connect(partial(self.setLocalization, "ru"))

        self.iconH = QtGui.QIcon()
        self.iconH.addFile(u":/layoutICO/horizonatllayout.ico", QtCore.QSize(), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.ui.action.setIcon(self.iconH)

    def translateUi(self):
        self.ui.action.setText(QtWidgets.QApplication.translate("MyDesigner", "Новый..."))

    def changeEvent(self, event):
        """Функция-обработчик событий изменения состояния"""

        if event.type() == QtCore.QEvent.LanguageChange:  # Если "ловим" событие LanguageChange
            self.translateUi()  # Тогда вызываем функцию translateUi()
        super(MyDesigner, self).changeEvent(event)  # Отправляем "родителю" новое состояние

    @QtCore.Slot()
    def setLocalization(self, lang):
        """Функция, являющаяся слотом для кнопок button_ru и button_en"""

        self.translator.load(f"to_{lang}.qm")
        QtWidgets.QApplication.instance().installTranslator(self.translator)  # Устанавливаем локализацию


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    myapp = MyDesigner()
    myapp.show()

    app.exec_()
