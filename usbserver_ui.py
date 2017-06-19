# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'usbserver.ui'
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(648, 397)
        self.Ok_Cancel = QtGui.QDialogButtonBox(Dialog)
        self.Ok_Cancel.setGeometry(QtCore.QRect(440, 280, 156, 40))
        self.Ok_Cancel.setOrientation(QtCore.Qt.Horizontal)
        self.Ok_Cancel.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.Ok_Cancel.setObjectName(_fromUtf8("Ok_Cancel"))
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(170, 10, 441, 271))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Courier New"))
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.IPaddr = QtGui.QLineEdit(self.groupBox)
        self.IPaddr.setObjectName(_fromUtf8("IPaddr"))
        self.verticalLayout.addWidget(self.IPaddr)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.TCPport = QtGui.QSpinBox(self.groupBox)
        self.TCPport.setMaximum(65535)
        self.TCPport.setObjectName(_fromUtf8("TCPport"))
        self.horizontalLayout.addWidget(self.TCPport)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.groupBox_3 = QtGui.QGroupBox(self.groupBox)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox_3)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_3 = QtGui.QLabel(self.groupBox_3)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox_3)
        self.AutoConnect = QtGui.QCheckBox(self.groupBox)
        self.AutoConnect.setObjectName(_fromUtf8("AutoConnect"))
        self.verticalLayout_2.addWidget(self.AutoConnect)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.gridLayout_2.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.groupBox_2 = QtGui.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 20, 151, 261))
        self.groupBox_2.setTitle(_fromUtf8(""))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.label_4 = QtGui.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(20, 200, 120, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Courier New"))
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(10, 30, 131, 141))
        self.label_5.setAutoFillBackground(False)
        self.label_5.setText(_fromUtf8(""))
        self.label_5.setPixmap(QtGui.QPixmap(_fromUtf8("Res/global.png")))
        self.label_5.setWordWrap(False)
        self.label_5.setObjectName(_fromUtf8("label_5"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.Ok_Cancel, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.Ok_Cancel, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.groupBox.setTitle(_translate("Dialog", "Connection Parameters", None))
        self.label_2.setText(_translate("Dialog", "Please type IP address or host name of the remote \n"
"computer where your shared USB device is plugged in:", None))
        self.label.setText(_translate("Dialog", "Select TCP Port", None))
        self.TCPport.setPrefix(_translate("Dialog", "324", None))
        self.groupBox_3.setTitle(_translate("Dialog", "Attention", None))
        self.label_3.setText(_translate("Dialog", "You should select the same TCP port as used on \n"
"remote side for incoming connections", None))
        self.AutoConnect.setText(_translate("Dialog", " Auto-Connect all USB devices from the remote \n"
" computer when they become available.", None))
        self.label_4.setText(_translate("Dialog", "Direct Connect to \n"
"remote USB server", None))

import Res_rc

"""
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
"""
