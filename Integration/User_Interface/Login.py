# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Login_Dialog(object):
    def setupUi(self, Login_Dialog):
        Login_Dialog.setObjectName(_fromUtf8("Login_Dialog"))
        Login_Dialog.resize(606, 351)
        Login_Dialog.setStyleSheet(_fromUtf8("QDialog {background-image: url(/home/pi/GitHub/Grocery_Recommendation/Integration/User_Interface/emoji.png);\n"
"}"))
        self.pushButton = QtGui.QPushButton(Login_Dialog)
        self.pushButton.setGeometry(QtCore.QRect(250, 260, 99, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.textEdit = QtGui.QTextEdit(Login_Dialog)
        self.textEdit.setGeometry(QtCore.QRect(263, 160, 256, 32))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.textEdit_2 = QtGui.QTextEdit(Login_Dialog)
        self.textEdit_2.setGeometry(QtCore.QRect(263, 198, 256, 31))
        self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))
        self.label_2 = QtGui.QLabel(Login_Dialog)
        self.label_2.setGeometry(QtCore.QRect(110, 198, 70, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(159, 158, 158))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_2.setPalette(palette)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label = QtGui.QLabel(Login_Dialog)
        self.label.setGeometry(QtCore.QRect(110, 160, 70, 32))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(159, 158, 158))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label.setPalette(palette)
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(Login_Dialog)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.textEdit_2.copy)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.textEdit.copy)
        QtCore.QMetaObject.connectSlotsByName(Login_Dialog)

    def retranslateUi(self, Login_Dialog):
        Login_Dialog.setWindowTitle(_translate("Login_Dialog", "Dialog", None))
        self.pushButton.setText(_translate("Login_Dialog", "Log In", None))
        self.label_2.setText(_translate("Login_Dialog", "Password", None))
        self.label.setText(_translate("Login_Dialog", "Username", None))

import sameer_rc
