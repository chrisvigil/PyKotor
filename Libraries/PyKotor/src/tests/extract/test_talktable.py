import pathlib
import sys

if getattr(sys, "frozen", False) is False:
    pykotor_path = pathlib.Path(__file__).parents[2] / "pykotor"
    print(pykotor_path)
    if pykotor_path.exists():
        working_dir = str(pykotor_path.parent)
        if working_dir in sys.path:
            sys.path.remove(working_dir)
        sys.path.insert(0, str(pykotor_path.parent))

import unittest

from pykotor.common.language import Language
from pykotor.extract.talktable import TalkTable

TEST_FILE = "src/tests/files/test.tlk"


class TestTalkTable(unittest.TestCase):
    def test_size(self):
        talktable = TalkTable(TEST_FILE)
        self.assertEqual(3, talktable.size())

    def test_string(self):
        talktable = TalkTable(TEST_FILE)
        self.assertEqual("abcdef", talktable.string(0))
        self.assertEqual("ghijklmnop", talktable.string(1))
        self.assertEqual("qrstuvwxyz", talktable.string(2))
        self.assertEqual("", talktable.string(-1))
        self.assertEqual("", talktable.string(3))

    def test_voiceover(self):
        talktable = TalkTable(TEST_FILE)
        self.assertEqual("resref01", talktable.sound(0))
        self.assertEqual("resref02", talktable.sound(1))
        self.assertEqual("", talktable.sound(2))
        self.assertEqual("", talktable.sound(-1))
        self.assertEqual("", talktable.sound(3))

    def test_batch(self):
        talktable = TalkTable(TEST_FILE)
        batch = talktable.batch([2, 0, -1, 3])
        self.assertEqual(("abcdef", "resref01"), batch[0])
        self.assertEqual(("qrstuvwxyz", ""), batch[2])
        self.assertEqual(("", ""), batch[-1])
        self.assertEqual(("", ""), batch[3])

    def test_language(self):
        talktable = TalkTable(TEST_FILE)
        self.assertEqual(talktable.language(), Language.ENGLISH)

if __name__ == "__main__":
    unittest.main()