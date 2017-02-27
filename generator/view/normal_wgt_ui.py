# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\python\Passwordgenerator\generator\view\normal_wgt.ui'
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

class Ui_Normalwgt(object):
    def setupUi(self, Normalwgt):
        Normalwgt.setObjectName(_fromUtf8("Normalwgt"))
        Normalwgt.resize(918, 534)
        self.label = QtGui.QLabel(Normalwgt)
        self.label.setGeometry(QtCore.QRect(270, 10, 71, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Source Code Pro ExtraLight"))
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.sb_length = QtGui.QSpinBox(Normalwgt)
        self.sb_length.setGeometry(QtCore.QRect(340, 10, 101, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Source Code Pro ExtraLight"))
        font.setPointSize(12)
        self.sb_length.setFont(font)
        self.sb_length.setMinimum(1)
        self.sb_length.setProperty("value", 8)
        self.sb_length.setObjectName(_fromUtf8("sb_length"))
        self.groupBox = QtGui.QGroupBox(Normalwgt)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 231, 121))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Source Code Pro ExtraLight"))
        font.setPointSize(12)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.cb_digits = QtGui.QCheckBox(self.groupBox)
        self.cb_digits.setGeometry(QtCore.QRect(10, 20, 100, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Source Code Pro ExtraLight"))
        font.setPointSize(12)
        self.cb_digits.setFont(font)
        self.cb_digits.setObjectName(_fromUtf8("cb_digits"))
        self.cb_lowercase = QtGui.QCheckBox(self.groupBox)
        self.cb_lowercase.setGeometry(QtCore.QRect(10, 40, 120, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Source Code Pro ExtraLight"))
        font.setPointSize(12)
        self.cb_lowercase.setFont(font)
        self.cb_lowercase.setObjectName(_fromUtf8("cb_lowercase"))
        self.cb_uppercase = QtGui.QCheckBox(self.groupBox)
        self.cb_uppercase.setGeometry(QtCore.QRect(10, 60, 120, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Source Code Pro ExtraLight"))
        font.setPointSize(12)
        self.cb_uppercase.setFont(font)
        self.cb_uppercase.setObjectName(_fromUtf8("cb_uppercase"))
        self.cb_punctuation = QtGui.QCheckBox(self.groupBox)
        self.cb_punctuation.setGeometry(QtCore.QRect(10, 80, 120, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Source Code Pro ExtraLight"))
        font.setPointSize(12)
        self.cb_punctuation.setFont(font)
        self.cb_punctuation.setObjectName(_fromUtf8("cb_punctuation"))
        self.label_2 = QtGui.QLabel(Normalwgt)
        self.label_2.setGeometry(QtCore.QRect(270, 50, 71, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Source Code Pro ExtraLight"))
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.sb_count = QtGui.QSpinBox(Normalwgt)
        self.sb_count.setGeometry(QtCore.QRect(340, 50, 101, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Source Code Pro ExtraLight"))
        font.setPointSize(12)
        self.sb_count.setFont(font)
        self.sb_count.setMinimum(1)
        self.sb_count.setObjectName(_fromUtf8("sb_count"))
        self.text_pwd = QtGui.QPlainTextEdit(Normalwgt)
        self.text_pwd.setGeometry(QtCore.QRect(20, 140, 871, 371))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Source Code Pro ExtraLight"))
        font.setPointSize(12)
        self.text_pwd.setFont(font)
        self.text_pwd.setObjectName(_fromUtf8("text_pwd"))
        self.btn_generate = QtGui.QPushButton(Normalwgt)
        self.btn_generate.setGeometry(QtCore.QRect(270, 90, 171, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Source Code Pro ExtraLight"))
        font.setPointSize(12)
        self.btn_generate.setFont(font)
        self.btn_generate.setObjectName(_fromUtf8("btn_generate"))

        self.retranslateUi(Normalwgt)
        QtCore.QMetaObject.connectSlotsByName(Normalwgt)

    def retranslateUi(self, Normalwgt):
        Normalwgt.setWindowTitle(_translate("Normalwgt", "Form", None))
        self.label.setText(_translate("Normalwgt", "密码长度", None))
        self.groupBox.setTitle(_translate("Normalwgt", "密码规则", None))
        self.cb_digits.setText(_translate("Normalwgt", "包含数字", None))
        self.cb_lowercase.setText(_translate("Normalwgt", "包含小写字母", None))
        self.cb_uppercase.setText(_translate("Normalwgt", "包含大写字母", None))
        self.cb_punctuation.setText(_translate("Normalwgt", "包含特殊字符", None))
        self.label_2.setText(_translate("Normalwgt", "生成数量", None))
        self.btn_generate.setText(_translate("Normalwgt", "生成密码", None))

