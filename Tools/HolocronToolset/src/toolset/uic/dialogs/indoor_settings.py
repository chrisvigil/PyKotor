# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialogs\indoor_settings.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from gui.widgets.edit.color import ColorEdit
from gui.widgets.edit.locstring import LocalizedStringLineEdit
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(285, 157)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.nameEdit = LocalizedStringLineEdit(Dialog)
        self.nameEdit.setMinimumSize(QtCore.QSize(0, 23))
        self.nameEdit.setObjectName("nameEdit")
        self.horizontalLayout_14.addWidget(self.nameEdit)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_14)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.colorEdit = ColorEdit(Dialog)
        self.colorEdit.setMinimumSize(QtCore.QSize(0, 23))
        self.colorEdit.setObjectName("colorEdit")
        self.horizontalLayout_13.addWidget(self.colorEdit)
        self.formLayout.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_13)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.warpCodeEdit = QtWidgets.QLineEdit(Dialog)
        self.warpCodeEdit.setMaxLength(6)
        self.warpCodeEdit.setObjectName("warpCodeEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.warpCodeEdit)
        self.skyboxSelect = QtWidgets.QComboBox(Dialog)
        self.skyboxSelect.setObjectName("skyboxSelect")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.skyboxSelect)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.verticalLayout.addLayout(self.formLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept) # type: ignore
        self.buttonBox.rejected.connect(Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Module Settings"))
        self.label.setText(_translate("Dialog", "Name:"))
        self.label_2.setText(_translate("Dialog", "Lighting:"))
        self.label_3.setText(_translate("Dialog", "Warp Code:"))
        self.label_4.setText(_translate("Dialog", "Skybox:"))