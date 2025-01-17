import os
import pathlib
import sys
import unittest

THIS_SCRIPT_PATH = pathlib.Path(__file__)
PYKOTOR_PATH = THIS_SCRIPT_PATH.parents[2].resolve()
UTILITY_PATH = THIS_SCRIPT_PATH.parents[4].joinpath("Utility", "src").resolve()
if PYKOTOR_PATH.exists():
    working_dir = str(PYKOTOR_PATH)
    if working_dir in sys.path:
        sys.path.remove(working_dir)
        os.chdir(PYKOTOR_PATH.parent)
    sys.path.insert(0, working_dir)
if UTILITY_PATH.exists():
    working_dir = str(UTILITY_PATH)
    if working_dir in sys.path:
        sys.path.remove(working_dir)
    sys.path.insert(0, working_dir)

from pykotor.common.language import Language
from pykotor.tools.encoding import decode_bytes_with_fallbacks

try:
    import charset_normalizer
except ImportError:
    charset_normalizer = None


class TestDecodeBytes(unittest.TestCase):

    def test_basic(self):  # sourcery skip: class-extract-method
        byte_str = b"hello world"
        result = decode_bytes_with_fallbacks(byte_str)
        self.assertEqual(result, "hello world")

    def test_non_ascii(self):
        byte_str = b"h\xc3\xa9llo w\xc3\xb6rld"
        result = decode_bytes_with_fallbacks(byte_str)
        self.assertEqual(result, "héllo wörld")

    def test_unknown_encoding(self):
        byte_str = b"\x80\x81\x82"
        with self.assertRaises(UnicodeDecodeError):
            byte_str.decode()
        result = byte_str.decode(errors="replace")
        self.assertEqual(result, "���")
        result = decode_bytes_with_fallbacks(byte_str, errors="replace")
        self.assertEqual(result, "Øab")

    def test_bom(self):
        byte_str = b"\xef\xbb\xbfhello world"
        result = byte_str.decode("utf-8-sig")
        self.assertEqual(result, "hello world")
        result = decode_bytes_with_fallbacks(byte_str)
        self.assertEqual(result, "hello world")

    def test_errors_replace(self):
        byte_str = b"h\xc3\xa9llo"
        #self.assertEqual(byte_str.decode(errors="replace"), "h?llo")
        self.assertEqual(byte_str.decode(errors="replace"), "héllo")

        result = decode_bytes_with_fallbacks(byte_str, errors="replace")
        self.assertEqual(result, "héllo")

    def test_known_encoding(self):
        byte_content = b"Hello, World!"
        errors = "strict"
        encoding = "utf-8"
        lang = None
        only_8bit_encodings = False
        expected_result = "Hello, World!"

        result = decode_bytes_with_fallbacks(byte_content, errors, encoding, lang, only_8bit_encodings)
        self.assertEqual(result, expected_result)

    def test_language_provided(self):
        byte_content = b"Bonjour le monde!"
        errors = "strict"
        encoding = None
        lang = Language.FRENCH
        only_8bit_encodings = False
        expected_result = "Bonjour le monde!"

        result = decode_bytes_with_fallbacks(byte_content, errors, encoding, lang, only_8bit_encodings)
        self.assertEqual(result, expected_result)

    def test_language_detect(self):
        byte_content = b"Bonjour le monde!"
        errors = "strict"
        encoding = None
        lang = Language.UNKNOWN
        only_8bit_encodings = False
        expected_result = "Bonjour le monde!"

        result = decode_bytes_with_fallbacks(byte_content, errors, encoding, lang, only_8bit_encodings)
        self.assertEqual(result, expected_result)

    def test_invalid_bytes_for_encoding(self):
        byte_content = b"\xff\xfe\x00"
        errors = "replace"
        encoding = "utf-8"
        lang = None
        only_8bit_encodings = False
        expected_result = "\ufffd\ufffd"
        result = byte_content.decode(encoding, errors)
        self.assertEqual(result, "��\x00")

        result = decode_bytes_with_fallbacks(byte_content, errors, encoding, lang, only_8bit_encodings)
        self.assertEqual(result, "��\x00")

    def test_fallback_to_detected_encoding(self):
        byte_content = b"\xc2\xa1Hola!"
        errors = "strict"
        encoding = None
        lang = None
        only_8bit_encodings = False
        expected_result = "¡Hola!"
        exp = "癒Hola!"
        exp2 = "Â¡Hola!"

        result = byte_content.decode(errors=errors)
        self.assertEqual(result, expected_result)
        result = decode_bytes_with_fallbacks(byte_content, errors, encoding, lang, only_8bit_encodings)
        self.assertEqual(result, exp if charset_normalizer is None else exp2)

    def test_8bit_encoding_only(self):
        byte_content = b"\xe4\xf6\xfc"
        errors = "strict"
        encoding = None
        lang = None
        only_8bit_encodings = True
        expected_result = "���"
        exp = "U6Ü"
        exp2 = "дць"

        result = byte_content.decode(errors="replace")
        self.assertEqual(result, expected_result)
        result = decode_bytes_with_fallbacks(byte_content, errors, encoding, lang, only_8bit_encodings)
        self.assertEqual(result, exp if charset_normalizer is None else exp2)

    def test_with_BOM_included(self):
        byte_content = b"\xef\xbb\xbfTest"
        errors = "strict"
        encoding = None
        lang = None
        only_8bit_encodings = False
        expected_result = "Test"

        result = decode_bytes_with_fallbacks(byte_content, errors, encoding, lang, only_8bit_encodings)
        self.assertEqual(result, expected_result)

    def test_undetectable_encoding_replace_errors(self):
        byte_content = b"\x80\x81\x82"
        errors = "replace"
        encoding = None
        lang = None
        only_8bit_encodings = False
        expected_result = "\ufffd\ufffd\ufffd"
        exp = "Øab"

        result = byte_content.decode(errors=errors)
        self.assertEqual(result, expected_result)
        result = decode_bytes_with_fallbacks(byte_content, errors, encoding, lang, only_8bit_encodings)
        self.assertEqual(result, exp)

    def test_strict_error_handling_decoding_failure(self):
        byte_content = b"\x80\x81\x82"
        errors = "strict"
        encoding = "ascii"
        lang = None
        only_8bit_encodings = False
        expected_result = "Øab"
        with self.assertRaises(UnicodeDecodeError):
            decode_bytes_with_fallbacks(byte_content, errors, encoding, lang, only_8bit_encodings)
            byte_content.decode(errors=errors)
        result = decode_bytes_with_fallbacks(byte_content, errors, encoding, lang, only_8bit_encodings)
        self.assertEqual(result, expected_result)

    def test_no_valid_encoding_found_strict_errors(self):
        byte_content = b"\x80\x81\x82"
        errors = "strict"
        encoding = None
        lang = None
        only_8bit_encodings = False
        expected_result = "Øab"
        with self.assertRaises(UnicodeDecodeError):
            byte_content.decode(errors=errors)
        result = decode_bytes_with_fallbacks(byte_content, errors, encoding, lang, only_8bit_encodings)
        self.assertEqual(result, expected_result)

