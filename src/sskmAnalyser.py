import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, pyqtSlot, QSettings, Qt

from mainwindow import Ui_SSKMAnalyser
from dataparser import DataParser
from plotcanvas import PlotCanvas

class MainWindowUIClass(QtWidgets.QMainWindow, Ui_SSKMAnalyser):
    def __init__( self ):        
        # Configure application settings
        self.settings = QSettings('Kekmania', 'sskmAnalyser')
        
        # Call init of super class
        super().__init__()
        self.setupUi(self)
        
    def setupUi(self, mainwindow):
        # Call setup of super class
        super().setupUi(mainwindow)
        
        # Get last filename from settings file and fill table
        lastFile = self.settings.value("lastDataFile")
        if lastFile is not None:
            self.fillTableWithDataFromFile(lastFile)

        # Initialize plotting canvas
        plotCanvas = PlotCanvas(parent=self.plotPlaceholder)

    def fillTableWithDataFromFile(self, fileName):
        # Parse data into booking class
        dataParser = DataParser(fileName)
        bookings = dataParser.GetAllBookings()

        # Show data in UI table
        self.dataTable.setRowCount(0)
        for row, booking in enumerate(bookings):
            self.dataTable.insertRow(row)
            
            dateItem = QtWidgets.QTableWidgetItem(booking.date)
            bookoingTypeItem = QtWidgets.QTableWidgetItem(booking.bookingType)
            nameItem = QtWidgets.QTableWidgetItem(booking.name)
            purposeItem = QtWidgets.QTableWidgetItem(booking.purpose)
            valueItem = QtWidgets.QTableWidgetItem(booking.value)
            
            valueItem.setTextAlignment(Qt.AlignRight)

            self.dataTable.setItem(row, 0, dateItem)
            self.dataTable.setItem(row, 1, bookoingTypeItem)
            self.dataTable.setItem(row, 2, nameItem)
            self.dataTable.setItem(row, 3, purposeItem)
            self.dataTable.setItem(row, 4, valueItem)
        
        self.dataTable.resizeColumnsToContents()

    # Slots 
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
        
        # Save filename to application settings for next startup
        self.settings.setValue("lastDataFile", fileName)

        # Actually fill the table
        self.fillTableWithDataFromFile(fileName)

if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindowUIClass()    
    ui.show()
    sys.exit(app.exec_())

main()

    