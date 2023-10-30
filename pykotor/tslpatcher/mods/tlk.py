from __future__ import annotations

from typing import TYPE_CHECKING

from pykotor.resource.formats.tlk.tlk_auto import bytes_tlk, read_tlk
from pykotor.tools.path import PurePath

if TYPE_CHECKING:
    from pykotor.common.misc import Game, ResRef
    from pykotor.resource.formats.tlk import TLK
    from pykotor.resource.type import SOURCE_TYPES
    from pykotor.tslpatcher.logger import PatchLogger
    from pykotor.tslpatcher.memory import PatcherMemory


class ModificationsTLK:
    def __init__(self, filename: str = "dialog.tlk", destination: str = "."):
        self.modifiers: list[ModifyTLK] = []
        self.filename: PurePath = PurePath(filename)
        self.destination = destination

    def apply(self, source_tlk: SOURCE_TYPES, memory: PatcherMemory, log: PatchLogger | None = None, game: Game | None = None) -> bytes:
        dialog = read_tlk(source_tlk)
        for modifier in self.modifiers:
            if modifier.is_replacement:
                modifier.replace(dialog, memory)
            else:
                modifier.insert(dialog, memory)
            if log:
                log.complete_patch()
        return bytes_tlk(dialog)


class ModifyTLK:
    def __init__(
        self,
        token_id: int,
        text: str,
        sound: ResRef,
        is_replacement: bool = False,
    ):
        self.token_id: int = token_id
        self.text: str = text
        self.sound: ResRef = sound
        self.is_replacement: bool = is_replacement

    def insert(self, dialog: TLK, memory: PatcherMemory) -> None:
        dialog.add(self.text, self.sound.get())
        memory.memory_str[self.token_id] = len(dialog.entries) - 1

    def replace(self, dialog: TLK, memory: PatcherMemory) -> None:
        dialog.replace(self.token_id, self.text, self.sound.get())
        memory.memory_str[self.token_id] = self.token_id
