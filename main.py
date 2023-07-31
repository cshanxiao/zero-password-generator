# -*- coding: utf8 -*-
u"""
@summary:
@author: Zero
@date: 2016年2月18日
"""

import cgitb
import sys
import traceback

from PyQt6.QtWidgets import QApplication

from generator.control.main_dlg import MainDialog

# 开发过程中捕捉全部异常
cgitb.enable(format='text')


def main():
    try:
        app = QApplication(sys.argv)
        dlg = MainDialog()
        dlg.show()
        app.exec()
    except:
        traceback.print_exc()


if __name__ == '__main__':
    main()
