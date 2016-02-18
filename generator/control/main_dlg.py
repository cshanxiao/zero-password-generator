#-*- coding: utf-8 -*-
'''
Created on 2014-1-2

@author: Administrator
'''
from PyQt4 import QtCore, QtGui
from generator.common.global_cnf import FRAME_WIDTH, FRAME_HEIGHT
from generator.view.main_dlg_ui import Ui_Maindlg
from generator.control.normal_wgt import Normalwgt

class Maindlg(QtGui.QDialog, Ui_Maindlg):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        Ui_Maindlg.__init__(self)
        self.setupUi(self)
        self.create_ui()

    def create_ui(self):
        self.resize(FRAME_WIDTH, FRAME_HEIGHT)
        self.setMaximumSize(QtCore.QSize(FRAME_WIDTH, FRAME_HEIGHT))
        self.setWindowFlags(QtCore.Qt.Window)
        self.setWindowIcon(QtGui.QIcon("./skin/tray.png"))

        self.tabWidget = QtGui.QTabWidget(self)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, FRAME_WIDTH, FRAME_HEIGHT))
        self.tabWidget.setTabPosition(QtGui.QTabWidget.North)
        self.tabWidget.setIconSize(QtCore.QSize(32, 32))
        self.show_tabs()
        self.tabWidget.setCurrentIndex(0)

    def show_tabs(self):
        u'''
        @summary:
        '''
        tab_normal = Normalwgt(self)
        tab_normal.setObjectName("tab_normal")
        icon = QtGui.QIcon("./skin/ssh.png")
        self.tabWidget.addTab(tab_normal, icon, u"普通密码生成")






