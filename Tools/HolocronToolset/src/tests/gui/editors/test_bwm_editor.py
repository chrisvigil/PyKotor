from __future__ import annotations

import os
import pathlib
import sys
import unittest
from unittest import TestCase

try:
    from PyQt5.QtTest import QTest
    from PyQt5.QtWidgets import QApplication
except (ImportError, ModuleNotFoundError):
    QTest, QApplication = None, None  # type: ignore[misc, assignment]


TESTS_FILES_PATH = next(f for f in pathlib.Path(__file__).parents if f.name == "tests") / "files"

if getattr(sys, "frozen", False) is False:
    def add_sys_path(p):
        working_dir = str(p)
        if working_dir in sys.path:
            sys.path.remove(working_dir)
        sys.path.insert(0, working_dir)
    pykotor_path = pathlib.Path(__file__).parents[6] / "Libraries" / "PyKotor" / "src" / "pykotor"
    if pykotor_path.exists():
        add_sys_path(pykotor_path.parent)
    gl_path = pathlib.Path(__file__).parents[6] / "Libraries" / "PyKotorGL" / "src" / "pykotor"
    if gl_path.exists():
        add_sys_path(gl_path.parent)
    utility_path = pathlib.Path(__file__).parents[6] / "Libraries" / "Utility" / "src" / "utility"
    if utility_path.exists():
        add_sys_path(utility_path.parent)
    toolset_path = pathlib.Path(__file__).parents[3] / "toolset"
    if toolset_path.exists():
        add_sys_path(toolset_path.parent)


K1_PATH = os.environ.get("K1_PATH")
K2_PATH = os.environ.get("K2_PATH")

from pykotor.common.stream import BinaryReader
from pykotor.extract.installation import Installation
from pykotor.resource.formats.bwm.bwm_auto import read_bwm
from pykotor.resource.type import ResourceType


@unittest.skipIf(
    not K2_PATH or not pathlib.Path(K2_PATH).joinpath("chitin.key").exists(),
    "K2_PATH environment variable is not set or not found on disk.",
)
@unittest.skipIf(
    QTest is None or not QApplication,
    "PyQt5 is required, please run pip install -r requirements.txt before running this test.",
)
class BWMEditorTest(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        # Make sure to configure this environment path before testing!
        from toolset.gui.editors.bwm import BWMEditor
        cls.BWMEditor = BWMEditor
        from toolset.data.installation import HTInstallation
        #cls.INSTALLATION = HTInstallation(K1_PATH, "", tsl=False, mainWindow=None)
        cls.K2_INSTALLATION = HTInstallation(K2_PATH, "", tsl=True, mainWindow=None)

    def setUp(self) -> None:
        self.app = QApplication([])
        self.editor = self.BWMEditor(None, self.K2_INSTALLATION)
        self.log_messages: list[str] = [os.linesep]

    def tearDown(self) -> None:
        self.app.deleteLater()

    def log_func(self, *args):
        self.log_messages.append("\t".join(args))

    def test_save_and_load(self):
        filepath = TESTS_FILES_PATH / "zio006j.wok"

        data = BinaryReader.load_file(filepath)
        old = read_bwm(data)
        supported = [ResourceType.WOK, ResourceType.DWK, ResourceType.PWK]
        self.editor.load(filepath, "zio006j", ResourceType.WOK, data)

        data, _ = self.editor.build()
        new = read_bwm(data)

        self.assertDeepEqual(old, new)

    @unittest.skipIf(
        not K1_PATH or not pathlib.Path(K1_PATH).joinpath("chitin.key").exists(),
        "K1_PATH environment variable is not set or not found on disk.",
    )
    def test_bwm_reconstruct_from_k1_installation(self) -> None:
        self.installation = Installation(K1_PATH)  # type: ignore[arg-type]
        for bwm_resource in (resource for resource in self.installation if resource.restype() in [ResourceType.WOK, ResourceType.DWK, ResourceType.PWK]):
            old = read_bwm(bwm_resource.data())
            self.editor.load(bwm_resource.filepath(), bwm_resource.resname(), bwm_resource.restype(), bwm_resource.data())

            data, _ = self.editor.build()
            new = read_bwm(data)

            self.assertDeepEqual(old, new)

    @unittest.skipIf(
        not K2_PATH or not pathlib.Path(K2_PATH).joinpath("chitin.key").exists(),
        "K2_PATH environment variable is not set or not found on disk.",
    )
    def test_bwm_reconstruct_from_k2_installation(self) -> None:
        self.installation = Installation(K2_PATH)  # type: ignore[arg-type]
        for bwm_resource in (resource for resource in self.installation if resource.restype() in [ResourceType.WOK, ResourceType.DWK, ResourceType.PWK]):
            old = read_bwm(bwm_resource.data())
            self.editor.load(bwm_resource.filepath(), bwm_resource.resname(), bwm_resource.restype(), bwm_resource.data())

            data, _ = self.editor.build()
            new = read_bwm(data)

            self.assertDeepEqual(old, new)

    def assertDeepEqual(self, obj1, obj2, context=''):
        if isinstance(obj1, dict) and isinstance(obj2, dict):
            self.assertEqual(set(obj1.keys()), set(obj2.keys()), context)
            for key in obj1:
                new_context = f"{context}.{key}" if context else str(key)
                self.assertDeepEqual(obj1[key], obj2[key], new_context)

        elif isinstance(obj1, (list, tuple)) and isinstance(obj2, (list, tuple)):
            self.assertEqual(len(obj1), len(obj2), context)
            for index, (item1, item2) in enumerate(zip(obj1, obj2)):
                new_context = f"{context}[{index}]" if context else f"[{index}]"
                self.assertDeepEqual(item1, item2, new_context)

        elif hasattr(obj1, '__dict__') and hasattr(obj2, '__dict__'):
            self.assertDeepEqual(obj1.__dict__, obj2.__dict__, context)

        else:
            self.assertEqual(obj1, obj2, context)

    def test_placeholder(self):
        ...


if __name__ == "__main__":
    unittest.main()
