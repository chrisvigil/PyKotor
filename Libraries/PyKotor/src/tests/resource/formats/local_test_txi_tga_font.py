import pathlib
import sys
import unittest
from tempfile import TemporaryDirectory

from PIL import Image

if getattr(sys, "frozen", False) is False:
    pykotor_path = pathlib.Path(__file__).parents[3] / "pykotor"
    if pykotor_path.exists():
        working_dir = str(pykotor_path.parent)
        if working_dir in sys.path:
            sys.path.remove(working_dir)
        sys.path.insert(0, str(pykotor_path.parent))

from pykotor.common.language import Language
from pykotor.resource.formats.tpc.txi_data import write_bitmap_font, write_bitmap_fonts
from utility.path import Path

FONT_PATH_FILE = Path("src/tests/files/roboto/Roboto-Black.ttf")
CHINESE_FONT_PATH_FILE = Path("src/tests/files/chinese_simplified_ttf/Unifontexmono-AL3RA.ttf")
THAI_FONT_PATH_FILE = Path("src/tests/files/TH Sarabun New Regular/TH Sarabun New Regular.ttf")


class TestWriteBitmapFont(unittest.TestCase):
    def setUp(self):
        self.output_path = Path(TemporaryDirectory().name)
        self.output_path.mkdir(exist_ok=True)
    def cleanUp(self):
        self.output_path.unlink()
    def test_bitmap_font(self):
        write_bitmap_fonts(self.output_path, r"C:\Windows\Fonts\Inkfree.ttf", (2048, 2048), Language.ENGLISH, draw_box=False, custom_scaling=1.0)
    def test_bitmap_font_chinese(self):
        write_bitmap_font(self.output_path / "test_font_chinese.tga", CHINESE_FONT_PATH_FILE, (10240,10240), Language.CHINESE_SIMPLIFIED)
    def test_bitmap_font_thai(self):
        write_bitmap_font(self.output_path / "test_font_thai.tga", THAI_FONT_PATH_FILE, (2048,2048), Language.THAI, draw_box=True)
    def test_valid_inputs(self) -> None:
        # Test with valid inputs
        target_path = Path("output/font.tga").resolve()
        resolution = (2048, 2048)
        lang = Language.ENGLISH

        write_bitmap_font(target_path, FONT_PATH_FILE, resolution, lang)

        # Verify output files were generated
        self.assertTrue(target_path.exists())
        self.assertTrue(target_path.with_suffix(".txi").exists())

        # Verify image file
        img = Image.open(target_path)
        self.assertEqual(img.size, resolution)
        self.assertEqual(img.mode, "RGBA")
        img.close()

    def test_invalid_font_path(self):
        # Test with invalid font path
        font_path = "invalid.ttf"
        target_path = self.output_path / "font.tga"
        resolution = (256, 256)
        lang = Language.ENGLISH

        with self.assertRaises(OSError):
            write_bitmap_font(target_path, font_path, resolution, lang)

    def test_invalid_language(self):
        # Test with invalid language
        target_path = self.output_path / "font.tga"
        resolution = (256, 256)
        lang = "invalid"

        with self.assertRaises((AttributeError, ValueError)):
            write_bitmap_font(target_path, FONT_PATH_FILE, resolution, lang)  # type: ignore[reportGeneralTypeIssues]

    def test_invalid_resolution(self):
        # Test with invalid resolution
        target_path = self.output_path / "font.tga"
        resolution = (0, 0)
        lang = Language.ENGLISH

        with self.assertRaises(ZeroDivisionError):
            write_bitmap_font(target_path, FONT_PATH_FILE, resolution, lang)

# Edge cases:
# - Resolution is very small or very large
# - Font file contains lots of glyphs
# - Language uses complex script

if __name__ == "__main__":
    unittest.main()