import csv
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, pyqtSlot

from mainwindow import Ui_SSKMAnalyser
from booking import Booking
from plotcanvas import PlotCanvas

class MainWindowUIClass(QtWidgets.QMainWindow, Ui_SSKMAnalyser):
    def __init__( self ):        
        # Call init of super class
        super().__init__()
        self.setupUi(self)
        
    def setupUi(self, mainwindow):
        # Call setup of super class
        super().setupUi(mainwindow)

        #m = PlotCanvas(self, width=4, height=3)
        #m.move(200,0)

    # slot
    @QtCore.pyqtSlot()
    def openFileSlot(self):
        
        # Open file dialog
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(
                        None,
                        "Open file",
                        "",
                        "CSV files (*.csv)",
                        options=options)
        # Parse file 
        if fileName:
            with open(fileName, 'r', encoding='iso8859_16') as csvfile:
                reader = csv.reader(csvfile, delimiter=';')                
                
                for i, row in enumerate(reader):
                    # Skip first line
                    if i == 0:
                        continue

                    booking = Booking(row[1], row[4], row[11], row[14])
                    totalRows = self.tableWidget.rowCount()
                    self.tableWidget.insertRow(totalRows)
                    self.tableWidget.setItem(totalRows-1, 0, QtWidgets.QTableWidgetItem(booking.date))
                    self.tableWidget.setItem(totalRows-1, 1, QtWidgets.QTableWidgetItem(booking.name))
                    self.tableWidget.setItem(totalRows-1, 2, QtWidgets.QTableWidgetItem(booking.purpose))
                    self.tableWidget.setItem(totalRows-1, 3, QtWidgets.QTableWidgetItem(booking.value))



if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindowUIClass()    
    ui.show()
    sys.exit(app.exec_())

main()

    