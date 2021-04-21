import sys
from PySide2 import QtWidgets, QtGui


class MyWidgets(QtWidgets.QWidget):

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        self.initUI()

    def initUI(self):
        layout = QtWidgets.QVBoxLayout()
        icon = QtGui.QIcon("Resources/ui/ico/Address Book.ico")
        abc = QtWidgets.QPushButton(icon, "Текст кнопки")

        checkbox = QtWidgets.QCheckBox("Флажок")
        checkbox.setChecked(True)
        print(checkbox.isChecked())

        layout.addWidget(abc)
        layout.addWidget(checkbox)
        self.setLayout(layout)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    myWindow = MyWidgets()
    myWindow.show()

    app.exec_()
