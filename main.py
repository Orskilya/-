import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtSql import QSqlDatabase, QSqlQueryModel


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('main.ui', self)
        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('coffee.sqlite')
        self.db.open()
        self.model = QSqlQueryModel(self)
        self.model.setQuery('''SELECT Coffee.ID, Sorts.name as "Сорт", Roasting.title as 
        "Степень прожарки", Ground_in_grains.title as "молотый/в зернах", taste_description as
        "Описание вкуса", price as "Цена", volume as "Объём пачки" FROM Coffee
        INNER JOIN Sorts ON Sorts.ID = Coffee.sort
        INNER JOIN Roasting ON Roasting.ID = Coffee.roasting
        INNER JOIN Ground_in_grains ON Ground_in_grains.ID = Coffee.ground_in_grains''')
        self.tableView.setModel(self.model)
        self.tableView.resizeColumnsToContents()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mn = MainWindow()
    sys.excepthook = except_hook
    mn.show()
    sys.exit(app.exec())
