# -*- coding: utf8 -*-
u'''
@summary:
@author: Administrator
@date: 2016年2月18日
'''

from PyQt4 import QtGui
from generator.core.password_generator import PasswordGenerator
from generator.view.normal_wgt_ui import Ui_Normalwgt

class Normalwgt(QtGui.QDialog, Ui_Normalwgt):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        Ui_Normalwgt.__init__(self)
        self.setupUi(self)

        self.bind_events()

    def bind_events(self):
        self.btn_generate.clicked.connect(self.generate_pwds)

    def generate_pwds(self, event):
        digits = self.cb_digits.isChecked()
        lowercase = self.cb_lowercase.isChecked()
        uppercase = self.cb_uppercase.isChecked()
        punctuation = self.cb_punctuation.isChecked()

        length = self.sb_length.value()
        count = self.sb_count.value()

        genaretor = PasswordGenerator()
        pwds = genaretor.generate_normal_password(digits, lowercase, uppercase,
                                                  punctuation, length, count)

        self.text_pwd.clear()
        for pwd in pwds:
            self.text_pwd.appendPlainText(pwd)



