import math

from pykotor.common.misc import Color, ResRef
from pykotor.resource.generics.git import GITPlaceable
from PyQt5.QtGui import QColor, QIcon, QImage, QPixmap
from PyQt5.QtWidgets import QColorDialog, QDialog, QDoubleSpinBox, QLabel, QWidget
from toolset.gui.widgets.long_spinbox import LongSpinBox


class PlaceableDialog(QDialog):
    def __init__(self, parent: QWidget, placeable: GITPlaceable):
        super().__init__(parent)

        from toolset.uic.dialogs.instance.placeable import Ui_Dialog

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.setWindowTitle("Edit Placeable")
        self.setWindowIcon(QIcon(QPixmap(":/images/icons/k1/placeable.png")))

        self.ui.colorButton.clicked.connect(lambda: self.changeColor(self.ui.colorSpin))
        self.ui.colorSpin.valueChanged.connect(lambda value: self.redoColorImage(value, self.ui.color))

        self.ui.resrefEdit.setText(placeable.resref.get())
        self.ui.xPosSpin.setValue(placeable.position.x)
        self.ui.yPosSpin.setValue(placeable.position.y)
        self.ui.zPosSpin.setValue(placeable.position.z)
        self.ui.bearingSpin.setValue(math.degrees(placeable.bearing))
        self.ui.colorSpin.setValue(0 if placeable.tweak_color is None else placeable.tweak_color.rgb_integer())

        self.placeable: GITPlaceable = placeable

        for widget in [getattr(self.ui, attr) for attr in dir(self.ui)]:
            if isinstance(widget, QDoubleSpinBox):
                widget.setDecimals(8)

    def accept(self) -> None:
        super().accept()
        self.placeable.resref = ResRef(self.ui.resrefEdit.text())
        self.placeable.position.x = self.ui.xPosSpin.value()
        self.placeable.position.y = self.ui.yPosSpin.value()
        self.placeable.position.z = self.ui.zPosSpin.value()
        self.placeable.bearing = math.radians(self.ui.bearingSpin.value())
        self.placeable.tweak_color = Color.from_rgb_integer(self.ui.colorSpin.value()) if self.ui.colorSpin.value() != 0 else None

    def changeColor(self, colorSpin: LongSpinBox) -> None:
        qcolor = QColorDialog.getColor(QColor(colorSpin.value()))
        color = Color.from_rgb_integer(qcolor.rgb())
        colorSpin.setValue(color.rgb_integer())

    def redoColorImage(self, value: int, colorLabel: QLabel) -> None:
        color = Color.from_bgr_integer(value)
        r, g, b = int(color.r * 255), int(color.g * 255), int(color.b * 255)
        data = bytes([r, g, b] * 16 * 16)
        pixmap = QPixmap.fromImage(QImage(data, 16, 16, QImage.Format_RGB888))
        colorLabel.setPixmap(pixmap)
