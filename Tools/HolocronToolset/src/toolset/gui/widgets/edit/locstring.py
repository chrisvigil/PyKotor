from __future__ import annotations

from typing import TYPE_CHECKING

from pykotor.common.language import LocalizedString
from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget
from toolset.gui.dialogs.edit.locstring import LocalizedStringDialog

if TYPE_CHECKING:
    from toolset.data.installation import HTInstallation


class LocalizedStringLineEdit(QWidget):
    editingFinished = QtCore.pyqtSignal()

    def __init__(self, parent: QWidget):
        """Initialize a locstring edit widget
        Args:
            parent: QWidget - Parent widget
        Returns:
            None
        - Initialize UI from designer file
        - Set initial locstring to invalid
        - Connect edit button to editLocstring method
        - Connect double click on text to editLocstring.
        """
        super().__init__(parent)

        from toolset.uic.widgets.locstring_edit import Ui_Form
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self._installation: HTInstallation | None = None
        self._locstring: LocalizedString = LocalizedString.from_invalid()

        self.ui.editButton.clicked.connect(self.editLocstring)
        self.ui.locstringText.mouseDoubleClickEvent = lambda _: self.editLocstring()

    def setInstallation(self, installation: HTInstallation) -> None:
        self._installation = installation

    def setLocstring(self, locstring: LocalizedString) -> None:
        """Sets the localized string for a UI element.

        Args:
        ----
            locstring: {Localized string object to set}

        Returns:
        -------
            None: {No return value}
        Processing Logic:
        ----------------
            - Sets the internal locstring property to the passed in value
            - Checks if the stringref is -1
            - If so, sets the text directly from the string and uses white background
            - If not, looks up the string from the talktable and uses a yellow background
        """
        self._locstring = locstring
        if locstring.stringref == -1:
            text = str(locstring)
            self.ui.locstringText.setText(text if text != "-1" else "")
            self.ui.locstringText.setStyleSheet("QLineEdit {background-color: white;}")
        else:
            self.ui.locstringText.setText(self._installation.talktable().string(locstring.stringref))
            self.ui.locstringText.setStyleSheet("QLineEdit {background-color: #fffded;}")

    def editLocstring(self) -> None:
        dialog = LocalizedStringDialog(self, self._installation, self._locstring)
        if dialog.exec_():
            self.setLocstring(dialog.locstring)
            self.editingFinished.emit()

    def locstring(self) -> LocalizedString:
        return self._locstring
