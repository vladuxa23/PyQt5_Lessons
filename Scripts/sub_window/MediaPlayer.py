import sys
from PySide2 import QtWidgets, QtCore, QtGui, QtMultimedia


class ProgressSlider(QtWidgets.QSlider):

    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None:
        super(ProgressSlider, self).mousePressEvent(event)
        if event.button() == QtCore.Qt.LeftButton:
            val = self.getValue(event.pos())
            print(val)
            self.setValue(val)

    def getValue(self, position):
        option = QtWidgets.QStyleOptionSlider()
        self.initStyleOption(option)
        gr = self.style().subControlRect(QtWidgets.QStyle.CC_Slider, option, QtWidgets.QStyle.SC_SliderGroove, self)
        sr = self.style().subControlRect(QtWidgets.QStyle.CC_Slider, option, QtWidgets.QStyle.SC_SliderHandle, self)

        if self.orientation() == QtCore.Qt.Horizontal:
            sliderLenght = sr.width()
            sliderMin = gr.x()
            sliderMax = gr.right() - sliderLenght + 1
        else:
            sliderLenght = sr.height()
            sliderMin = gr.y()
            sliderMax = gr.bottom() - sliderLenght + 1

        pr = position - sr.center() + sr.topLeft()
        p = pr.x() if self.orientation() == QtCore.Qt.Horizontal else pr.y()

        return QtWidgets.QStyle.sliderValueFromPosition(self.minimum(), self.maximum(), p - sliderMin, sliderMax - sliderMin, option.upsideDown)


class MediaPlayer(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)

        self.initUI()

        self.currentPlayList = QtMultimedia.QMediaPlaylist()
        self.player = QtMultimedia.QMediaPlayer()

        self.userAction = -1

        # self.player.mediaStatusChanged.connect(self.qmp_mediaStatusChanged)
        # self.player.stateChanged.connect(self.qmp_stateChanged)
        # self.player.positionChanged.connect(self.qmp_positionChanged)
        # self.player.volumeChanged.connect(self.qmp_volumeChanged)
        self.player.setVolume(60)

        # self.statusBar().showMessage("No Media ")
        #
        # self.colModel = QtGui.QStandardItemModel()
        #
        #
        # self.pushButtonAddTrack.clicked.connect(self.addTrack)
        # self.pushButtonPlayMusic.clicked.connect(self.player.play)
        # self.pushButtonStopMusic.clicked.connect(self.player.stop)

    def initUI(self):
        self.setWindowTitle("MusicPlayer")
        self.setFixedSize(300, 450)

        centralWidget = QtWidgets.QWidget()
        self.setCentralWidget(centralWidget)

        self.treeViewMusicList = QtWidgets.QTreeView()

        self.pushButtonAddTrack = QtWidgets.QPushButton("+", self)
        self.pushButtonDelTrack = QtWidgets.QPushButton("-", self)
        self.pushButtonPlayMusic = QtWidgets.QPushButton("Play", self)
        self.pushButtonStopMusic = QtWidgets.QPushButton("Stop", self)

        self.progressSliderTrack = ProgressSlider()
        self.progressSliderTrack.setOrientation(QtCore.Qt.Horizontal)

        layoutHButton = QtWidgets.QHBoxLayout()
        layoutHButton.addWidget(self.pushButtonAddTrack)
        layoutHButton.addWidget(self.pushButtonDelTrack)
        layoutHButton.addWidget(self.pushButtonPlayMusic)
        layoutHButton.addWidget(self.pushButtonStopMusic)

        layoutV = QtWidgets.QVBoxLayout()
        layoutV.addWidget(self.treeViewMusicList)
        layoutV.addWidget(self.progressSliderTrack)
        layoutV.addLayout(layoutHButton)

        centralWidget.setLayout(layoutV)

    def addItemToColumnModel(self, path, trackTime):
        self.colModel.appendRow([QtGui.QStandardItem(str(path)),
                                 QtGui.QStandardItem(str(trackTime))])

    def addTrack(self):
        path, ok = QtWidgets.QFileDialog.getOpenFileName(self, caption="Выбор трэка", filter="*.mp3 *.wav")

        if ok:
            self.addItemToColumnModel(path, "1234")
            self.treeViewMusisList.setModel(self.colModel)

    def playTrack(self):
        try:
            track = QtMultimedia.QMediaContent(QtCore.QUrl.fromLocalFile(self.treeViewMusisList.selectedIndexes()[0].data(QtCore.Qt.DisplayRole)))
            self.player.setMedia(track)
            self.player.setVolume(50)
            self.player.play()
        except IndexError:
            QtWidgets.QMessageBox.warning(self, "Ошибка", "Трэк для воспроизведения не выбран")

    def exitAction(self):
        exitAc = QtWidgets.QAction("&Exit", self)




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    myapp = MediaPlayer()
    myapp.show()

    app.exec_()
