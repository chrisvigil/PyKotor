# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editors\git.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(838, 648)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.filterEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.filterEdit.setText("")
        self.filterEdit.setMaxLength(16)
        self.filterEdit.setObjectName("filterEdit")
        self.verticalLayout.addWidget(self.filterEdit)
        self.listWidget = QtWidgets.QListWidget(self.layoutWidget)
        self.listWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.listWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.layoutWidget1 = QtWidgets.QWidget(self.splitter)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.lockInstancesCheck = QtWidgets.QCheckBox(self.layoutWidget1)
        self.lockInstancesCheck.setMaximumSize(QtCore.QSize(28, 16777215))
        self.lockInstancesCheck.setStyleSheet("QCheckbox {\n"
"    spacing: 0px;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    image: url(:/images/icons/lock.png);\n"
"    border: 1px solid rgba(30, 144, 255, 0.0);\n"
"    width: 26px;\n"
"    height: 26px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover {\n"
"    background: rgba(30, 144, 255, 0.2);\n"
"    border: 1px solid rgba(30, 144, 255, 0.4);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background: rgba(30, 144, 255, 0.4);\n"
"    border:1px solid rgba(30, 144, 255, 0.6);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover {\n"
"    background: rgba(30, 144, 255, 0.5);\n"
"    border:1px solid rgba(30, 144, 255, 0.7);\n"
"}\n"
"\n"
"")
        self.lockInstancesCheck.setText("")
        self.lockInstancesCheck.setChecked(False)
        self.lockInstancesCheck.setObjectName("lockInstancesCheck")
        self.horizontalLayout_2.addWidget(self.lockInstancesCheck)
        self.label = QtWidgets.QLabel(self.layoutWidget1)
        self.label.setMaximumSize(QtCore.QSize(16777215, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.viewCreatureCheck = QtWidgets.QCheckBox(self.layoutWidget1)
        self.viewCreatureCheck.setMaximumSize(QtCore.QSize(28, 16777215))
        self.viewCreatureCheck.setStyleSheet("QCheckbox {\n"
"    spacing: 0px;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    image: url(:/images/icons/k1/creature.png);\n"
"    border: 1px solid rgba(30, 144, 255, 0.0);\n"
"    width: 26px;\n"
"    height: 26px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover {\n"
"    background: rgba(30, 144, 255, 0.2);\n"
"    border: 1px solid rgba(30, 144, 255, 0.4);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background: rgba(30, 144, 255, 0.4);\n"
"    border:1px solid rgba(30, 144, 255, 0.6);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover {\n"
"    background: rgba(30, 144, 255, 0.5);\n"
"    border:1px solid rgba(30, 144, 255, 0.7);\n"
"}\n"
"\n"
"")
        self.viewCreatureCheck.setText("")
        self.viewCreatureCheck.setChecked(True)
        self.viewCreatureCheck.setObjectName("viewCreatureCheck")
        self.horizontalLayout_2.addWidget(self.viewCreatureCheck)
        self.viewDoorCheck = QtWidgets.QCheckBox(self.layoutWidget1)
        self.viewDoorCheck.setMaximumSize(QtCore.QSize(28, 16777215))
        self.viewDoorCheck.setStyleSheet("QCheckBox::indicator {\n"
"    image: url(:/images/icons/k1/door.png);\n"
"    border: 1px solid rgba(30, 144, 255, 0.0);\n"
"    width: 26px;\n"
"    height: 26px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover {\n"
"    background: rgba(30, 144, 255, 0.2);\n"
"    border: 1px solid rgba(30, 144, 255, 0.4);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background: rgba(30, 144, 255, 0.4);\n"
"    border:1px solid rgba(30, 144, 255, 0.6);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover {\n"
"    background: rgba(30, 144, 255, 0.5);\n"
"    border:1px solid rgba(30, 144, 255, 0.7);\n"
"}\n"
"\n"
"")
        self.viewDoorCheck.setText("")
        self.viewDoorCheck.setChecked(True)
        self.viewDoorCheck.setObjectName("viewDoorCheck")
        self.horizontalLayout_2.addWidget(self.viewDoorCheck)
        self.viewPlaceableCheck = QtWidgets.QCheckBox(self.layoutWidget1)
        self.viewPlaceableCheck.setMaximumSize(QtCore.QSize(28, 16777215))
        self.viewPlaceableCheck.setStyleSheet("QCheckBox::indicator {\n"
"    image: url(:/images/icons/k1/placeable.png);\n"
"    border: 1px solid rgba(30, 144, 255, 0.0);\n"
"    width: 26px;\n"
"    height: 26px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover {\n"
"    background: rgba(30, 144, 255, 0.2);\n"
"    border: 1px solid rgba(30, 144, 255, 0.4);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background: rgba(30, 144, 255, 0.4);\n"
"    border:1px solid rgba(30, 144, 255, 0.6);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover {\n"
"    background: rgba(30, 144, 255, 0.5);\n"
"    border:1px solid rgba(30, 144, 255, 0.7);\n"
"}\n"
"\n"
"")
        self.viewPlaceableCheck.setText("")
        self.viewPlaceableCheck.setChecked(True)
        self.viewPlaceableCheck.setObjectName("viewPlaceableCheck")
        self.horizontalLayout_2.addWidget(self.viewPlaceableCheck)
        self.viewStoreCheck = QtWidgets.QCheckBox(self.layoutWidget1)
        self.viewStoreCheck.setMaximumSize(QtCore.QSize(28, 16777215))
        self.viewStoreCheck.setStyleSheet("QCheckBox::indicator {\n"
"    image: url(:/images/icons/k1/merchant.png);\n"
"    border: 1px solid rgba(30, 144, 255, 0.0);\n"
"    width: 26px;\n"
"    height: 26px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover {\n"
"    background: rgba(30, 144, 255, 0.2);\n"
"    border: 1px solid rgba(30, 144, 255, 0.4);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background: rgba(30, 144, 255, 0.4);\n"
"    border:1px solid rgba(30, 144, 255, 0.6);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover {\n"
"    background: rgba(30, 144, 255, 0.5);\n"
"    border:1px solid rgba(30, 144, 255, 0.7);\n"
"}\n"
"\n"
"")
        self.viewStoreCheck.setText("")
        self.viewStoreCheck.setChecked(True)
        self.viewStoreCheck.setObjectName("viewStoreCheck")
        self.horizontalLayout_2.addWidget(self.viewStoreCheck)
        self.viewSoundCheck = QtWidgets.QCheckBox(self.layoutWidget1)
        self.viewSoundCheck.setMaximumSize(QtCore.QSize(28, 16777215))
        self.viewSoundCheck.setStyleSheet("QCheckBox::indicator {\n"
"    image: url(:/images/icons/k1/sound.png);\n"
"    border: 1px solid rgba(30, 144, 255, 0.0);\n"
"    width: 26px;\n"
"    height: 26px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover {\n"
"    background: rgba(30, 144, 255, 0.2);\n"
"    border: 1px solid rgba(30, 144, 255, 0.4);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background: rgba(30, 144, 255, 0.4);\n"
"    border:1px solid rgba(30, 144, 255, 0.6);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover {\n"
"    background: rgba(30, 144, 255, 0.5);\n"
"    border:1px solid rgba(30, 144, 255, 0.7);\n"
"}\n"
"\n"
"")
        self.viewSoundCheck.setText("")
        self.viewSoundCheck.setChecked(True)
        self.viewSoundCheck.setObjectName("viewSoundCheck")
        self.horizontalLayout_2.addWidget(self.viewSoundCheck)
        self.viewWaypointCheck = QtWidgets.QCheckBox(self.layoutWidget1)
        self.viewWaypointCheck.setMaximumSize(QtCore.QSize(28, 16777215))
        self.viewWaypointCheck.setStyleSheet("QCheckBox::indicator {\n"
"    image: url(:/images/icons/k1/waypoint.png);\n"
"    border: 1px solid rgba(30, 144, 255, 0.0);\n"
"    width: 26px;\n"
"    height: 26px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover {\n"
"    background: rgba(30, 144, 255, 0.2);\n"
"    border: 1px solid rgba(30, 144, 255, 0.4);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background: rgba(30, 144, 255, 0.4);\n"
"    border:1px solid rgba(30, 144, 255, 0.6);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover {\n"
"    background: rgba(30, 144, 255, 0.5);\n"
"    border:1px solid rgba(30, 144, 255, 0.7);\n"
"}\n"
"\n"
"")
        self.viewWaypointCheck.setText("")
        self.viewWaypointCheck.setChecked(True)
        self.viewWaypointCheck.setObjectName("viewWaypointCheck")
        self.horizontalLayout_2.addWidget(self.viewWaypointCheck)
        self.viewCameraCheck = QtWidgets.QCheckBox(self.layoutWidget1)
        self.viewCameraCheck.setMaximumSize(QtCore.QSize(28, 16777215))
        self.viewCameraCheck.setStyleSheet("QCheckBox::indicator {\n"
"    image: url(:/images/icons/k1/camera.png);\n"
"    border: 1px solid rgba(30, 144, 255, 0.0);\n"
"    width: 26px;\n"
"    height: 26px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover {\n"
"    background: rgba(30, 144, 255, 0.2);\n"
"    border: 1px solid rgba(30, 144, 255, 0.4);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background: rgba(30, 144, 255, 0.4);\n"
"    border:1px solid rgba(30, 144, 255, 0.6);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover {\n"
"    background: rgba(30, 144, 255, 0.5);\n"
"    border:1px solid rgba(30, 144, 255, 0.7);\n"
"}\n"
"\n"
"")
        self.viewCameraCheck.setText("")
        self.viewCameraCheck.setChecked(True)
        self.viewCameraCheck.setObjectName("viewCameraCheck")
        self.horizontalLayout_2.addWidget(self.viewCameraCheck)
        self.viewEncounterCheck = QtWidgets.QCheckBox(self.layoutWidget1)
        self.viewEncounterCheck.setMaximumSize(QtCore.QSize(28, 16777215))
        self.viewEncounterCheck.setStyleSheet("QCheckBox::indicator {\n"
"    image: url(:/images/icons/k1/encounter.png);\n"
"    border: 1px solid rgba(30, 144, 255, 0.0);\n"
"    width: 26px;\n"
"    height: 26px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover {\n"
"    background: rgba(30, 144, 255, 0.2);\n"
"    border: 1px solid rgba(30, 144, 255, 0.4);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background: rgba(30, 144, 255, 0.4);\n"
"    border:1px solid rgba(30, 144, 255, 0.6);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover {\n"
"    background: rgba(30, 144, 255, 0.5);\n"
"    border:1px solid rgba(30, 144, 255, 0.7);\n"
"}\n"
"\n"
"")
        self.viewEncounterCheck.setText("")
        self.viewEncounterCheck.setChecked(True)
        self.viewEncounterCheck.setObjectName("viewEncounterCheck")
        self.horizontalLayout_2.addWidget(self.viewEncounterCheck)
        self.viewTriggerCheck = QtWidgets.QCheckBox(self.layoutWidget1)
        self.viewTriggerCheck.setMaximumSize(QtCore.QSize(28, 16777215))
        self.viewTriggerCheck.setStyleSheet("QCheckBox::indicator {\n"
"    image: url(:/images/icons/k1/trigger.png);\n"
"    border: 1px solid rgba(30, 144, 255, 0.0);\n"
"    width: 26px;\n"
"    height: 26px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover {\n"
"    background: rgba(30, 144, 255, 0.2);\n"
"    border: 1px solid rgba(30, 144, 255, 0.4);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background: rgba(30, 144, 255, 0.4);\n"
"    border:1px solid rgba(30, 144, 255, 0.6);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover {\n"
"    background: rgba(30, 144, 255, 0.5);\n"
"    border:1px solid rgba(30, 144, 255, 0.7);\n"
"}\n"
"\n"
"")
        self.viewTriggerCheck.setText("")
        self.viewTriggerCheck.setChecked(True)
        self.viewTriggerCheck.setObjectName("viewTriggerCheck")
        self.horizontalLayout_2.addWidget(self.viewTriggerCheck)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.renderArea = WalkmeshRenderer(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.renderArea.sizePolicy().hasHeightForWidth())
        self.renderArea.setSizePolicy(sizePolicy)
        self.renderArea.setMouseTracking(True)
        self.renderArea.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.renderArea.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.renderArea.setStyleSheet("background: black;")
        self.renderArea.setObjectName("renderArea")
        self.verticalLayout_2.addWidget(self.renderArea)
        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 838, 21))
        self.menubar.setObjectName("menubar")
        self.menuNew = QtWidgets.QMenu(self.menubar)
        self.menuNew.setObjectName("menuNew")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuWaypointLabels = QtWidgets.QMenu(self.menuView)
        self.menuWaypointLabels.setObjectName("menuWaypointLabels")
        self.menuTriggerLabels = QtWidgets.QMenu(self.menuView)
        self.menuTriggerLabels.setObjectName("menuTriggerLabels")
        self.menuDoorLabels = QtWidgets.QMenu(self.menuView)
        self.menuDoorLabels.setObjectName("menuDoorLabels")
        self.menuCreatureLabels = QtWidgets.QMenu(self.menuView)
        self.menuCreatureLabels.setObjectName("menuCreatureLabels")
        self.menuPlaceableLabels = QtWidgets.QMenu(self.menuView)
        self.menuPlaceableLabels.setObjectName("menuPlaceableLabels")
        self.menuMerchantLabels = QtWidgets.QMenu(self.menuView)
        self.menuMerchantLabels.setObjectName("menuMerchantLabels")
        self.menuSound_Labels = QtWidgets.QMenu(self.menuView)
        self.menuSound_Labels.setObjectName("menuSound_Labels")
        self.menuEncounterLabels = QtWidgets.QMenu(self.menuView)
        self.menuEncounterLabels.setObjectName("menuEncounterLabels")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_As = QtWidgets.QAction(MainWindow)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionRevert = QtWidgets.QAction(MainWindow)
        self.actionRevert.setObjectName("actionRevert")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionZoomIn = QtWidgets.QAction(MainWindow)
        self.actionZoomIn.setObjectName("actionZoomIn")
        self.actionZoomOut = QtWidgets.QAction(MainWindow)
        self.actionZoomOut.setObjectName("actionZoomOut")
        self.actionRecentreCamera = QtWidgets.QAction(MainWindow)
        self.actionRecentreCamera.setObjectName("actionRecentreCamera")
        self.actionDeleteSelected = QtWidgets.QAction(MainWindow)
        self.actionDeleteSelected.setObjectName("actionDeleteSelected")
        self.actionUseWaypointResRef = QtWidgets.QAction(MainWindow)
        self.actionUseWaypointResRef.setObjectName("actionUseWaypointResRef")
        self.actionUseWaypointName = QtWidgets.QAction(MainWindow)
        self.actionUseWaypointName.setObjectName("actionUseWaypointName")
        self.actionUseWaypointTag = QtWidgets.QAction(MainWindow)
        self.actionUseWaypointTag.setObjectName("actionUseWaypointTag")
        self.actionUseTriggerResRef = QtWidgets.QAction(MainWindow)
        self.actionUseTriggerResRef.setObjectName("actionUseTriggerResRef")
        self.actionUseTriggerTag = QtWidgets.QAction(MainWindow)
        self.actionUseTriggerTag.setObjectName("actionUseTriggerTag")
        self.actionUseDoorResRef = QtWidgets.QAction(MainWindow)
        self.actionUseDoorResRef.setObjectName("actionUseDoorResRef")
        self.actionUseDoorTag = QtWidgets.QAction(MainWindow)
        self.actionUseDoorTag.setObjectName("actionUseDoorTag")
        self.actionUseCreatureResRef = QtWidgets.QAction(MainWindow)
        self.actionUseCreatureResRef.setObjectName("actionUseCreatureResRef")
        self.actionUseCreatureName = QtWidgets.QAction(MainWindow)
        self.actionUseCreatureName.setObjectName("actionUseCreatureName")
        self.actionUseCreatureTag = QtWidgets.QAction(MainWindow)
        self.actionUseCreatureTag.setObjectName("actionUseCreatureTag")
        self.actionUseDoorName = QtWidgets.QAction(MainWindow)
        self.actionUseDoorName.setObjectName("actionUseDoorName")
        self.actionUseDoorResTag = QtWidgets.QAction(MainWindow)
        self.actionUseDoorResTag.setObjectName("actionUseDoorResTag")
        self.actionUseWaypointResName = QtWidgets.QAction(MainWindow)
        self.actionUseWaypointResName.setObjectName("actionUseWaypointResName")
        self.actionUseWaypointResTag = QtWidgets.QAction(MainWindow)
        self.actionUseWaypointResTag.setObjectName("actionUseWaypointResTag")
        self.actionUseTriggerName = QtWidgets.QAction(MainWindow)
        self.actionUseTriggerName.setObjectName("actionUseTriggerName")
        self.actionUseTriggerResTag = QtWidgets.QAction(MainWindow)
        self.actionUseTriggerResTag.setObjectName("actionUseTriggerResTag")
        self.actionUsePlaceableResRef = QtWidgets.QAction(MainWindow)
        self.actionUsePlaceableResRef.setObjectName("actionUsePlaceableResRef")
        self.actionUsePlaceableTag = QtWidgets.QAction(MainWindow)
        self.actionUsePlaceableTag.setObjectName("actionUsePlaceableTag")
        self.actionUsePlaceableName = QtWidgets.QAction(MainWindow)
        self.actionUsePlaceableName.setObjectName("actionUsePlaceableName")
        self.actionUseMerchantResRef = QtWidgets.QAction(MainWindow)
        self.actionUseMerchantResRef.setObjectName("actionUseMerchantResRef")
        self.actionUseMerchantName = QtWidgets.QAction(MainWindow)
        self.actionUseMerchantName.setObjectName("actionUseMerchantName")
        self.actionUseMerchantTag = QtWidgets.QAction(MainWindow)
        self.actionUseMerchantTag.setObjectName("actionUseMerchantTag")
        self.actionUseSoundResRef = QtWidgets.QAction(MainWindow)
        self.actionUseSoundResRef.setObjectName("actionUseSoundResRef")
        self.actionUseSoundName = QtWidgets.QAction(MainWindow)
        self.actionUseSoundName.setObjectName("actionUseSoundName")
        self.actionUseSoundTag = QtWidgets.QAction(MainWindow)
        self.actionUseSoundTag.setObjectName("actionUseSoundTag")
        self.actionUseEncounterResRef = QtWidgets.QAction(MainWindow)
        self.actionUseEncounterResRef.setObjectName("actionUseEncounterResRef")
        self.actionUseEncounterName = QtWidgets.QAction(MainWindow)
        self.actionUseEncounterName.setObjectName("actionUseEncounterName")
        self.actionUseEncounterTag = QtWidgets.QAction(MainWindow)
        self.actionUseEncounterTag.setObjectName("actionUseEncounterTag")
        self.menuNew.addAction(self.actionNew)
        self.menuNew.addAction(self.actionOpen)
        self.menuNew.addAction(self.actionSave)
        self.menuNew.addAction(self.actionSave_As)
        self.menuNew.addAction(self.actionRevert)
        self.menuNew.addSeparator()
        self.menuNew.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionDeleteSelected)
        self.menuWaypointLabels.addAction(self.actionUseWaypointResRef)
        self.menuWaypointLabels.addAction(self.actionUseWaypointName)
        self.menuWaypointLabels.addAction(self.actionUseWaypointTag)
        self.menuTriggerLabels.addAction(self.actionUseTriggerResRef)
        self.menuTriggerLabels.addAction(self.actionUseTriggerName)
        self.menuTriggerLabels.addAction(self.actionUseTriggerTag)
        self.menuDoorLabels.addAction(self.actionUseDoorResRef)
        self.menuDoorLabels.addAction(self.actionUseDoorName)
        self.menuDoorLabels.addAction(self.actionUseDoorTag)
        self.menuCreatureLabels.addAction(self.actionUseCreatureResRef)
        self.menuCreatureLabels.addAction(self.actionUseCreatureName)
        self.menuCreatureLabels.addAction(self.actionUseCreatureTag)
        self.menuPlaceableLabels.addAction(self.actionUsePlaceableResRef)
        self.menuPlaceableLabels.addAction(self.actionUsePlaceableName)
        self.menuPlaceableLabels.addAction(self.actionUsePlaceableTag)
        self.menuMerchantLabels.addAction(self.actionUseMerchantResRef)
        self.menuMerchantLabels.addAction(self.actionUseMerchantName)
        self.menuMerchantLabels.addAction(self.actionUseMerchantTag)
        self.menuSound_Labels.addAction(self.actionUseSoundResRef)
        self.menuSound_Labels.addAction(self.actionUseSoundName)
        self.menuSound_Labels.addAction(self.actionUseSoundTag)
        self.menuEncounterLabels.addAction(self.actionUseEncounterResRef)
        self.menuEncounterLabels.addAction(self.actionUseEncounterName)
        self.menuEncounterLabels.addAction(self.actionUseEncounterTag)
        self.menuView.addAction(self.actionZoomIn)
        self.menuView.addAction(self.actionZoomOut)
        self.menuView.addAction(self.actionRecentreCamera)
        self.menuView.addSeparator()
        self.menuView.addAction(self.menuCreatureLabels.menuAction())
        self.menuView.addAction(self.menuDoorLabels.menuAction())
        self.menuView.addAction(self.menuPlaceableLabels.menuAction())
        self.menuView.addAction(self.menuMerchantLabels.menuAction())
        self.menuView.addAction(self.menuSound_Labels.menuAction())
        self.menuView.addAction(self.menuWaypointLabels.menuAction())
        self.menuView.addAction(self.menuEncounterLabels.menuAction())
        self.menuView.addAction(self.menuTriggerLabels.menuAction())
        self.menubar.addAction(self.menuNew.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.filterEdit.setPlaceholderText(_translate("MainWindow", "filter..."))
        self.lockInstancesCheck.setToolTip(_translate("MainWindow", "Lock all instances in place"))
        self.label.setText(_translate("MainWindow", "|"))
        self.viewCreatureCheck.setToolTip(_translate("MainWindow", "Show Creatures"))
        self.viewDoorCheck.setToolTip(_translate("MainWindow", "Show Doors"))
        self.viewPlaceableCheck.setToolTip(_translate("MainWindow", "Show Placeables"))
        self.viewStoreCheck.setToolTip(_translate("MainWindow", "Show Merchants"))
        self.viewSoundCheck.setToolTip(_translate("MainWindow", "Show Sounds"))
        self.viewWaypointCheck.setToolTip(_translate("MainWindow", "Show Waypoints"))
        self.viewCameraCheck.setToolTip(_translate("MainWindow", "Show Cameras"))
        self.viewEncounterCheck.setToolTip(_translate("MainWindow", "Show Encounters"))
        self.viewTriggerCheck.setToolTip(_translate("MainWindow", "Show Triggers"))
        self.menuNew.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuWaypointLabels.setTitle(_translate("MainWindow", "Waypoint Labels"))
        self.menuTriggerLabels.setTitle(_translate("MainWindow", "Trigger Labels"))
        self.menuDoorLabels.setTitle(_translate("MainWindow", "Door Labels"))
        self.menuCreatureLabels.setTitle(_translate("MainWindow", "Creature Labels"))
        self.menuPlaceableLabels.setTitle(_translate("MainWindow", "Placeable Labels"))
        self.menuMerchantLabels.setTitle(_translate("MainWindow", "Merchant Labels"))
        self.menuSound_Labels.setTitle(_translate("MainWindow", "Sound Labels"))
        self.menuEncounterLabels.setTitle(_translate("MainWindow", "Encounter Labels"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave_As.setText(_translate("MainWindow", "Save As"))
        self.actionRevert.setText(_translate("MainWindow", "Revert"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionZoomIn.setText(_translate("MainWindow", "Zoom In"))
        self.actionZoomOut.setText(_translate("MainWindow", "Zoom Out"))
        self.actionRecentreCamera.setText(_translate("MainWindow", "Reset Camera"))
        self.actionDeleteSelected.setText(_translate("MainWindow", "Delete Selected"))
        self.actionUseWaypointResRef.setText(_translate("MainWindow", "ResRef"))
        self.actionUseWaypointName.setText(_translate("MainWindow", "Name"))
        self.actionUseWaypointTag.setText(_translate("MainWindow", "Tag"))
        self.actionUseTriggerResRef.setText(_translate("MainWindow", "ResRef"))
        self.actionUseTriggerTag.setText(_translate("MainWindow", "Tag"))
        self.actionUseDoorResRef.setText(_translate("MainWindow", "ResRef"))
        self.actionUseDoorTag.setText(_translate("MainWindow", "Tag"))
        self.actionUseCreatureResRef.setText(_translate("MainWindow", "ResRef"))
        self.actionUseCreatureName.setText(_translate("MainWindow", "Name"))
        self.actionUseCreatureTag.setText(_translate("MainWindow", "Tag"))
        self.actionUseDoorName.setText(_translate("MainWindow", "Name"))
        self.actionUseDoorResTag.setText(_translate("MainWindow", "Tag (UTD)"))
        self.actionUseWaypointResName.setText(_translate("MainWindow", "Name (UTW)"))
        self.actionUseWaypointResTag.setText(_translate("MainWindow", "Tag (UTW)"))
        self.actionUseTriggerName.setText(_translate("MainWindow", "Name"))
        self.actionUseTriggerResTag.setText(_translate("MainWindow", "Tag (UTT)"))
        self.actionUsePlaceableResRef.setText(_translate("MainWindow", "ResRef"))
        self.actionUsePlaceableTag.setText(_translate("MainWindow", "Tag"))
        self.actionUsePlaceableName.setText(_translate("MainWindow", "Name"))
        self.actionUseMerchantResRef.setText(_translate("MainWindow", "ResRef"))
        self.actionUseMerchantName.setText(_translate("MainWindow", "Name"))
        self.actionUseMerchantTag.setText(_translate("MainWindow", "Tag"))
        self.actionUseSoundResRef.setText(_translate("MainWindow", "ResRef"))
        self.actionUseSoundName.setText(_translate("MainWindow", "Name"))
        self.actionUseSoundTag.setText(_translate("MainWindow", "Tag"))
        self.actionUseEncounterResRef.setText(_translate("MainWindow", "ResRef"))
        self.actionUseEncounterName.setText(_translate("MainWindow", "Name"))
        self.actionUseEncounterTag.setText(_translate("MainWindow", "Tag"))
from toolset.gui.widgets.walkmesh_renderer import WalkmeshRenderer
import resources_rc
