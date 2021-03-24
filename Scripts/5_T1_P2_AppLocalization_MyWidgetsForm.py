from PySide2 import QtCore, QtWidgets, QtGui
from ui import mainTestForm
import time
import os
import ui.my_resources
import random


class CustomTableView(QtGui.QStandardItemModel):

    def __init__(self, parent=None):
        QtGui.QStandardItemModel.__init__(self, parent=parent)

    def data(self, item, role):
        if role == QtCore.Qt.DisplayRole:
            if item.column() == 1:
                try:
                    number = QtGui.QStandardItemModel.data(self, item, QtCore.Qt.DisplayRole)
                    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(number)))
                except ValueError:
                    pass

            if item.column() == 2:
                try:
                    worked = QtGui.QStandardItemModel.data(self, item, QtCore.Qt.DisplayRole)
                    if worked == "1":
                        answer = "Обрабатывался"
                    else:
                        answer = "Не обрабатывался"
                    return answer
                except ValueError:
                    pass

        if role == QtCore.Qt.BackgroundRole:
            if item.row() % 2:
                return QtGui.QColor(QtCore.Qt.lightGray)

        return QtGui.QStandardItemModel.data(self, item, role)


class ComboboxWithCheckBox(QtWidgets.QComboBox):

    def addItem(self, item):

        super(ComboboxWithCheckBox, self).addItem(item)
        item = self.model().item(self.count() - 1, 0)
        item.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
        item.setCheckState(QtCore.Qt.Unchecked)

    def itemChecked(self, index):
        item = self.model().item(index, 0)
        return item.checkState() == QtCore.Qt.Checked

    def checkItems(self):
        checkedItems = []
        for i in range(self.count()):
            if self.itemChecked(i):
                checkedItems.append(self.model().item(i, 0).text())

        return checkedItems

    def paintEvent(self, event):

        painter = QtWidgets.QStylePainter(self)
        painter.setPen(self.palette().color(QtGui.QPalette.Text))
        opt = QtWidgets.QStyleOptionComboBox()
        self.initStyleOption(opt)
        opt.currentText = ",".join(self.checkItems())
        painter.drawComplexControl(QtWidgets.QStyle.CC_ComboBox, opt)
        painter.drawControl(QtWidgets.QStyle.CE_ComboBoxLabel, opt)

        self.setToolTip("\n".join(self.checkItems()))


class DoubleDelegate(QtWidgets.QStyledItemDelegate):

    def createEditor(self, parent, option, index):
        editor = QtWidgets.QDoubleSpinBox(parent, decimals=1)
        editor.setFrame(False)
        editor.setMinimum(-1.7976931348623157e308)
        editor.setMaximum(1.7976931348623157e308)
        editor.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        editor.setSizePolicy(QtWidgets.QSizePolicy.Ignored, editor.sizePolicy().verticalPolicy())

        editor.valueChanged.connect(lambda: print(editor.value()))

        return editor

    def updateEditorGeometry(self, editor, option, index):
        editor.setGeometry(option.rect)


class ComboBoxDelegate(QtWidgets.QStyledItemDelegate):

    def __init__(self, parent=None):
        super(ComboBoxDelegate, self).__init__(parent)
        self.items = []

    def paint(self, painter, option, index):
        if (isinstance(self.parent(), QtWidgets.QAbstractItemView)
                and self.parent().model() is index.model()):
            self.parent().openPersistentEditor(index)
        QtWidgets.QStyledItemDelegate.paint(self, painter, option, index)

    def setItems(self, items):
        self.items = items

    def createEditor(self, widget, option, index):
        editor = QtWidgets.QComboBox(widget)
        editor.addItems(self.items)
        return editor

    def setModelData(self, editor, model, index):
        model.setData(index, editor.currentText(), QtCore.Qt.EditRole)

    def updateEditorGeometry(self, editor, option, index):
        editor.setGeometry(option.rect)


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
        editor.setText("...")

    def updateEditorGeometry(self, editor, option, index):
        editor.setGeometry(option.rect)


class ProgressBarDelegate(QtWidgets.QStyledItemDelegate):
    def __init__(self, parent, color):
        super(ProgressBarDelegate, self).__init__(parent)
        self.color = color

    def paint(self, painter, option, index):
        if index.column() == 4:
            if (isinstance(self.parent(), QtWidgets.QAbstractItemView)
                    and self.parent().model() is index.model()):
                self.parent().openPersistentEditor(index)
            QtWidgets.QStyledItemDelegate.paint(self, painter, option, index)
        else:
            QtWidgets.QStyledItemDelegate.paint(self, painter, option, index)

    def createEditor(self, parent: QtWidgets.QWidget, option: QtWidgets.QStyleOptionViewItem,
                     index: QtCore.QModelIndex) -> QtWidgets.QWidget:
        print(index.data())
        editor = QtWidgets.QProgressBar(parent)
        editor.setRange(0, 0)
        editor.setTextVisible(False)
        editor.setStyleSheet("QProgressBar:chunk {background-color:" + self.color + "; width: 20px; margin: 0.5px}")

        return editor


class MyWidgetsForm(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.ui = mainTestForm.Ui_MainWindow()
        self.ui.setupUi(self)

        self.loadTable()

        self.checkComboBox = ComboboxWithCheckBox()
        self.pb = QtWidgets.QPushButton("Получить данные")
        self.checkComboBox.addItem("")
        self.checkComboBox.addItem("1")
        self.checkComboBox.addItem("2")
        self.checkComboBox.addItem("3")
        self.ui.verticalLayout_11.addWidget(self.checkComboBox)
        self.ui.verticalLayout_11.addWidget(self.pb)

        self.pb.clicked.connect(lambda: print(self.checkComboBox.checkItems()))

        self.pbDelegate.clicked.connect(self.onDelegateClicked)

    def onDelegateClicked(self, pushRow):
        # print(self.ui.tableView.model().index(pushRow.row(), 0).data())
        # print(self.ui.tableView.model().index(pushRow.row(), 1).data())
        # print(self.ui.tableView.model().index(pushRow.row(), 3).data())

        print(self.ui.tableView.model().index(pushRow.row(), 4).data())
        if self.ui.tableView.model().index(pushRow.row(), 4).data() is None or self.ui.tableView.model().index(pushRow.row(), 4).data() == 0:
            prbarDelegate = ProgressBarDelegate(self.ui.tableView, "green")
            self.ui.tableView.setItemDelegateForRow(pushRow.row(), prbarDelegate)

            self.ui.tableView.model().setData(self.ui.tableView.model().index(pushRow.row(), 4), 1,
                                              QtCore.Qt.DisplayRole)

        elif self.ui.tableView.model().index(pushRow.row(), 4).data() == 1:
            prbarDelegate = ProgressBarDelegate(self.ui.tableView, "red")
            self.ui.tableView.setItemDelegateForRow(pushRow.row(), prbarDelegate)

            self.ui.tableView.model().setData(self.ui.tableView.model().index(pushRow.row(), 4), 0,
                                              QtCore.Qt.DisplayRole)

        self.update()



    # ДЛЯ ДЕЛЕГАТОВ
    def loadTable(self):
        headers = ['Путь', 'Число', 'Выбор', 'Обзор', 'Прогресс']

        self.stm = QtGui.QStandardItemModel()
        self.stm.setHorizontalHeaderLabels(headers)
        data = [x for x in os.listdir("Resources") if os.path.isdir(os.path.join("Resources", x))]
        print(data)
        self.stm.setRowCount(len(data))

        self.pbDelegate = PushButtonDelegate(self.ui.tableView)
        self.double = DoubleDelegate(self.ui.tableView)
        self.comboBoxDelegate = ComboBoxDelegate(self.ui.tableView)
        self.comboBoxDelegate.setItems(["", "1234", "5678"])

        for row in range(len(data)):
            self.stm.setItem(row, 0, QtGui.QStandardItem(data[row]))
            self.stm.setItem(row, 1, QtGui.QStandardItem(str(20)))

        self.ui.tableView.setModel(self.stm)
        self.ui.tableView.clearSpans()
        self.ui.tableView.resizeColumnsToContents()
        self.ui.tableView.setItemDelegateForColumn(1, self.double)
        self.ui.tableView.setItemDelegateForColumn(2, self.pbDelegate)
        self.ui.tableView.setItemDelegateForColumn(3, self.comboBoxDelegate)
        # self.ui.tableView.setItemDelegateForColumn(4, self.prbarDelegate)
        self.ui.tableView.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

    # ДЛЯ КАСТОМА
    # def loadTable(self):
    #     headers = ['Путь', 'Время', 'Статус']
    #
    #     stm = CustomTableView()
    #     stm.setHorizontalHeaderLabels(headers)
    #     data = [x for x in os.listdir("Resources") if os.path.isdir(os.path.join("Resources", x))]
    #     print(data)
    #     stm.setRowCount(len(data))
    #     #
    #
    #     for row in range(len(data)):
    #         stm.setItem(row, 0, QtGui.QStandardItem(data[row]))
    #         stm.setItem(row, 1, QtGui.QStandardItem(str(int(time.time() + random.randint(0, 40)))))
    #         stm.setItem(row, 2, QtGui.QStandardItem(str(random.randint(0, 1))))
    #
    #     self.ui.tableView.setModel(stm)
    #     self.ui.tableView.clearSpans()
    #     self.ui.tableView.resizeColumnsToContents()


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    myapp = MyWidgetsForm()
    myapp.show()

    app.exec_()
