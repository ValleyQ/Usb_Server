#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from future_builtins import *

import sys

from PyQt4.QtCore import Qt, SIGNAL
from PyQt4.QtGui  import QApplication, QComboBox, QDialog
from PyQt4.QtGui  import QDoubleSpinBox, QGridLayout, QLabel
import usbserver_ui

class UsbBox(QDialog, usbserver_ui.Ui_Dialog):
    def __init__(self, parent=None):
        super(UsbBox, self).__init__(parent)

        self.setupUi(self)

if __name__ == "__main__":
    app=QApplication(sys.argv)
    form=UsbBox()
    form.show()
    app.exec_()
