# -*- coding: utf-8 -*-
"""
Created on 2014-1-2

@author: Zero
"""
from pathlib import Path

from PyQt6 import QtCore, QtGui
from PyQt6.QtWidgets import QDialog, QTabWidget

from generator.control.normal_wgt import NormalWidget
from generator.view.main_dlg import Ui_Maindlg
from settings import RESOURCE_PATH, FRAME_WIDTH, FRAME_HEIGHT


class MainDialog(QDialog, Ui_Maindlg):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        Ui_Maindlg.__init__(self)
        self.setupUi(self)
        self.create_ui()

    def create_ui(self):
        self.resize(FRAME_WIDTH, FRAME_HEIGHT)
        self.setMaximumSize(QtCore.QSize(FRAME_WIDTH, FRAME_HEIGHT))
        self.setWindowFlags(QtCore.Qt.WindowType.Window)
        self.setWindowIcon(QtGui.QIcon(Path(RESOURCE_PATH).joinpath("tray.png").as_posix()))

        self.tabWidget = QTabWidget(self)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, FRAME_WIDTH, FRAME_HEIGHT))
        self.tabWidget.setTabPosition(QTabWidget.TabPosition.North)
        self.tabWidget.setIconSize(QtCore.QSize(32, 32))
        self.show_tabs()
        self.tabWidget.setCurrentIndex(0)

    def show_tabs(self):
        """
        @summary:
        """
        tab_normal = NormalWidget(self)
        tab_normal.setObjectName("tab_normal")
        icon = QtGui.QIcon(Path(RESOURCE_PATH).joinpath("ssh.png").as_posix())
        self.tabWidget.addTab(tab_normal, icon, u"普通密码生成")
