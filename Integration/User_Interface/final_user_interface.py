# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TestSuper.ui'
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

class Ui_Recommend_Dialog(object):
    def setupUi(self, Recommend_Dialog):
        Recommend_Dialog.setObjectName(_fromUtf8("Recommend_Dialog"))
        Recommend_Dialog.resize(602, 352)
        Recommend_Dialog.setStyleSheet(_fromUtf8("QDialog{border-image: url(:/new_image_path/fandv.jpg);}"))
        self.tabLayout = QtGui.QTabWidget(Recommend_Dialog)
        self.tabLayout.setGeometry(QtCore.QRect(10, 10, 581, 331))
        self.tabLayout.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.tabLayout.setMouseTracking(False)
        self.tabLayout.setAutoFillBackground(False)
        self.tabLayout.setStyleSheet(_fromUtf8("background-color: rgb(255, 239, 175);"))
        self.tabLayout.setTabPosition(QtGui.QTabWidget.North)
        self.tabLayout.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabLayout.setIconSize(QtCore.QSize(30, 30))
        self.tabLayout.setElideMode(QtCore.Qt.ElideNone)
        self.tabLayout.setTabsClosable(True)
        self.tabLayout.setMovable(True)
        self.tabLayout.setObjectName(_fromUtf8("tabLayout"))
        self.ShoppingList = QtGui.QWidget()
        self.ShoppingList.setObjectName(_fromUtf8("ShoppingList"))
        self.pushButton = QtGui.QPushButton(self.ShoppingList)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 111, 27))
        self.pushButton.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.checkBox_3 = QtGui.QCheckBox(self.ShoppingList)
        self.checkBox_3.setGeometry(QtCore.QRect(14, 137, 20, 21))
        self.checkBox_3.setText(_fromUtf8(""))
        self.checkBox_3.setObjectName(_fromUtf8("checkBox_3"))
        self.checkBox_5 = QtGui.QCheckBox(self.ShoppingList)
        self.checkBox_5.setGeometry(QtCore.QRect(14, 213, 20, 21))
        self.checkBox_5.setText(_fromUtf8(""))
        self.checkBox_5.setObjectName(_fromUtf8("checkBox_5"))
        self.checkBox_2 = QtGui.QCheckBox(self.ShoppingList)
        self.checkBox_2.setGeometry(QtCore.QRect(14, 100, 20, 21))
        self.checkBox_2.setText(_fromUtf8(""))
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.textEdit_2 = QtGui.QTextEdit(self.ShoppingList)
        self.textEdit_2.setGeometry(QtCore.QRect(40, 95, 523, 31))
        self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))
        self.checkBox_6 = QtGui.QCheckBox(self.ShoppingList)
        self.checkBox_6.setGeometry(QtCore.QRect(14, 250, 20, 21))
        self.checkBox_6.setText(_fromUtf8(""))
        self.checkBox_6.setObjectName(_fromUtf8("checkBox_6"))
        self.textEdit_5 = QtGui.QTextEdit(self.ShoppingList)
        self.textEdit_5.setGeometry(QtCore.QRect(40, 208, 523, 31))
        self.textEdit_5.setObjectName(_fromUtf8("textEdit_5"))
        self.checkBox_1 = QtGui.QCheckBox(self.ShoppingList)
        self.checkBox_1.setGeometry(QtCore.QRect(14, 62, 20, 21))
        self.checkBox_1.setText(_fromUtf8(""))
        self.checkBox_1.setObjectName(_fromUtf8("checkBox_1"))
        self.textEdit_6 = QtGui.QTextEdit(self.ShoppingList)
        self.textEdit_6.setGeometry(QtCore.QRect(40, 245, 523, 32))
        self.textEdit_6.setObjectName(_fromUtf8("textEdit_6"))
        self.textEdit_3 = QtGui.QTextEdit(self.ShoppingList)
        self.textEdit_3.setGeometry(QtCore.QRect(40, 132, 523, 32))
        self.textEdit_3.setObjectName(_fromUtf8("textEdit_3"))
        self.checkBox_4 = QtGui.QCheckBox(self.ShoppingList)
        self.checkBox_4.setGeometry(QtCore.QRect(14, 175, 20, 21))
        self.checkBox_4.setText(_fromUtf8(""))
        self.checkBox_4.setObjectName(_fromUtf8("checkBox_4"))
        self.textEdit_1 = QtGui.QTextEdit(self.ShoppingList)
        self.textEdit_1.setGeometry(QtCore.QRect(40, 57, 523, 32))
        self.textEdit_1.setObjectName(_fromUtf8("textEdit_1"))
        self.textEdit_4 = QtGui.QTextEdit(self.ShoppingList)
        self.textEdit_4.setGeometry(QtCore.QRect(40, 170, 523, 32))
        self.textEdit_4.setObjectName(_fromUtf8("textEdit_4"))
        self.tabLayout.addTab(self.ShoppingList, _fromUtf8(""))
        self.Recommender = QtGui.QWidget()
        self.Recommender.setObjectName(_fromUtf8("Recommender"))
        self.scrollArea = QtGui.QScrollArea(self.Recommender)
        self.scrollArea.setGeometry(QtCore.QRect(0, 0, 601, 311))
        self.scrollArea.setStyleSheet(_fromUtf8("background-color: rgb(255, 239, 175);"))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 599, 309))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.label_4 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_4.setGeometry(QtCore.QRect(30, 40, 70, 70))
        self.label_4.setMinimumSize(QtCore.QSize(70, 70))
        self.label_4.setStyleSheet(_fromUtf8("image: url(:/new_image_path/icon_milk.png);"))
        self.label_4.setText(_fromUtf8(""))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_5.setGeometry(QtCore.QRect(130, 50, 161, 70))
        self.label_5.setStyleSheet(_fromUtf8("font: 14pt \"Monospace\";"))
        self.label_5.setText(_fromUtf8(""))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_6.setGeometry(QtCore.QRect(30, 120, 70, 70))
        self.label_6.setStyleSheet(_fromUtf8("image: url(:/new_image_path/beer.png);"))
        self.label_6.setText(_fromUtf8(""))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_7.setGeometry(QtCore.QRect(130, 120, 161, 70))
        self.label_7.setStyleSheet(_fromUtf8("font: 14pt \"Monospace\";"))
        self.label_7.setText(_fromUtf8(""))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_8.setGeometry(QtCore.QRect(30, 190, 70, 70))
        self.label_8.setStyleSheet(_fromUtf8("image: url(:/new_image_path/soap.png);"))
        self.label_8.setText(_fromUtf8(""))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_9.setGeometry(QtCore.QRect(130, 190, 171, 70))
        self.label_9.setStyleSheet(_fromUtf8("font: 14pt \"Monospace\";"))
        self.label_9.setText(_fromUtf8(""))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.tabLayout.addTab(self.Recommender, _fromUtf8(""))

        self.retranslateUi(Recommend_Dialog)
        self.tabLayout.setCurrentIndex(1)
        QtCore.QObject.connect(self.checkBox_1, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.textEdit_1.copy)
        QtCore.QObject.connect(self.checkBox_5, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.textEdit_5.copy)
        QtCore.QObject.connect(self.checkBox_2, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.textEdit_2.copy)
        QtCore.QObject.connect(self.checkBox_4, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.textEdit_4.copy)
        QtCore.QObject.connect(self.checkBox_3, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.textEdit_3.copy)
        QtCore.QObject.connect(self.checkBox_6, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.textEdit_6.copy)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.pushButton.toggle)
        QtCore.QMetaObject.connectSlotsByName(Recommend_Dialog)

    def retranslateUi(self, Recommend_Dialog):
        Recommend_Dialog.setWindowTitle(_translate("Recommend_Dialog", "Dialog", None))
        self.pushButton.setText(_translate("Recommend_Dialog", "Suggest", None))
        self.textEdit_1.setHtml(_translate("Recommend_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Piboto\'; font-size:12pt; font-weight:200; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Ubuntu\'; font-size:11pt; font-weight:400;\"><br /></p></body></html>", None))
        self.tabLayout.setTabText(self.tabLayout.indexOf(self.ShoppingList), _translate("Recommend_Dialog", "ShoppingList", None))
        self.tabLayout.setTabText(self.tabLayout.indexOf(self.Recommender), _translate("Recommend_Dialog", "Recommender", None))

import new_qrc_resource_rc
import sameer_rc
