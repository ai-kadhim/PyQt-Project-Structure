# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmMain.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_frmMain(object):
    def setupUi(self, frmMain):
        frmMain.setObjectName("frmMain")
        frmMain.resize(302, 163)
        self.centralwidget = QtWidgets.QWidget(frmMain)
        self.centralwidget.setObjectName("centralwidget")
        self.btnTryMe = QtWidgets.QPushButton(self.centralwidget)
        self.btnTryMe.setGeometry(QtCore.QRect(110, 90, 75, 23))
        self.btnTryMe.setObjectName("btnTryMe")
        self.txtOutput = QtWidgets.QLineEdit(self.centralwidget)
        self.txtOutput.setGeometry(QtCore.QRect(90, 50, 113, 20))
        self.txtOutput.setObjectName("txtOutput")
        frmMain.setCentralWidget(self.centralwidget)

        self.retranslateUi(frmMain)
        QtCore.QMetaObject.connectSlotsByName(frmMain)

    def retranslateUi(self, frmMain):
        _translate = QtCore.QCoreApplication.translate
        frmMain.setWindowTitle(_translate("frmMain", "MainWindow"))
        self.btnTryMe.setText(_translate("frmMain", "Try Me"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    frmMain = QtWidgets.QMainWindow()
    ui = Ui_frmMain()
    ui.setupUi(frmMain)
    frmMain.show()
    sys.exit(app.exec_())

