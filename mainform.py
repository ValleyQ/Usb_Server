# -*- coding: utf-8 -*-

"""
Module implementing mainWindow.
"""
import os
import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *

import mainform_ui
import usbserver

class MainWindow(QMainWindow, mainform_ui.Ui_MainWindow):
    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)

        self.setupUi(self)
        self.setupMenu()

    def setupMenu(self):
        # UsbBox
        self.connect(self.actionSetting, SIGNAL("triggered()"),
                    self.showUsbBox)

    def showUsbBox(self):
        dlg = usbserver.UsbBox(self)
        dlg.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainForm = MainWindow()
    mainForm.show()
    sys.exit(app.exec_())
