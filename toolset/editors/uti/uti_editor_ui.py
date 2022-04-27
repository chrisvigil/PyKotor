# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editors\uti\uti_editor.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(550, 308)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.tab)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.nameEdit = QtWidgets.QLineEdit(self.tab)
        self.nameEdit.setReadOnly(True)
        self.nameEdit.setObjectName("nameEdit")
        self.horizontalLayout_18.addWidget(self.nameEdit)
        self.nameChangeButton = QtWidgets.QPushButton(self.tab)
        self.nameChangeButton.setMaximumSize(QtCore.QSize(26, 16777215))
        self.nameChangeButton.setObjectName("nameChangeButton")
        self.horizontalLayout_18.addWidget(self.nameChangeButton)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_18)
        self.label_14 = QtWidgets.QLabel(self.tab)
        self.label_14.setObjectName("label_14")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_14)
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.tagEdit = QtWidgets.QLineEdit(self.tab)
        self.tagEdit.setObjectName("tagEdit")
        self.horizontalLayout_19.addWidget(self.tagEdit)
        self.tagGenerateButton = QtWidgets.QPushButton(self.tab)
        self.tagGenerateButton.setMaximumSize(QtCore.QSize(26, 16777215))
        self.tagGenerateButton.setObjectName("tagGenerateButton")
        self.horizontalLayout_19.addWidget(self.tagGenerateButton)
        self.formLayout.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_19)
        self.label_38 = QtWidgets.QLabel(self.tab)
        self.label_38.setObjectName("label_38")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_38)
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.resrefEdit = QtWidgets.QLineEdit(self.tab)
        self.resrefEdit.setMaxLength(16)
        self.resrefEdit.setObjectName("resrefEdit")
        self.horizontalLayout_20.addWidget(self.resrefEdit)
        self.resrefGenerateButton = QtWidgets.QPushButton(self.tab)
        self.resrefGenerateButton.setMaximumSize(QtCore.QSize(26, 16777215))
        self.resrefGenerateButton.setObjectName("resrefGenerateButton")
        self.horizontalLayout_20.addWidget(self.resrefGenerateButton)
        self.formLayout.setLayout(2, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_20)
        self.label_39 = QtWidgets.QLabel(self.tab)
        self.label_39.setObjectName("label_39")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_39)
        self.baseSelect = ComboBox2DA(self.tab)
        self.baseSelect.setObjectName("baseSelect")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.baseSelect)
        self.label_40 = QtWidgets.QLabel(self.tab)
        self.label_40.setObjectName("label_40")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_40)
        self.label_41 = QtWidgets.QLabel(self.tab)
        self.label_41.setObjectName("label_41")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_41)
        self.label_42 = QtWidgets.QLabel(self.tab)
        self.label_42.setObjectName("label_42")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_42)
        self.costSpin = QtWidgets.QSpinBox(self.tab)
        self.costSpin.setMaximum(1000000)
        self.costSpin.setObjectName("costSpin")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.costSpin)
        self.additionalCostSpin = QtWidgets.QSpinBox(self.tab)
        self.additionalCostSpin.setMaximum(1000000)
        self.additionalCostSpin.setObjectName("additionalCostSpin")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.additionalCostSpin)
        self.label_53 = QtWidgets.QLabel(self.tab)
        self.label_53.setObjectName("label_53")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_53)
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.descEdit = LocalizedStringLineEdit(self.tab)
        self.descEdit.setMinimumSize(QtCore.QSize(0, 23))
        self.descEdit.setObjectName("descEdit")
        self.horizontalLayout_21.addWidget(self.descEdit)
        self.formLayout.setLayout(3, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_21)
        self.upgradeSpin = QtWidgets.QSpinBox(self.tab)
        self.upgradeSpin.setMaximum(255)
        self.upgradeSpin.setObjectName("upgradeSpin")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.upgradeSpin)
        self.horizontalLayout.addLayout(self.formLayout)
        spacerItem = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.plotCheckbox = QtWidgets.QCheckBox(self.tab)
        self.plotCheckbox.setObjectName("plotCheckbox")
        self.verticalLayout.addWidget(self.plotCheckbox)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_43 = QtWidgets.QLabel(self.tab)
        self.label_43.setObjectName("label_43")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_43)
        self.chargesSpin = QtWidgets.QSpinBox(self.tab)
        self.chargesSpin.setMaximum(255)
        self.chargesSpin.setObjectName("chargesSpin")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.chargesSpin)
        self.label_44 = QtWidgets.QLabel(self.tab)
        self.label_44.setObjectName("label_44")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_44)
        self.label_45 = QtWidgets.QLabel(self.tab)
        self.label_45.setObjectName("label_45")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_45)
        self.label_46 = QtWidgets.QLabel(self.tab)
        self.label_46.setObjectName("label_46")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_46)
        self.label_47 = QtWidgets.QLabel(self.tab)
        self.label_47.setObjectName("label_47")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_47)
        self.stackSpin = QtWidgets.QSpinBox(self.tab)
        self.stackSpin.setMaximum(65535)
        self.stackSpin.setObjectName("stackSpin")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.stackSpin)
        self.modelVarSpin = QtWidgets.QSpinBox(self.tab)
        self.modelVarSpin.setMaximum(255)
        self.modelVarSpin.setObjectName("modelVarSpin")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.modelVarSpin)
        self.bodyVarSpin = QtWidgets.QSpinBox(self.tab)
        self.bodyVarSpin.setMaximum(255)
        self.bodyVarSpin.setObjectName("bodyVarSpin")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.bodyVarSpin)
        self.textureVarSpin = QtWidgets.QSpinBox(self.tab)
        self.textureVarSpin.setMaximum(255)
        self.textureVarSpin.setObjectName("textureVarSpin")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.textureVarSpin)
        self.verticalLayout.addLayout(self.formLayout_2)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.horizontalLayout.setStretch(0, 6)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 5)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.tab_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.tab_2)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.availablePropertyList = QtWidgets.QTreeWidget(self.tab_2)
        self.availablePropertyList.setObjectName("availablePropertyList")
        self.availablePropertyList.headerItem().setText(0, "1")
        self.availablePropertyList.header().setVisible(False)
        self.verticalLayout_3.addWidget(self.availablePropertyList)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.addPropertyButton = QtWidgets.QPushButton(self.tab_2)
        self.addPropertyButton.setMaximumSize(QtCore.QSize(20, 16777215))
        self.addPropertyButton.setObjectName("addPropertyButton")
        self.verticalLayout_2.addWidget(self.addPropertyButton)
        self.removePropertyButton = QtWidgets.QPushButton(self.tab_2)
        self.removePropertyButton.setMaximumSize(QtCore.QSize(20, 16777215))
        self.removePropertyButton.setObjectName("removePropertyButton")
        self.verticalLayout_2.addWidget(self.removePropertyButton)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        self.assignedPropertiesList = QtWidgets.QListWidget(self.tab_2)
        self.assignedPropertiesList.setObjectName("assignedPropertiesList")
        self.verticalLayout_4.addWidget(self.assignedPropertiesList)
        self.editPropertyButton = QtWidgets.QPushButton(self.tab_2)
        self.editPropertyButton.setObjectName("editPropertyButton")
        self.verticalLayout_4.addWidget(self.editPropertyButton)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.commentsEdit = QtWidgets.QPlainTextEdit(self.tab_3)
        self.commentsEdit.setObjectName("commentsEdit")
        self.gridLayout_2.addWidget(self.commentsEdit, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 550, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSaveAs = QtWidgets.QAction(MainWindow)
        self.actionSaveAs.setObjectName("actionSaveAs")
        self.actionRevert = QtWidgets.QAction(MainWindow)
        self.actionRevert.setObjectName("actionRevert")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSaveAs)
        self.menuFile.addAction(self.actionRevert)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_6.setText(_translate("MainWindow", "Name:"))
        self.nameChangeButton.setText(_translate("MainWindow", "..."))
        self.label_14.setText(_translate("MainWindow", "Tag:"))
        self.tagGenerateButton.setText(_translate("MainWindow", "-"))
        self.label_38.setText(_translate("MainWindow", "ResRef:"))
        self.resrefGenerateButton.setText(_translate("MainWindow", "-"))
        self.label_39.setText(_translate("MainWindow", "Base Item:"))
        self.label_40.setText(_translate("MainWindow", "Cost:"))
        self.label_41.setText(_translate("MainWindow", "Additional Cost:"))
        self.label_42.setText(_translate("MainWindow", "Upgrade Level:"))
        self.label_53.setText(_translate("MainWindow", "Description:"))
        self.plotCheckbox.setText(_translate("MainWindow", "Plot"))
        self.label_43.setText(_translate("MainWindow", "Charges:"))
        self.label_44.setText(_translate("MainWindow", "Stack Size:"))
        self.label_45.setText(_translate("MainWindow", "Model Variation:"))
        self.label_46.setText(_translate("MainWindow", "Body Variation:"))
        self.label_47.setText(_translate("MainWindow", "Texture Variation:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "General"))
        self.label.setText(_translate("MainWindow", "Available Properties"))
        self.addPropertyButton.setText(_translate("MainWindow", "->"))
        self.removePropertyButton.setText(_translate("MainWindow", "<-"))
        self.label_2.setText(_translate("MainWindow", "Assigned Properties"))
        self.editPropertyButton.setText(_translate("MainWindow", "Edit Property"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Properties"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Comments"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSaveAs.setText(_translate("MainWindow", "Save As"))
        self.actionRevert.setText(_translate("MainWindow", "Revert"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
from toolset.misc.widget.widgets import ComboBox2DA, LocalizedStringLineEdit
