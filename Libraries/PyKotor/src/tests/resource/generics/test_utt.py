import os
import pathlib
import sys
from unittest import TestCase
import unittest

from pykotor.resource.formats.gff.gff_data import GFF
from pykotor.resource.type import ResourceType


THIS_SCRIPT_PATH = pathlib.Path(__file__)
PYKOTOR_PATH = THIS_SCRIPT_PATH.parents[3].resolve()
UTILITY_PATH = THIS_SCRIPT_PATH.parents[5].joinpath("Utility", "src").resolve()
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

from pykotor.common.misc import Game
from pykotor.resource.formats.gff import read_gff
from pykotor.resource.generics.utt import UTT, construct_utt, dismantle_utt
from pykotor.extract.installation import Installation

TEST_FILE = "src/tests/files/test.utt"

K1_PATH = os.environ.get("K1_PATH")
K2_PATH = os.environ.get("K2_PATH")


class TestUTT(TestCase):
    def setUp(self):
        self.log_messages = [os.linesep]

    def log_func(self, *msgs):
        self.log_messages.append("\t".join(msgs))

    @unittest.skipIf(
        not K1_PATH or not pathlib.Path(K1_PATH).joinpath("chitin.key").exists(),
        "K1_PATH environment variable is not set or not found on disk.",
    )
    def test_gff_reconstruct_from_k1_installation(self) -> None:
        self.installation = Installation(K1_PATH)  # type: ignore[arg-type]
        for resource in (resource for resource in self.installation if resource.restype() == ResourceType.UTT):
            gff: GFF = read_gff(resource.data())
            reconstructed_gff: GFF = dismantle_utt(construct_utt(gff), Game.K1)
            self.assertTrue(gff.compare(reconstructed_gff, self.log_func, ignore_default_changes=True), os.linesep.join(self.log_messages))

    @unittest.skipIf(
        not K2_PATH or not pathlib.Path(K2_PATH).joinpath("chitin.key").exists(),
        "K2_PATH environment variable is not set or not found on disk.",
    )
    def test_gff_reconstruct_from_k2_installation(self) -> None:
        self.installation = Installation(K2_PATH)  # type: ignore[arg-type]
        for resource in (resource for resource in self.installation if resource.restype() == ResourceType.UTT):
            gff: GFF = read_gff(resource.data())
            reconstructed_gff: GFF = dismantle_utt(construct_utt(gff))
            self.assertTrue(gff.compare(reconstructed_gff, self.log_func, ignore_default_changes=True), os.linesep.join(self.log_messages))

    def test_gff_reconstruct(self) -> None:
        gff = read_gff(TEST_FILE)
        reconstructed_gff = dismantle_utt(construct_utt(gff))
        self.assertTrue(gff.compare(reconstructed_gff, self.log_func), os.linesep.join(self.log_messages))

    def test_io_construct(self):
        gff = read_gff(TEST_FILE)
        utt = construct_utt(gff)
        self.validate_io(utt)

    def test_io_reconstruct(self):
        gff = read_gff(TEST_FILE)
        gff = dismantle_utt(construct_utt(gff))
        utt = construct_utt(gff)
        self.validate_io(utt)

    def validate_io(self, utt: UTT):
        self.assertEqual("GenericTrigger001", utt.tag)
        self.assertEqual("generictrigge001", utt.resref)
        self.assertEqual(42968, utt.name.stringref)
        self.assertEqual(1, utt.auto_remove_key)
        self.assertEqual(1, utt.faction_id)
        self.assertEqual(1, utt.cursor_id)
        self.assertEqual(3.0, utt.highlight_height)
        self.assertEqual("somekey", utt.key_name)
        self.assertEqual(0, utt.loadscreen_id)
        self.assertEqual(0, utt.portrait_id)
        self.assertEqual(1, utt.type_id)
        self.assertEqual(1, utt.trap_detectable)
        self.assertEqual(10, utt.trap_detect_dc)
        self.assertEqual(1, utt.trap_disarmable)
        self.assertEqual(10, utt.trap_disarm_dc)
        self.assertEqual(1, utt.is_trap)
        self.assertEqual(1, utt.trap_once)
        self.assertEqual(1, utt.trap_type)
        self.assertEqual("ondisarm", utt.on_disarm)
        self.assertEqual("ontraptriggered", utt.on_trap_triggered)
        self.assertEqual("onclick", utt.on_click)
        self.assertEqual("onheartbeat", utt.on_heartbeat)
        self.assertEqual("onenter", utt.on_enter)
        self.assertEqual("onexit", utt.on_exit)
        self.assertEqual("onuserdefined", utt.on_user_defined)
        self.assertEqual(6, utt.palette_id)
        self.assertEqual("comment", utt.comment)
