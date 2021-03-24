from PySide2 import QtCore, QtWidgets, QtGui


class ProgressBarDelegate(QtWidgets.QStyledItemDelegate):
    def __init__(self, parent, color):
        super(ProgressBarDelegate, self).__init__(parent)
        self.color = color

    def paint(self, painter, option, index):
        if index.column() == 2:
            if (isinstance(self.parent(), QtWidgets.QAbstractItemView)
                    and self.parent().model() is index.model()):
                self.parent().openPersistentEditor(index)
            QtWidgets.QStyledItemDelegate.paint(self, painter, option, index)
        else:
            QtWidgets.QStyledItemDelegate.paint(self, painter, option, index)

    def createEditor(self, parent: QtWidgets.QWidget, option: QtWidgets.QStyleOptionViewItem,
                     index: QtCore.QModelIndex) -> QtWidgets.QWidget:

        editor = QtWidgets.QProgressBar(parent)
        editor.setRange(0, 0)
        editor.setTextVisible(False)
        editor.setStyleSheet("QProgressBar:chunk {background-color:" + self.color + "; width: 20px; margin: 0.5px}")
        editor.valueChanged.connect(self.setMyStyle)

        return editor

    @staticmethod
    def setMyStyle():
        print("123")


class PushButtonDelegate(QtWidgets.QStyledItemDelegate):
    clicked = QtCore.Signal(QtCore.QModelIndex)

    def paint(self, painter, option, index):
        if (isinstance(self.parent(), QtWidgets.QAbstractItemView)
                and self.parent().model() is index.model()):
            self.parent().openPersistentEditor(index)
        QtWidgets.QStyledItemDelegate.paint(self, painter, option, index)

    def createEditor(self, parent, option, index):
        button = QtWidgets.QPushButton(parent)
        button.clicked.connect(lambda *args, ix=index: self.clicked.emit(ix))

        return button

    def setEditorData(self, editor, index):
        editor.setText("Start/Stop")

    def updateEditorGeometry(self, editor, option, index):
        editor.setGeometry(option.rect)


class MyWidgetsForm(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)

        self.initUi()
        self.initModel()

        self.pbDelegate.clicked.connect(self.onPBDelegateClicked)

    def onPBDelegateClicked(self, pushRow):
        print(self.tableView.model().index(pushRow.row(), 2).data())
        if self.tableView.model().index(pushRow.row(), 2).data() is None or self.tableView.model().index(pushRow.row(),
                                                                                                         2).data() == 0:

            prbarDelegate = ProgressBarDelegate(self.tableView, "green")
            self.tableView.setItemDelegateForColumn(pushRow.row(), prbarDelegate)

            self.tableView.model().setData(self.tableView.model().index(pushRow.row(), 2), 1,
                                           QtCore.Qt.DisplayRole)

        elif self.tableView.model().index(pushRow.row(), 2).data() == 1:
            prbarDelegate = ProgressBarDelegate(self.tableView, "red")
            self.tableView.setItemDelegateForColumn(pushRow.row(), prbarDelegate)

            self.tableView.model().setData(self.tableView.model().index(pushRow.row(), 2), 0,
                                           QtCore.Qt.DisplayRole)

    def initUi(self):
        self.setFixedSize(600, 300)

        self.tableView = QtWidgets.QTableView()
        layout = QtWidgets.QHBoxLayout()
        layout.addWidget(self.tableView)
        cw = QtWidgets.QWidget()
        cw.setLayout(layout)
        self.setCentralWidget(cw)

    def initModel(self):
        headers = ['Путь', 'Управление', 'Прогресс']
        self.pbDelegate = PushButtonDelegate(self.tableView)
        prbarDelegate = ProgressBarDelegate(self.tableView, "red")
        self.stm = QtGui.QStandardItemModel()
        self.stm.setHorizontalHeaderLabels(headers)

        for row in range(5):
            self.stm.setItem(row, 0, QtGui.QStandardItem("some_path" + str(row)))
            self.stm.setItem(row, 1, QtGui.QStandardItem())



        self.tableView.setModel(self.stm)
        self.tableView.clearSpans()
        self.tableView.setItemDelegateForColumn(1, self.pbDelegate)
        self.tableView.setItemDelegateForColumn(2, prbarDelegate)
        self.tableView.resizeColumnsToContents()
        self.tableView.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    myapp = MyWidgetsForm()
    myapp.show()

    app.exec_()