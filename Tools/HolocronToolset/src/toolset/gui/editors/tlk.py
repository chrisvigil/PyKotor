from __future__ import annotations

from time import sleep
from typing import TYPE_CHECKING

from pykotor.common.language import Language
from pykotor.common.misc import ResRef
from pykotor.resource.formats.tlk import TLK, TLKEntry, bytes_tlk, read_tlk, write_tlk
from pykotor.resource.type import ResourceType
from PyQt5 import QtCore
from PyQt5.QtCore import QSortFilterProxyModel, QThread
from PyQt5.QtGui import QStandardItem, QStandardItemModel
from PyQt5.QtWidgets import QAction, QDialog, QProgressBar, QShortcut, QVBoxLayout, QWidget
from toolset.gui.editor import Editor

if TYPE_CHECKING:
    import os

    from toolset.data.installation import HTInstallation


class TLKEditor(Editor):
    def __init__(self, parent: QWidget | None, installation: HTInstallation | None = None):
        """Initialize the TLK Editor.

        Args:
        ----
            parent: QWidget - Parent widget
            installation: HTInstallation | None - Installation object

        Processing Logic:
        ----------------
            - Set up the UI from the designer file
            - Connect menu and signal handlers
            - Hide search/jump boxes
            - Set up the data model and proxy model for the table view
            - Make bottom panel take minimal space
            - Create a new empty TLK file.
        """
        supported = [ResourceType.TLK, ResourceType.TLK_XML, ResourceType.TLK_JSON]
        super().__init__(parent, "TLK Editor", "none", supported, supported, installation)

        from toolset.uic.editors.tlk import Ui_MainWindow

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self._setupMenus()
        self._setupSignals()

        self.ui.searchBox.setVisible(False)
        self.ui.jumpBox.setVisible(False)

        self.language = Language.ENGLISH

        self.model = QStandardItemModel(self)
        self.proxyModel = QSortFilterProxyModel(self)
        self.proxyModel.setSourceModel(self.model)
        self.ui.talkTable.setModel(self.proxyModel)

        # Make the bottom panel take as little space possible
        self.ui.splitter.setSizes([99999999, 1])

        self.new()

    def _setupSignals(self) -> None:
        """Set up signal connections for UI actions and widgets.

        Processing Logic:
        ----------------
            - Connect action triggers to slot functions
            - Connect button clicks to slot functions
            - Connect table and text edits to update functions
            - Set up keyboard shortcuts to trigger actions.
        """
        self.ui.actionGoTo.triggered.connect(self.toggleGotoBox)
        self.ui.jumpButton.clicked.connect(lambda: self.gotoLine(self.ui.jumpSpinbox.value()))
        self.ui.actionFind.triggered.connect(self.toggleFilterBox)
        self.ui.searchButton.clicked.connect(lambda: self.doFilter(self.ui.searchEdit.text()))
        self.ui.actionInsert.triggered.connect(self.insert)
        #self.ui.actionAuto_detect_slower.triggered.connect()

        self.ui.talkTable.clicked.connect(self.selectionChanged)
        self.ui.textEdit.textChanged.connect(self.updateEntry)
        self.ui.soundEdit.textChanged.connect(self.updateEntry)

        self.populateLanguageMenu()

        QShortcut("Ctrl+F", self).activated.connect(self.toggleFilterBox)
        QShortcut("Ctrl+G", self).activated.connect(self.toggleGotoBox)
        QShortcut("Ctrl+I", self).activated.connect(self.insert)

    def populateLanguageMenu(self):
        self.ui.menuLanguage.clear()

        # Add 'Auto_Detect_slower' action first
        autoDetectAction = QAction("Auto_detect_slower", self)
        autoDetectAction.triggered.connect(lambda: self.onLanguageSelected("auto_detect"))
        self.ui.menuLanguage.addAction(autoDetectAction)

        # Separator
        self.ui.menuLanguage.addSeparator()

        # Add languages from the enum
        for language in Language:
            action = QAction(language.name.replace("_", " "), self)
            action.triggered.connect(lambda _checked, lang=language: self.onLanguageSelected(lang))
            self.ui.menuLanguage.addAction(action)

    def onLanguageSelected(self, language) -> None:
        if isinstance(language, Language):
            print(f"Language selected: {language.name}")
            self.change_language(language)
        else:
            print("Auto detect selected")
            self.change_language(Language.UNKNOWN)

    def change_language(self, language: Language):

        tlk: TLK = read_tlk(self._revert, language=language)
        self._extracted_from_new_2()
        dialog = LoaderDialog(self, bytes_tlk(tlk), self.model)
        self._extracted_from_load_10(dialog)
        self.language = tlk.language

    def load(self, filepath: os.PathLike | str, resref: str, restype: ResourceType, data: bytes) -> None:
        """Loads data into the resource from a file.

        Args:
        ----
            filepath: The path to the file to load from.
            resref: The resource reference.
            restype: The resource type.
            data: The raw data bytes.

        Processing Logic:
        ----------------
            - Clears existing model data
            - Sets column count to 2 and hides second column
            - Opens dialog to process loading data
            - Sets loaded data as model
            - Sets sorting proxy model
            - Connects selection changed signal
            - Sets max rows in spinbox.
        """
        super().load(filepath, resref, restype, data)
        self._extracted_from_new_2()
        dialog = LoaderDialog(self, data, self.model)
        self._extracted_from_load_10(dialog)

    # TODO Rename this here and in `change_language` and `load`
    def _extracted_from_load_10(self, dialog: LoaderDialog):
        dialog.exec_()
        self.model = dialog.model
        self.proxyModel = QSortFilterProxyModel(self)
        self.proxyModel.setSourceModel(self.model)
        self.ui.talkTable.setModel(self.proxyModel)
        self.ui.talkTable.selectionModel().selectionChanged.connect(self.selectionChanged)
        self.ui.jumpSpinbox.setMaximum(self.model.rowCount())

    def new(self) -> None:
        super().new()

        self._extracted_from_new_2()
        self.ui.textEdit.setEnabled(False)
        self.ui.soundEdit.setEnabled(False)

    # TODO Rename this here and in `_extracted_from_load_5` and `new`
    def _extracted_from_new_2(self):
        self.model.clear()
        self.model.setColumnCount(2)
        self.ui.talkTable.hideColumn(1)

    def build(self) -> tuple[bytes, bytes]:
        """Builds a TLK file from the model data.

        Returns
        -------
            tuple[bytes, bytes]: A tuple containing the TLK data and an empty bytes object

        Processing Logic:
        ----------------
        - Iterate through each row in the model
        - Extract the text and sound from each item
        - Add an entry to the TLK object with the text and sound
        - Write the TLK object to a byte array
        - Return the byte array and an empty bytes object as a tuple.
        """
        tlk = TLK()
        tlk.language = self.language

        for i in range(self.model.rowCount()):
            text = self.model.item(i, 0).text()
            sound = ResRef(self.model.item(i, 1).text())
            tlk.entries.append(TLKEntry(text, sound))

        data = bytearray()
        write_tlk(tlk, data, self._restype)
        return data, b""

    def insert(self) -> None:
        self.model.appendRow([QStandardItem(""), QStandardItem("")])

    def doFilter(self, text: str) -> None:
        self.proxyModel.setFilterFixedString(text)

    def toggleFilterBox(self) -> None:
        self.ui.searchBox.setVisible(not self.ui.searchBox.isVisible())

    def gotoLine(self, line: int) -> None:
        index = self.model.index(line, 0)
        proxyIndex = self.proxyModel.mapFromSource(index)
        self.ui.talkTable.scrollTo(proxyIndex)
        self.ui.talkTable.setCurrentIndex(proxyIndex)

    def toggleGotoBox(self) -> None:
        self.ui.jumpBox.setVisible(not self.ui.jumpBox.isVisible())

    def selectionChanged(self) -> None:
        """Handle selection changes in the talk table.

        Processing Logic:
        ----------------
            - Check if any rows are selected in the talk table
            - If no rows selected, disable text and sound editors
            - If rows selected, enable text and sound editors
            - Get selected row data from model
            - Populate text and sound editors with data from selected row.
        """
        selected = self.ui.talkTable.selectionModel().selection()

        if len(selected.indexes()) == 0:
            self.ui.textEdit.setEnabled(False)
            self.ui.soundEdit.setEnabled(False)
            return

        self.ui.textEdit.setEnabled(True)
        self.ui.soundEdit.setEnabled(True)

        proxyIndex = selected.indexes()[0]
        sourceIndex = self.proxyModel.mapToSource(proxyIndex)
        item = self.model.itemFromIndex(sourceIndex)

        text = item.text()
        sound = self.model.item(sourceIndex.row(), 1).text()

        self.ui.textEdit.setPlainText(text)
        self.ui.soundEdit.setText(sound)

    def updateEntry(self) -> None:
        proxyIndex = self.ui.talkTable.selectedIndexes()[0]
        sourceIndex = self.proxyModel.mapToSource(proxyIndex)

        self.model.item(sourceIndex.row(), 0).setText(self.ui.textEdit.toPlainText())
        self.model.item(sourceIndex.row(), 1).setText(self.ui.soundEdit.text())


class LoaderDialog(QDialog):
    def __init__(self, parent, fileData, model):
        """Initializes the loading dialog.

        Args:
        ----
            parent: {The parent widget of the dialog}
            fileData: {The data to load}
            model: {The model to populate}.

        Processing Logic:
        ----------------
            - Creates a progress bar to display loading progress
            - Sets up the dialog layout and adds progress bar
            - Starts a worker thread to load the data in the background
            - Connects signals from worker to update progress bar.
        """
        super().__init__(parent)

        self._progressBar = QProgressBar(self)
        self._progressBar.setMinimum(0)
        self._progressBar.setMaximum(0)
        self._progressBar.setTextVisible(False)

        self.setLayout(QVBoxLayout())
        self.layout().addWidget(self._progressBar)

        self.setWindowTitle("Loading...")
        self.setFixedSize(200, 40)

        self.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)
        self.setWindowFlag(QtCore.Qt.WindowContextHelpButtonHint, False)

        self.model = QStandardItemModel()
        self.model.setColumnCount(2)

        self.worker = LoaderWorker(fileData, model)
        self.worker.entryCount.connect(self.onEntryCount)
        self.worker.batch.connect(self.onBatch)
        self.worker.loaded.connect(self.onLoaded)
        self.worker.language.connect(self.setupLanguage)
        self.worker.start()

    def onEntryCount(self, count: int):
        self._progressBar.setMaximum(count)

    def onBatch(self, batch: list[QStandardItem]):
        for row in batch:
            self.model.appendRow(row)
            index = self.model.rowCount() - 1
            self.model.setVerticalHeaderItem(index, QStandardItem(str(index)))
        self._progressBar.setValue(self.model.rowCount())

    def setupLanguage(self, language: Language):
        self.language = language

    def onLoaded(self):
        self.close()


class LoaderWorker(QThread):
    batch = QtCore.pyqtSignal(object)
    entryCount = QtCore.pyqtSignal(object)
    loaded = QtCore.pyqtSignal()
    language = QtCore.pyqtSignal(object)

    def __init__(self, fileData, model) -> None:
        super().__init__()
        self._fileData: bytes = fileData
        self._model: QStandardItemModel = model

    def load_data(self):
        """Load tlk data from file."""
        tlk = read_tlk(self._fileData)
        self.entryCount.emit(len(tlk))
        self.language.emit(tlk.language)

        batch = []
        for _stringref, entry in tlk:
            batch.append([QStandardItem(entry.text), QStandardItem(entry.voiceover.get())])
            if len(batch) > 200:
                self.batch.emit(batch)
                batch = []
                sleep(0.001)
        self.batch.emit(batch)
        self.loaded.emit()

    def run(self):
        """Load tlk data from file in batches.

        Processing Logic:
        ----------------
            - Reads timeline data from file
            - Counts number of entries and emits count
            - Loops through entries and batches data into lists of 200
            - Emits batches and sleeps to allow UI to update
            - Emits final batch
            - Signals loading is complete.
        """
        self.load_data()
