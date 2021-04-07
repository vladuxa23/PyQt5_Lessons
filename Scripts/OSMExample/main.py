import os
import re
import sys
import requests
from PySide2 import QtCore, QtWidgets, QtWebEngineWidgets, QtWebChannel

# https://www.youtube.com/watch?v=6c6KX0GjUI8&ab_channel=TKST1102


class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi()

        self.pushButtonCheckIP.clicked.connect(self.getIPInfo)

    def setupUi(self):
        file = os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            "src/main/assets/map.html",)

        mainLayout = QtWidgets.QHBoxLayout()
        mainMap = QtWidgets.QVBoxLayout()
        rightPanel = QtWidgets.QVBoxLayout()

        # mainMap
        sp = QtWidgets.QSizePolicy()
        sp.setVerticalStretch(0)

        self.label = QtWidgets.QLabel()
        self.label.setSizePolicy(sp)

        self.view = QtWebEngineWidgets.QWebEngineView()
        self.channel = QtWebChannel.QWebChannel()
        self.channel.registerObject("MainWindow", self)
        self.view.page().setWebChannel(self.channel)
        self.view.setUrl(QtCore.QUrl.fromLocalFile(file))

        mainMap.addWidget(self.label)
        mainMap.addWidget(self.view)

        # rightPanel
        label = QtWidgets.QLabel("Проверить IP")
        label.setMinimumWidth(120)
        self.lineEditCheckIP = QtWidgets.QLineEdit()
        self.lineEditCheckIP.setPlaceholderText("Введите IP для проверки")
        self.pushButtonCheckIP = QtWidgets.QPushButton("Проверить")

        rightPanel.addWidget(label)
        rightPanel.addWidget(self.lineEditCheckIP)
        rightPanel.addWidget(self.pushButtonCheckIP)
        rightPanel.addStretch(1)

        mainLayout.addLayout(mainMap)
        mainLayout.addLayout(rightPanel)
        self.setLayout(mainLayout)

    @QtCore.Slot(float, float)
    def onMapMove(self, lat, lng):
        self.label.setText("Текущие координаты:\nДолгота: {:.5f}, Широта: {:.5f}".format(lng, lat))

    @QtCore.Slot()
    def getIPInfo(self):
        def getIPValidation(ip):
            if len(ip) != 0:
                reg = "^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$"
                if re.match(reg, ip) is not None:
                    return True
                else:
                    return False
            else:
                QtWidgets.QMessageBox.about(self, "Внимание", "Введите IP - адрес")

        ip = self.lineEditCheckIP.text()

        if getIPValidation(ip) is False:
            QtWidgets.QMessageBox.warning(self, "Ошибка", "Введенные данные не являются IP - адресом")
            return None

        response = requests.get(f"http://ip-api.com/json/{ip}")
        response = response.json()
        print(response)

        if response.get('status') != 'success':
            QtWidgets.QMessageBox.about(self, "Уведомление", "IP - адрес не найден")
            return None

        page = self.view.page()
        # page.runJavaScript(f"map.panTo(L.latLng({response.get('lat')}, {response.get('lon')}));")
        page.runJavaScript(f"map.setView([{response.get('lat')}, {response.get('lon')}], 14);")
        page.runJavaScript(f"L.marker([{response.get('lat')}, {response.get('lon')}]) .addTo(map)"
                           f".bindPopup('<b>Провайдер:</b>{response.get('isp')}<br><b>Организация:</b> {response.get('org')}')"
                           f".openPopup();")
        circleOpt = "{color: 'blue', fillColor: '#B8E1E9', fillOpacity: 0.4, radius: 500}"
        page.runJavaScript("L.circle([{0}, {1}], {2}).addTo(map);"
                           .format(response.get('lat'), response.get('lon'), circleOpt))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
