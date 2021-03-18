import sys
from random_word import RandomWords
from PySide2 import QtCore, QtWidgets, QtGui


class MyModelsPreview(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.rndWords = RandomWords()

        self.initUi()






    def initUi(self):
        # центральное окно
        centralWidget = QtWidgets.QWidget()
        self.setCentralWidget(centralWidget)

        self.setMinimumSize(500, 700)
        self.setMaximumSize(500, 700)
        # модели
        lm = self.createQStringListModel()

        # виджеты
        self.comboBox = QtWidgets.QComboBox()
        self.comboBox.setModel(lm)

        self.listView = QtWidgets.QListView()
        self.listView.setModel(lm)

        self.tableView = QtWidgets.QTableView()
        self.tableView.setModel(self.createQStandardItemModel())
        self.tableView.resizeColumnsToContents()  # Нежелательно делать для большого количества данных

        self.treeView = QtWidgets.QTreeView()
        self.treeView.setModel(self.createQStandardItemModel())

        # компоновка
        layoutV1 = QtWidgets.QVBoxLayout()
        layoutV1.addWidget(self.comboBox)
        layoutV1.addWidget(self.listView)
        layoutV1.addWidget(self.tableView)
        layoutV1.addWidget(self.treeView)

        centralWidget.setLayout(layoutV1)


    def createQStringListModel(self):
        lst = self.rndWords.get_random_words()[:]
        return QtCore.QStringListModel(lst)

    def createQStandardItemModel(self):
        sim = QtGui.QStandardItemModel()
        lst = self.rndWords.get_random_words()
        for row, elem in enumerate(lst):
            item1 = QtGui.QStandardItem(str(row+1))
            item2 = QtGui.QStandardItem(lst[row])
            sim.appendRow([item1, item2])
        sim.setHorizontalHeaderLabels(["№ п/п", "Слово"])

        return sim

# Основное отличие в QStringListModel и QStandardItemModel



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    myWindow = MyModelsPreview()
    myWindow.show()

    app.exec_()
