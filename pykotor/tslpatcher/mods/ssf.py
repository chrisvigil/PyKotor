from __future__ import annotations

from typing import TYPE_CHECKING

from pykotor.resource.formats.ssf import bytes_ssf, read_ssf

if TYPE_CHECKING:
    from pykotor.resource.formats.ssf import SSF, SSFSound
    from pykotor.resource.type import SOURCE_TYPES
    from pykotor.tslpatcher.memory import PatcherMemory, TokenUsage


class ModifySSF:
    def __init__(self, sound: SSFSound, stringref: TokenUsage):
        self.sound: SSFSound = sound
        self.stringref: TokenUsage = stringref

    def apply(self, ssf: SSF, memory: PatcherMemory) -> None:
        ssf.set_data(self.sound, int(self.stringref.value(memory)))


class ModificationsSSF:
    def __init__(
        self,
        filename: str,
        replace_file: bool,
        modifiers: list[ModifySSF] | None = None,
    ):
        self.filename: str = filename
        self.destination = "Override"
        self.replace_file: bool = replace_file
        self.no_replacefile_check = True
        self.modifiers: list[ModifySSF] = modifiers if modifiers is not None else []

    def apply(self, source_ssf: SOURCE_TYPES, memory: PatcherMemory, log=None, game=None) -> bytes:
        ssf: SSF = read_ssf(source_ssf)
        for modifier in self.modifiers:
            modifier.apply(ssf, memory)
        return bytes_ssf(ssf)
