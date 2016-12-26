# -*- coding: utf8 -*-
u'''
@summary:
@author: Administrator
@date: 2016年2月18日
'''
import sys

from PyQt4 import QtGui
from PyQt4.QtGui import QFontDatabase, QFont

from generator.control.main_dlg import Maindlg


def main():
    app = QtGui.QApplication(sys.argv)
    
    # 设置字体
    loadedFontID = QFontDatabase.addApplicationFont(
        "./resource/fonts/SourceCodePro-LightIt.ttf")
    loadedFontFamilies = QFontDatabase.applicationFontFamilies(loadedFontID)
    fontName = loadedFontFamilies[0]
    font  = QFont(fontName, 12)
    app.setFont(font)
    
    mdlg = Maindlg()
    mdlg.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf8')
    main()


