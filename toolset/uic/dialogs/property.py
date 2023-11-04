# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialogs\property.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(536, 318)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.propertyEdit = QtWidgets.QLineEdit(Dialog)
        self.propertyEdit.setEnabled(False)
        self.propertyEdit.setObjectName("propertyEdit")
        self.verticalLayout.addWidget(self.propertyEdit)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.subpropertyEdit = QtWidgets.QLineEdit(Dialog)
        self.subpropertyEdit.setEnabled(False)
        self.subpropertyEdit.setObjectName("subpropertyEdit")
        self.verticalLayout.addWidget(self.subpropertyEdit)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.costEdit = QtWidgets.QLineEdit(Dialog)
        self.costEdit.setEnabled(False)
        self.costEdit.setObjectName("costEdit")
        self.verticalLayout.addWidget(self.costEdit)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.parameterEdit = QtWidgets.QLineEdit(Dialog)
        self.parameterEdit.setEnabled(False)
        self.parameterEdit.setObjectName("parameterEdit")
        self.verticalLayout.addWidget(self.parameterEdit)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.upgradeSelect = QtWidgets.QComboBox(Dialog)
        self.upgradeSelect.setObjectName("upgradeSelect")
        self.verticalLayout.addWidget(self.upgradeSelect)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.costList = QtWidgets.QListWidget(Dialog)
        self.costList.setObjectName("costList")
        self.verticalLayout_2.addWidget(self.costList)
        self.costSelectButton = QtWidgets.QPushButton(Dialog)
        self.costSelectButton.setObjectName("costSelectButton")
        self.verticalLayout_2.addWidget(self.costSelectButton)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_3.addWidget(self.label_6)
        self.parameterList = QtWidgets.QListWidget(Dialog)
        self.parameterList.setObjectName("parameterList")
        self.verticalLayout_3.addWidget(self.parameterList)
        self.parameterSelectButton = QtWidgets.QPushButton(Dialog)
        self.parameterSelectButton.setObjectName("parameterSelectButton")
        self.verticalLayout_3.addWidget(self.parameterSelectButton)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.horizontalLayout.setStretch(0, 3)
        self.horizontalLayout.setStretch(1, 4)
        self.horizontalLayout.setStretch(2, 4)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_4.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept) # type: ignore
        self.buttonBox.rejected.connect(Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Item Property:"))
        self.label_2.setText(_translate("Dialog", "Item Sub-Property:"))
        self.label_3.setText(_translate("Dialog", "Item Cost Parameter:"))
        self.label_4.setText(_translate("Dialog", "Parameter 1:"))
        self.label_7.setText(_translate("Dialog", "Upgrade Type:"))
        self.label_5.setText(_translate("Dialog", "Cost Parameter Values:"))
        self.costSelectButton.setText(_translate("Dialog", "Select"))
        self.label_6.setText(_translate("Dialog", "Parameter Values:"))
        self.parameterSelectButton.setText(_translate("Dialog", "Select"))
