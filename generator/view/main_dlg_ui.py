# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\python_molynd\Passwordgenerator\generator\view\main_dlg.ui'
#
# Created: Thu Feb 18 12:09:03 2016
#      by: PyQt4 UI code generator 4.10
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

class Ui_Maindlg(object):
    def setupUi(self, Maindlg):
        Maindlg.setObjectName(_fromUtf8("Maindlg"))
        Maindlg.setWindowModality(QtCore.Qt.NonModal)
        Maindlg.resize(825, 565)

        self.retranslateUi(Maindlg)
        QtCore.QMetaObject.connectSlotsByName(Maindlg)

    def retranslateUi(self, Maindlg):
        Maindlg.setWindowTitle(_translate("Maindlg", "密码生成器", None))

