import sys
from PyQt5 import QtWidgets, QtCore, QtGui


class TestSettings(QtWidgets.QMainWindow):

    def __init__(self):
        super(TestSettings, self).__init__()

        self.initUI()
        self.loadData()

    def initUI(self):
        centralWidget = QtWidgets.QWidget()
        self.setCentralWidget(centralWidget)

        self.labelName = QtWidgets.QLabel("Имя")
        self.labelName.setMinimumWidth(50)
        self.labelSurname = QtWidgets.QLabel("Фамилия")
        self.labelSurname.setMinimumWidth(50)
        self.labelTelephone = QtWidgets.QLabel("Тел.")
        self.labelTelephone.setMinimumWidth(50)
        self.labelEMail = QtWidgets.QLabel("E-Mail")
        self.labelEMail.setMinimumWidth(50)

        self.lineEditName = QtWidgets.QLineEdit()
        self.lineEditSurname = QtWidgets.QLineEdit()
        self.lineEditTelephone = QtWidgets.QLineEdit()
        self.lineEditEMail = QtWidgets.QLineEdit()

        # self.pushButtonPrint = QtWidgets.QPushButton("Распечатать")

        self.checkBox = QtWidgets.QCheckBox()

        layoutHName = QtWidgets.QHBoxLayout()
        layoutHName.addWidget(self.labelName)
        layoutHName.addWidget(self.lineEditName)
        layoutHSurname = QtWidgets.QHBoxLayout()
        layoutHSurname.addWidget(self.labelSurname)
        layoutHSurname.addWidget(self.lineEditSurname)
        layoutHTelephone = QtWidgets.QHBoxLayout()
        layoutHTelephone.addWidget(self.labelTelephone)
        layoutHTelephone.addWidget(self.lineEditTelephone)
        layoutHEMail = QtWidgets.QHBoxLayout()
        layoutHEMail.addWidget(self.labelEMail)
        layoutHEMail.addWidget(self.lineEditEMail)

        layoutVMain = QtWidgets.QVBoxLayout()
        layoutVMain.addLayout(layoutHName)
        layoutVMain.addLayout(layoutHSurname)
        layoutVMain.addLayout(layoutHTelephone)
        layoutVMain.addLayout(layoutHEMail)
        layoutVMain.addWidget(self.checkBox)
        # layoutVMain.addWidget(self.pushButtonPrint)

        centralWidget.setLayout(layoutVMain)

    def loadData(self):
        self.settings = QtCore.QSettings("MyDataCard")
        #
        self.lineEditName.setText(self.settings.value("Name", "Введите имя"))
        self.lineEditSurname.setText(self.settings.value("Surname", "Введите фамилия"))
        self.lineEditTelephone.setText(self.settings.value("Telephone", "Введите телефон"))
        self.lineEditEMail.setText(self.settings.value("EMail", "Введите e-mail"))
        self.checkBox.setCheckState(self.settings.value("CheckState", 0))

        # self.settings.clear()

    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        self.settings.setValue("Name", self.lineEditName.text())
        self.settings.setValue("Surname", self.lineEditSurname.text())
        self.settings.setValue("Telephone", self.lineEditTelephone.text())
        self.settings.setValue("EMail", self.lineEditEMail.text())
        self.settings.setValue("CheckState", self.checkBox.checkState())

        self.settings.sync()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    windows = TestSettings()
    windows.show()
    app.exec()