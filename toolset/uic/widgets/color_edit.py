# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widgets\color_edit.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(235, 23)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.colorLabel = QtWidgets.QLabel(Form)
        self.colorLabel.setMinimumSize(QtCore.QSize(16, 16))
        self.colorLabel.setMaximumSize(QtCore.QSize(16, 16))
        self.colorLabel.setStyleSheet("background: black;")
        self.colorLabel.setText("")
        self.colorLabel.setObjectName("colorLabel")
        self.horizontalLayout.addWidget(self.colorLabel)
        self.colorSpin = LongSpinBox(Form)
        self.colorSpin.setObjectName("colorSpin")
        self.horizontalLayout.addWidget(self.colorSpin)
        self.editButton = QtWidgets.QPushButton(Form)
        self.editButton.setMaximumSize(QtCore.QSize(26, 23))
        self.editButton.setObjectName("editButton")
        self.horizontalLayout.addWidget(self.editButton)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.editButton.setText(_translate("Form", "..."))
from toolset.gui.widgets.long_spinbox import LongSpinBox
