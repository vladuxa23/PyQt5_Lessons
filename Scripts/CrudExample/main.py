import sys
import crud_design
from PySide2.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableView
from PySide2 import QtSql
from PySide2 import QtCore

class Form(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = crud_design.Ui_MainWindow()
        self.ui.setupUi(self)

        self.initSQLModel()

        self.ui.pushButton.clicked.connect(self.addToDb)
        self.ui.pushButton_2.clicked.connect(self.updaterow)
        self.ui.pushButton_3.clicked.connect(self.delrow)




        # print(self.ui.tableView.currentIndex().row())

    def initSQLModel(self):

        self.db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('fieldlist.db')
        self.model = QtSql.QSqlTableModel()
        self.model.setTable('field')
        self.model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
        self.model.select()
        self.model.setHeaderData(0, QtCore.Qt.Horizontal, "id")
        self.model.setHeaderData(1, QtCore.Qt.Horizontal, "Name")
        self.model.setHeaderData(2, QtCore.Qt.Horizontal, "Surname")
        self.model.setHeaderData(3, QtCore.Qt.Horizontal, "DOB")
        self.model.setHeaderData(4, QtCore.Qt.Horizontal, "Phone")
        self.ui.tableView.setModel(self.model)

        self.i = self.model.rowCount()

        self.ui.lcdNumber.display(self.i)

    def addToDb(self):
        print(self.i)
        self.model.insertRows(self.i,1)
        self.model.setData(self.model.index(self.i,1),self.ui.lineEdit.text())
        self.model.setData(self.model.index(self.i, 2), self.ui.lineEdit_2.text())
        self.model.setData(self.model.index(self.i,4), self.ui.lineEdit_3.text())
        self.model.setData(self.model.index(self.i,3), self.ui.dateEdit.text())
        self.model.submitAll()
        self.i += 1
        self.ui.lcdNumber.display(self.i)

    def delrow(self):
        if self.ui.tableView.currentIndex().row() > -1:
            self.model.removeRow(self.ui.tableView.currentIndex().row())
            self.i -= 1
            self.model.select()
            self.ui.lcdNumber.display(self.i)
        else:
            QMessageBox.question(self,'Message', "Please select a row would you like to delete", QMessageBox.Ok)
            self.show()

    def updaterow(self):
        if self.ui.tableView.currentIndex().row() > -1:
            record = self.model.record(self.ui.tableView.currentIndex().row())
            record.setValue("Name",self.ui.lineEdit.text())
            record.setValue("Surname",self.ui.lineEdit_2.text())
            record.setValue("DOB", self.ui.dateEdit.text())
            record.setValue("Phone", self.ui.lineEdit_3.text())
            self.model.setRecord(self.ui.tableView.currentIndex().row(), record)
        else:
            QMessageBox.question(self,'Message', "Please select a row would you like to update", QMessageBox.Ok)
            self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    frm = Form()
    frm.show()
    sys.exit(app.exec_())
