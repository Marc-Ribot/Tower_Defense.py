# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\mribo\OneDrive\Documents\6è quadri\Tower_Defense.py\Mapa1.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1038, 600)
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        MainWindow.setStyleSheet("background-color: rgb(0, 170, 255);")
        MainWindow.setIconSize(QtCore.QSize(300, 300))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Dinero = QtWidgets.QLabel(self.centralwidget)
        self.Dinero.setGeometry(QtCore.QRect(260, 10, 91, 41))
        self.Dinero.setObjectName("Dinero")
        self.Oleada = QtWidgets.QLabel(self.centralwidget)
        self.Oleada.setGeometry(QtCore.QRect(120, 10, 101, 51))
        self.Oleada.setObjectName("Oleada")
        self.Diners = QtWidgets.QLabel(self.centralwidget)
        self.Diners.setGeometry(QtCore.QRect(70, -10, 1141, 601))
        self.Diners.setObjectName("Diners")
        self.Torre_1 = QtWidgets.QPushButton(self.centralwidget)
        self.Torre_1.setGeometry(QtCore.QRect(620, 450, 101, 91))
        self.Torre_1.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Torretas/Torre cost 1.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Torre_1.setIcon(icon)
        self.Torre_1.setIconSize(QtCore.QSize(100, 100))
        self.Torre_1.setObjectName("Torre_1")
        self.Torre_2 = QtWidgets.QPushButton(self.centralwidget)
        self.Torre_2.setGeometry(QtCore.QRect(740, 450, 101, 91))
        self.Torre_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Torretas/Torre cost 2.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Torre_2.setIcon(icon1)
        self.Torre_2.setIconSize(QtCore.QSize(100, 100))
        self.Torre_2.setObjectName("Torre_2")
        self.Torre_5 = QtWidgets.QPushButton(self.centralwidget)
        self.Torre_5.setGeometry(QtCore.QRect(870, 450, 101, 91))
        self.Torre_5.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/Torretas/Torre cost 5.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Torre_5.setIcon(icon2)
        self.Torre_5.setIconSize(QtCore.QSize(100, 100))
        self.Torre_5.setObjectName("Torre_5")
        self.progressBarLife = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBarLife.setGeometry(QtCore.QRect(810, 60, 161, 61))
        self.progressBarLife.setProperty("value", 24)
        self.progressBarLife.setObjectName("progressBarLife")
        self.Diners.raise_()
        self.Dinero.raise_()
        self.Oleada.raise_()
        self.Torre_1.raise_()
        self.Torre_2.raise_()
        self.Torre_5.raise_()
        self.progressBarLife.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1038, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Dinero.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Dinero: $0</span></p></body></html>"))
        self.Oleada.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">Oleada: 0</span></p></body></html>"))
        self.Diners.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/Mapa/1.jpg\"/></p></body></html>"))
import Imatges_rc
