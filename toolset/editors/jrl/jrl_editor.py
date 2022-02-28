from typing import Optional, Union

import chardet
from PyQt5.QtCore import QItemSelection, QPoint
from PyQt5.QtGui import QIcon, QPixmap, QStandardItemModel, QStandardItem, QColor
from PyQt5.QtWidgets import QWidget, QPlainTextEdit, QLineEdit, QMenu, QShortcut
from pykotor.common.language import LocalizedString
from pykotor.extract.installation import Installation
from pykotor.resource.formats.gff import load_gff, write_gff
from pykotor.resource.generics.jrl import construct_jrl, JRL, JRLQuest, JRLEntry, dismantle_jrl, JRLQuestPriority
from pykotor.resource.type import ResourceType

from data.installation import HTInstallation
from editors.editor import Editor, LocalizedStringDialog
from editors.jrl import jrl_editor_ui


class JRLEditor(Editor):
    """
    Journal Editor is designed for editing JRL files.

    Journal Editor is simular to the NWN counterpart which displays quests as root items in a tree plus their respective
    entries as child items. Entries that are marked as end nodes are highlighted a dark red color. The selected entry
    or quest can be edited at the bottom of the window.
    """

    # JRLEditor stores a tree model and a JRL instance. These two objects must be kept in sync with each other manually:
    # eg. if you code an entry to be deleted from the journal, ensure that you delete corresponding item in the tree.\
    # It would be nice at some point to create our own implementation of QAbstractItemModel that automatically mirrors
    # the JRL object.

    def __init__(self, parent: QWidget, installation: Optional[HTInstallation] = None):
        supported = [ResourceType.JRL]
        super().__init__(parent, "Journal Editor", supported, supported, installation)
        self.resize(400, 250)

        self.ui = jrl_editor_ui.Ui_MainWindow()
        self.ui.setupUi(self)
        self._setup_menus()
        self._setupSignals()

        iconVersion = "x" if installation is None else "2" if installation.tsl else "1"
        iconPath = ":/images/icons/k{}/journal.png".format(iconVersion)
        self.setWindowIcon(QIcon(QPixmap(iconPath)))

        self._jrl: JRL = JRL()
        self._model: QStandardItemModel = QStandardItemModel(self)
        self.setInstallation(installation)

        self.ui.journalTree.setModel(self._model)

        self.new()

    def _setupSignals(self) -> None:
        self.ui.journalTree.selectionModel().selectionChanged.connect(self.onSelectionChanged)
        self.ui.journalTree.customContextMenuRequested.connect(self.onContextMenuRequested)

        self.ui.categoryNameButton.clicked.connect(self.changeQuestName)
        self.ui.entryTextEdit.doubleClicked.connect(self.changeEntryText)

        # Make sure all these signals are excusively fired through user interaction NOT when values change
        # programmatically, otherwise values bleed into other items when onSelectionChanged() fires.
        self.ui.categoryTag.editingFinished.connect(self.onValueUpdated)
        self.ui.categoryPlotSpin.editingFinished.connect(self.onValueUpdated)
        self.ui.categoryPlanetSelect.activated.connect(self.onValueUpdated)
        self.ui.categoryPrioritySelect.activated.connect(self.onValueUpdated)
        self.ui.categoryCommentEdit.keyReleased.connect(self.onValueUpdated)
        self.ui.entryIdSpin.editingFinished.connect(self.onValueUpdated)
        self.ui.entryXpSpin.editingFinished.connect(self.onValueUpdated)
        self.ui.entryEndCheck.clicked.connect(self.onValueUpdated)

        QShortcut("Del", self).activated.connect(self.onDeleteShortcut)

    def load(self, filepath: str, resref: str, restype: ResourceType, data: bytes) -> None:
        super().load(filepath, resref, restype, data)

        self._jrl = construct_jrl(load_gff(data))

        self._model.clear()
        for quest in self._jrl.quests:
            questItem = QStandardItem()
            questItem.setData(quest)
            self.refreshQuestItem(questItem)
            self._model.appendRow(questItem)

            for entry in quest.entries:
                entryItem = QStandardItem()
                entryItem.setData(entry)
                self.refreshEntryItem(entryItem)
                questItem.appendRow(entryItem)

    def build(self) -> bytes:
        data = bytearray()
        write_gff(dismantle_jrl(self._jrl), data)
        return data

    def new(self) -> None:
        super().new()
        self._jrl = JRL()
        self._model.clear()

    def setInstallation(self, installation: HTInstallation) -> None:
        self._installation = installation

        planets = installation.htGetCache2DA(HTInstallation.TwoDA_PLANETS)

        self.ui.categoryPlanetSelect.clear()
        self.ui.categoryPlanetSelect.addItem("[None]", -1)
        for row in planets:
            text = self._installation.talktable().string(row.get_integer("name"))
            text = row.get_string("label").replace("_", " ").title() if text == "" or text is None else text
            self.ui.categoryPlanetSelect.addItem(text)

    def refreshEntryItem(self, entryItem: QStandardItem) -> None:
        """
        Updates the specified item's (storing entry data) text.

        Args:
            entryItem: The item to refresh.
        """
        text = "[{}] {}".format(entryItem.data().entry_id, self._installation.string(entryItem.data().text))
        entryItem.setForeground(QColor(0x880000 if entryItem.data().end else 0x000000))
        entryItem.setText(text)

    def refreshQuestItem(self, questItem: QStandardItem) -> None:
        """
        Updates the specified item's (storing quest data) text.

        Args:
            questItem: The item to refresh.
        """
        text = self._installation.string(questItem.data().name, "[Unnamed]")
        questItem.setText(text)

    def changeQuestName(self) -> None:
        """
        Opens a LocalizedStringDialog for editing the name of the selected quest.
        """
        dialog = LocalizedStringDialog(self, self._installation, self.ui.categoryNameEdit.locstring)
        if dialog.exec_():
            self._loadLocstring(self.ui.categoryNameEdit, dialog.locstring)
            self.onValueUpdated()
            item = self._model.itemFromIndex(self.ui.journalTree.selectedIndexes()[0])
            quest: JRLQuest = item.data()
            quest.name = dialog.locstring
            self.refreshQuestItem(item)

    def changeEntryText(self) -> None:
        """
        Opens a LocalizedStringDialog for editing the text of the selected entry.
        """
        dialog = LocalizedStringDialog(self, self._installation, self.ui.entryTextEdit.locstring)
        if dialog.exec_():
            self._loadLocstring(self.ui.entryTextEdit, dialog.locstring)
            self.onValueUpdated()
            item = self._model.itemFromIndex(self.ui.journalTree.selectedIndexes()[0])
            entry: JRLEntry = item.data()
            entry.text = dialog.locstring
            self.refreshEntryItem(item)

    def removeQuest(self, questItem: QStandardItem) -> None:
        """
        Removes a quest from the journal.

        Args:
            questItem: The item in the tree that stores the quest.
        """
        quest = questItem.data()
        self._model.removeRow(questItem.row())
        self._jrl.quests.remove(quest)

    def removeEntry(self, entryItem: QStandardItem) -> None:
        """
        Removes an entry from the journal.

        Args:
            entryItem: The item in the tree that stores the entry.
        """
        entry = entryItem.data()
        entryItem.parent().removeRow(entryItem.row())
        for quest in self._jrl.quests:
            if entry in quest.entries:
                quest.entries.remove(entry)
                break

    def addEntry(self, questItem: QStandardItem, newEntry: JRLEntry):
        """
        Adds a entry to a quest in the journal.

        Args:
            questItem: The item in the tree that stores the quest.
            newEntry: The entry to add into the quest.
        """
        entryItem = QStandardItem()
        entryItem.setData(newEntry)
        self.refreshEntryItem(entryItem)
        questItem.appendRow(entryItem)
        questItem.data().entries.append(newEntry)

    def addQuest(self, newQuest: JRLQuest):
        """
        Adds a quest to the journal.

        Args:
            newQuest: The new quest to be added in.
        """
        questItem = QStandardItem()
        questItem.setData(newQuest)
        self.refreshQuestItem(questItem)
        self._model.appendRow(questItem)
        self._jrl.quests.append(newQuest)

    def onValueUpdated(self) -> None:
        """
        This method should be connected to all the widgets that store data related quest or entry text (besides the
        ones storing localized strings, those are updated elsewhere). This method will update either all the values
        for an entry or quest based off the aforementioned widgets.
        """
        item = self._model.itemFromIndex(self.ui.journalTree.selectedIndexes()[0])
        data = item.data()
        if isinstance(data, JRLQuest):
            data.name = self.ui.categoryNameEdit.locstring
            data.tag = self.ui.categoryTag.text()
            data.plot_index = self.ui.categoryPlotSpin.value()
            data.planet_id = self.ui.categoryPlanetSelect.currentIndex() - 1
            data.priority = JRLQuestPriority(self.ui.categoryPrioritySelect.currentIndex())
            data.comment = self.ui.categoryCommentEdit.toPlainText()
        elif isinstance(data, JRLEntry):
            data.text = self.ui.entryTextEdit.locstring
            data.end = self.ui.entryEndCheck.isChecked()
            data.xp_percentage = self.ui.entryXpSpin.value()
            data.entry_id = self.ui.entryIdSpin.value()
            self.refreshEntryItem(item)

    def onSelectionChanged(self, selection: QItemSelection) -> None:
        """
        This method should be connected to a signal that emits when selection changes for the journalTree widget. It
        will update the widget values that store data for either entries or quests, depending what has been selected
        in the tree.
        """
        self.ui.categoryCommentEdit.blockSignals(True)
        self.ui.entryTextEdit.blockSignals(True)

        if selection.indexes():
            item = self._model.itemFromIndex(selection.indexes()[0])
            data = item.data()
            if isinstance(data, JRLQuest):
                self.ui.questPages.setCurrentIndex(0)
                self._loadLocstring(self.ui.categoryNameEdit, data.name)
                self.ui.categoryTag.setText(data.tag)
                self.ui.categoryPlotSpin.setValue(data.plot_index)
                self.ui.categoryPlanetSelect.setCurrentIndex(data.planet_id + 1)
                self.ui.categoryPrioritySelect.setCurrentIndex(data.priority.value)
                self.ui.categoryCommentEdit.setPlainText(data.comment)
            elif isinstance(data, JRLEntry):
                self.ui.questPages.setCurrentIndex(1)
                self._loadLocstring(self.ui.entryTextEdit, data.text)
                self.ui.entryEndCheck.setChecked(data.end)
                self.ui.entryXpSpin.setValue(data.xp_percentage)
                self.ui.entryIdSpin.setValue(data.entry_id)

        self.ui.categoryCommentEdit.blockSignals(False)
        self.ui.entryTextEdit.blockSignals(False)


    def onContextMenuRequested(self, point: QPoint) -> None:
        """
        This method should be connected to the customContextMenuRequested of the journalTree object. This will popup the
        context menu and display various options depending on if there is an item selected in the tree and what kind
        of data the item stores (Quest or Entry).
        """
        index = self.ui.journalTree.indexAt(point)
        item = self._model.itemFromIndex(index)

        menu = QMenu(self)

        if item:
            index = self.ui.journalTree.selectedIndexes()[0]
            item = self._model.itemFromIndex(index)
            data = item.data()

            if isinstance(data, JRLQuest):
                menu.addAction("Add Entry").triggered.connect(lambda: self.addEntry(item, JRLEntry()))
                menu.addAction("Remove Quest").triggered.connect(lambda: self.removeQuest(item))
            elif isinstance(data, JRLEntry):
                menu.addAction("Remove Entry").triggered.connect(lambda: self.removeEntry(item))
        else:
            menu.addAction("Add Quest").triggered.connect(lambda: self.addQuest(JRLQuest()))

        menu.popup(self.ui.journalTree.viewport().mapToGlobal(point))

    def onDeleteShortcut(self) -> None:
        """
        This method should be connected to the activated signal of a QShortcut. The method will delete the selected
        item from the tree.
        """

        if self.ui.journalTree.selectedIndexes():
            index = self.ui.journalTree.selectedIndexes()[0]
            item = self._model.itemFromIndex(index)

            if item.parent() is None:  # ie. root item, therefore quest
                self.removeQuest(item)
            else:  # child item, therefore entry
                self.removeEntry(item)
