import json
import requests
from PySide2 import QtCore, QtWidgets, QtGui

# API
# https://rapidapi.com/cloud-actions-cloud-actions-default/api/language-translation/endpoints

class TranslateAPIApp(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)

        self.initUI()

        self.button.clicked.connect(self.translator)

    def initUI(self):

        self.textEditFrom = QtWidgets.QTextEdit()
        self.textEditFrom.setPlaceholderText("Введите русский текст")
        self.textEditTo = QtWidgets.QTextEdit()
        self.textEditTo.setPlaceholderText("Переведённый текст")
        self.button = QtWidgets.QPushButton("Перевести")

        layoutV = QtWidgets.QVBoxLayout()
        layoutH = QtWidgets.QHBoxLayout()

        layoutH.addWidget(self.textEditFrom)
        layoutH.addWidget(self.textEditTo)
        layoutV.addLayout(layoutH)
        layoutV.addWidget(self.button)

        centralWidget = QtWidgets.QWidget()
        centralWidget.setLayout(layoutV)
        self.setCentralWidget(centralWidget)

    def translator(self):
        print(str())
        url = "https://language-translation.p.rapidapi.com/translateLanguage/translate"

        querystring = {
            "text": self.textEditFrom.toPlainText(),
            "type": "plain", "target": "ru"}

        headers = {
            'x-rapidapi-key': "fcc2302543msh291a911d795577bp127b5fjsn326e8482b68c",
            'x-rapidapi-host': "language-translation.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        print(response.text)
        data = json.loads(response.text)
        self.textEditTo.setText(data['translatedText'])


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    myapp = TranslateAPIApp()
    myapp.show()
    app.exec_()


