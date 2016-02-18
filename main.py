# -*- coding: utf8 -*-
u'''
@summary:
@author: Administrator
@date: 2016年2月18日
'''
import sys
from PyQt4 import QtGui
from generator.control.main_dlg import Maindlg

def main():
    app = QtGui.QApplication(sys.argv)
    mdlg = Maindlg()
    mdlg.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf8')
    main()


