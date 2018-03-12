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
        Recommend_Dialog.resize(602, 419)
        Recommend_Dialog.setStyleSheet(_fromUtf8("QDialog {background-image: url(:/newPrefix/fandv.jpg);}"))
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
        self.ShoppingList_VolControl = QtGui.QSlider(self.ShoppingList)
        self.ShoppingList_VolControl.setGeometry(QtCore.QRect(440, 10, 131, 21))
        self.ShoppingList_VolControl.setOrientation(QtCore.Qt.Horizontal)
        self.ShoppingList_VolControl.setObjectName(_fromUtf8("ShoppingList_VolControl"))
        self.gridLayoutWidget = QtGui.QWidget(self.ShoppingList)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 50, 551, 500))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.textEdit_2 = QtGui.QTextEdit(self.gridLayoutWidget)
        self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))
        self.gridLayout.addWidget(self.textEdit_2, 1, 1, 1, 1)
        self.checkBox_2 = QtGui.QCheckBox(self.gridLayoutWidget)
        self.checkBox_2.setText(_fromUtf8(""))
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.gridLayout.addWidget(self.checkBox_2, 1, 0, 1, 1)
        self.textEdit_1 = QtGui.QTextEdit(self.gridLayoutWidget)
        self.textEdit_1.setObjectName(_fromUtf8("textEdit_1"))
        self.gridLayout.addWidget(self.textEdit_1, 0, 1, 1, 1)
        self.checkBox_4 = QtGui.QCheckBox(self.gridLayoutWidget)
        self.checkBox_4.setText(_fromUtf8(""))
        self.checkBox_4.setObjectName(_fromUtf8("checkBox_4"))
        self.gridLayout.addWidget(self.checkBox_4, 4, 0, 1, 1)
        self.checkBox_1 = QtGui.QCheckBox(self.gridLayoutWidget)
        self.checkBox_1.setText(_fromUtf8(""))
        self.checkBox_1.setObjectName(_fromUtf8("checkBox_1"))
        self.gridLayout.addWidget(self.checkBox_1, 0, 0, 1, 1)
        self.checkBox_3 = QtGui.QCheckBox(self.gridLayoutWidget)
        self.checkBox_3.setText(_fromUtf8(""))
        self.checkBox_3.setObjectName(_fromUtf8("checkBox_3"))
        self.gridLayout.addWidget(self.checkBox_3, 2, 0, 1, 1)
        self.checkBox_5 = QtGui.QCheckBox(self.gridLayoutWidget)
        self.checkBox_5.setText(_fromUtf8(""))
        self.checkBox_5.setObjectName(_fromUtf8("checkBox_5"))
        self.gridLayout.addWidget(self.checkBox_5, 5, 0, 1, 1)
        self.textEdit_3 = QtGui.QTextEdit(self.gridLayoutWidget)
        self.textEdit_3.setObjectName(_fromUtf8("textEdit_3"))
        self.gridLayout.addWidget(self.textEdit_3, 2, 1, 1, 1)
        self.textEdit_4 = QtGui.QTextEdit(self.gridLayoutWidget)
        self.textEdit_4.setObjectName(_fromUtf8("textEdit_4"))
        self.gridLayout.addWidget(self.textEdit_4, 4, 1, 1, 1)
        self.textEdit_5 = QtGui.QTextEdit(self.gridLayoutWidget)
        self.textEdit_5.setObjectName(_fromUtf8("textEdit_5"))
        self.gridLayout.addWidget(self.textEdit_5, 5, 1, 1, 1)
        self.checkBox_6 = QtGui.QCheckBox(self.gridLayoutWidget)
        self.checkBox_6.setText(_fromUtf8(""))
        self.checkBox_6.setObjectName(_fromUtf8("checkBox_6"))
        self.gridLayout.addWidget(self.checkBox_6, 6, 0, 1, 1)
        self.textEdit_6 = QtGui.QTextEdit(self.gridLayoutWidget)
        self.textEdit_6.setObjectName(_fromUtf8("textEdit_6"))
        self.gridLayout.addWidget(self.textEdit_6, 6, 1, 1, 1)
        self.pushButton = QtGui.QPushButton(self.ShoppingList)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 111, 27))
        self.pushButton.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
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
        self.Recommender_VolControl = QtGui.QSlider(self.scrollAreaWidgetContents)
        self.Recommender_VolControl.setGeometry(QtCore.QRect(440, 20, 131, 21))
        self.Recommender_VolControl.setOrientation(QtCore.Qt.Horizontal)
        self.Recommender_VolControl.setObjectName(_fromUtf8("Recommender_VolControl"))
        self.label = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label.setGeometry(QtCore.QRect(20, 40, 70, 80))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setGeometry(QtCore.QRect(120, 40, 70, 80))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_3.setGeometry(QtCore.QRect(100, 65, 16, 27))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_4.setGeometry(QtCore.QRect(20, 130, 70, 70))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_5.setGeometry(QtCore.QRect(100, 130, 70, 70))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_6.setGeometry(QtCore.QRect(20, 220, 70, 70))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_7.setGeometry(QtCore.QRect(100, 220, 70, 70))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_8.setGeometry(QtCore.QRect(334, 130, 70, 70))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_9.setGeometry(QtCore.QRect(414, 130, 70, 70))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.tabLayout.addTab(self.Recommender, _fromUtf8(""))

        self.retranslateUi(Recommend_Dialog)
        self.tabLayout.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Recommend_Dialog)

    def retranslateUi(self, Recommend_Dialog):
        Recommend_Dialog.setWindowTitle(_translate("Recommend_Dialog", "Dialog", None))
        self.textEdit_1.setHtml(_translate("Recommend_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.pushButton.setText(_translate("Recommend_Dialog", "ActiveSuggest", None))
        self.tabLayout.setTabText(self.tabLayout.indexOf(self.ShoppingList), _translate("Recommend_Dialog", "ShoppingList", None))
        self.label.setText(_translate("Recommend_Dialog", "TextLabel", None))
        self.label_2.setText(_translate("Recommend_Dialog", "TextLabel", None))
        self.label_3.setText(_translate("Recommend_Dialog", "+", None))
        self.label_4.setText(_translate("Recommend_Dialog", "TextLabel", None))
        self.label_5.setText(_translate("Recommend_Dialog", "TextLabel", None))
        self.label_6.setText(_translate("Recommend_Dialog", "TextLabel", None))
        self.label_7.setText(_translate("Recommend_Dialog", "TextLabel", None))
        self.label_8.setText(_translate("Recommend_Dialog", "TextLabel", None))
        self.label_9.setText(_translate("Recommend_Dialog", "TextLabel", None))
        self.tabLayout.setTabText(self.tabLayout.indexOf(self.Recommender), _translate("Recommend_Dialog", "Recommender", None))

import sameer_rc
