# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SSKMAnalyser(object):
    def setupUi(self, SSKMAnalyser):
        SSKMAnalyser.setObjectName("SSKMAnalyser")
        SSKMAnalyser.resize(1114, 865)
        self.centralwidget = QtWidgets.QWidget(SSKMAnalyser)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.vertLayoutMain = QtWidgets.QVBoxLayout()
        self.vertLayoutMain.setObjectName("vertLayoutMain")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.rawDataTab = QtWidgets.QWidget()
        self.rawDataTab.setObjectName("rawDataTab")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.rawDataTab)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.vertLayoutRawDataTab = QtWidgets.QVBoxLayout()
        self.vertLayoutRawDataTab.setObjectName("vertLayoutRawDataTab")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.rawDataTab)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 534, 376))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout.addWidget(self.scrollArea)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.vertLayoutRawDataTab.addLayout(self.horizontalLayout)
        self.dataTable = QtWidgets.QTableWidget(self.rawDataTab)
        self.dataTable.setObjectName("dataTable")
        self.dataTable.setColumnCount(4)
        self.dataTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.dataTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTable.setHorizontalHeaderItem(3, item)
        self.vertLayoutRawDataTab.addWidget(self.dataTable)
        self.verticalLayout_3.addLayout(self.vertLayoutRawDataTab)
        self.tabWidget.addTab(self.rawDataTab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.vertLayoutMain.addWidget(self.tabWidget)
        self.verticalLayout.addLayout(self.vertLayoutMain)
        SSKMAnalyser.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(SSKMAnalyser)
        self.statusbar.setObjectName("statusbar")
        SSKMAnalyser.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(SSKMAnalyser)
        self.toolBar.setObjectName("toolBar")
        SSKMAnalyser.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionOpen_file = QtWidgets.QAction(SSKMAnalyser)
        self.actionOpen_file.setObjectName("actionOpen_file")
        self.toolBar.addAction(self.actionOpen_file)

        self.retranslateUi(SSKMAnalyser)
        self.tabWidget.setCurrentIndex(0)
        self.actionOpen_file.triggered.connect(SSKMAnalyser.openFileSlot)
        QtCore.QMetaObject.connectSlotsByName(SSKMAnalyser)

    def retranslateUi(self, SSKMAnalyser):
        _translate = QtCore.QCoreApplication.translate
        SSKMAnalyser.setWindowTitle(_translate("SSKMAnalyser", "MainWindow"))
        item = self.dataTable.horizontalHeaderItem(0)
        item.setText(_translate("SSKMAnalyser", "Date"))
        item = self.dataTable.horizontalHeaderItem(1)
        item.setText(_translate("SSKMAnalyser", "Name"))
        item = self.dataTable.horizontalHeaderItem(2)
        item.setText(_translate("SSKMAnalyser", "Purpose"))
        item = self.dataTable.horizontalHeaderItem(3)
        item.setText(_translate("SSKMAnalyser", "Value"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.rawDataTab), _translate("SSKMAnalyser", "Raw Data"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("SSKMAnalyser", "Tab 2"))
        self.toolBar.setWindowTitle(_translate("SSKMAnalyser", "toolBar"))
        self.actionOpen_file.setText(_translate("SSKMAnalyser", "Open File"))