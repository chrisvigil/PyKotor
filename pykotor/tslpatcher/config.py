from __future__ import annotations

from configparser import ConfigParser
from enum import IntEnum
from typing import TYPE_CHECKING

from chardet import UniversalDetector

from pykotor.common.stream import BinaryReader, BinaryWriter
from pykotor.extract.capsule import Capsule
from pykotor.extract.file import ResourceIdentifier
from pykotor.extract.installation import Installation, SearchLocation
from pykotor.resource.formats.erf import ERF, read_erf, write_erf
from pykotor.resource.formats.erf.erf_data import ERFType
from pykotor.resource.formats.gff import read_gff
from pykotor.resource.formats.gff.gff_auto import bytes_gff
from pykotor.resource.formats.ncs.ncs_auto import bytes_ncs, compile_nss
from pykotor.resource.formats.rim import RIM, read_rim, write_rim
from pykotor.resource.formats.ssf import read_ssf, write_ssf
from pykotor.resource.formats.tlk import read_tlk, write_tlk
from pykotor.resource.formats.twoda import read_2da, write_2da
from pykotor.tools.misc import is_capsule_file, is_mod_file, is_rim_file
from pykotor.tools.path import CaseAwarePath
from pykotor.tslpatcher.logger import PatchLogger
from pykotor.tslpatcher.memory import PatcherMemory
from pykotor.tslpatcher.mods.install import InstallFile, InstallFolder
from pykotor.tslpatcher.mods.tlk import ModificationsTLK

if TYPE_CHECKING:
    from pykotor.resource.formats.twoda.twoda_data import TwoDA
    from pykotor.tslpatcher.mods.gff import ModificationsGFF
    from pykotor.tslpatcher.mods.nss import ModificationsNSS
    from pykotor.tslpatcher.mods.ssf import ModificationsSSF
    from pykotor.tslpatcher.mods.twoda import Modifications2DA


class LogLevel(IntEnum):
    # Docstrings taken from ChangeEdit docs

    NOTHING = 0
    """No feedback at all. The text from "info.rtf" will continue to be displayed during installation"""

    GENERAL = 1
    """Only general progress information will be displayed. Not recommended."""

    ERRORS = 2
    """General progress information is displayed, along with any serious errors encountered."""

    WARNINGS = 3
    """General progress information, serious errors and warnings are displayed. This is
    recommended for the release version of your mod."""

    FULL = 4
    """Full feedback. On top of what is displayed at level 3, it also shows verbose progress
    information that may be useful for a Modder to see what is happening. Intended for
    Debugging."""


class PatcherConfig:
    def __init__(self):
        self.window_title: str = ""
        self.confirm_message: str = ""
        self.game_number: int | None = None

        self.required_file: str | None = None
        self.required_message: str = ""

        self.install_list: list[InstallFolder] = []
        self.patches_2da: list[Modifications2DA] = []
        self.patches_gff: list[ModificationsGFF] = []
        self.patches_ssf: list[ModificationsSSF] = []
        self.patches_nss: list[ModificationsNSS] = []
        self.patches_tlk: ModificationsTLK = ModificationsTLK()

    def load(self, ini_text: str, mod_path: CaseAwarePath | str) -> None:
        from pykotor.tslpatcher.reader import ConfigReader

        ini = ConfigParser(
            delimiters=("="),
            allow_no_value=True,
            strict=False,
            interpolation=None,
        )
        ini.optionxform = str  # type: ignore[reportGeneralTypeIssues]  # use case sensitive keys
        ini.read_string(ini_text)

        ConfigReader(ini, CaseAwarePath(mod_path)).load(self)

    def patch_count(self) -> int:
        return (
            len(self.patches_2da)
            + len(self.patches_gff)
            + len(self.patches_ssf)
            + 1
            + len(self.install_list)
            + len(self.patches_nss)
        )


class PatcherNamespace:
    def __init__(self):
        self.namespace_id: str = ""
        self.ini_filename: str = ""
        self.info_filename: str = ""
        self.data_folderpath: str = ""
        self.name: str = ""
        self.description: str = ""


class ModInstaller:
    def __init__(
        self,
        mod_path: CaseAwarePath,
        game_path: CaseAwarePath,
        ini_file: str,
        logger: PatchLogger | None = None,
    ):
        self.game_path: CaseAwarePath = game_path
        self.mod_path: CaseAwarePath = mod_path
        self.ini_file: str = ini_file
        self.output_path: CaseAwarePath = game_path
        self.log: PatchLogger = PatchLogger() if logger is None else logger

        self._config: PatcherConfig | None = None

    def config(self) -> PatcherConfig:
        """
        Returns the PatcherConfig object associated with the mod installer. The object is created when the method is
        first called then cached for future calls.
        """
        if self._config is None:
            ini_file_bytes = BinaryReader.load_file(self.mod_path / self.ini_file)

            detector = UniversalDetector()
            detector.feed(ini_file_bytes)
            detector.close()
            encoding = detector.result["encoding"]
            assert encoding is not None

            ini_text = ini_file_bytes.decode(encoding)
            self._config = PatcherConfig()
            self._config.load(ini_text, self.mod_path)

        return self._config

    # extract into multiple funcs perhaps?
    def install(self) -> None:
        config = self.config()

        installation = Installation(self.game_path)
        memory = PatcherMemory()
        twodas = {}
        soundsets = {}
        templates = {}

        # Apply changes to dialog.tlk
        if len(config.patches_tlk.modifiers) > 0:
            dialog_tlk = read_tlk(installation.path() / "dialog.tlk")
            config.patches_tlk.apply(dialog_tlk, memory)
            write_tlk(dialog_tlk, str(self.output_path / "dialog.tlk"))
            self.log.complete_patch()

        # Move nwscript.nss to Override if there are any nss patches to do
        if len(config.patches_nss) > 0:
            folder_install = InstallFolder("Override")
            if folder_install not in config.install_list:
                config.install_list.append(folder_install)
            file_install = InstallFile("nwscript.nss", True)
            folder_install.files.append(file_install)

        # Apply changes from [InstallList]
        for folder in config.install_list:
            folder.apply(self.log, self.mod_path, self.output_path)
            self.log.complete_patch()

        # Apply changes to 2DA files
        for twoda_patch in config.patches_2da:
            resname, restype = ResourceIdentifier.from_path(twoda_patch.filename)
            search = installation.resource(
                resname,
                restype,
                [SearchLocation.OVERRIDE, SearchLocation.CUSTOM_FOLDERS],
                folders=[self.mod_path],
            )
            if search is None or search.data is None:
                self.log.add_error(
                    f"Didn't patch '{twoda_patch.filename}' because search data is `None`.",
                )
                continue
            twoda: TwoDA = read_2da(search.data)
            twodas[twoda_patch.filename] = twoda

            self.log.add_note(f"Patching '{twoda_patch.filename}'")
            twoda_patch.apply(twoda, memory)
            write_2da(twoda, str(self.output_path / "Override" / twoda_patch.filename))

            self.log.complete_patch()

        # Apply changes to SSF files
        for ssf_patch in config.patches_ssf:
            resname, restype = ResourceIdentifier.from_path(ssf_patch.filename)
            search = installation.resource(
                resname,
                restype,
                [SearchLocation.OVERRIDE, SearchLocation.CUSTOM_FOLDERS],
                folders=[self.mod_path],
            )
            if search is None or search.data is None:
                self.log.add_error(
                    f"Didn't patch '{ssf_patch.filename}' because search data is `None`.",
                )
                continue

            soundset = soundsets[ssf_patch.filename] = read_ssf(search.data)

            self.log.add_note(f"Patching '{ssf_patch.filename}'")
            ssf_patch.apply(soundset, memory)
            write_ssf(soundset, self.output_path / "Override" / ssf_patch.filename)

            self.log.complete_patch()

        # Apply changes to GFF files
        for gff_patch in config.patches_gff:
            resname, restype = ResourceIdentifier.from_path(gff_patch.filename)

            capsule = None
            gff_filepath: CaseAwarePath = self.output_path / gff_patch.destination
            if is_capsule_file(gff_patch.destination.name):
                capsule = Capsule(gff_filepath)

            search = installation.resource(
                resname,
                restype,
                [
                    SearchLocation.OVERRIDE,
                    SearchLocation.CUSTOM_FOLDERS,
                    SearchLocation.CUSTOM_MODULES,
                ],
                folders=[self.mod_path],
                capsules=[] if capsule is None else [capsule],
            )
            if search is None or search.data is None:
                self.log.add_error(
                    f"Didn't patch '{gff_patch.filename}' because search data is `None`.",
                )
                continue

            norm_game_path = installation.path()
            norm_file_path_rel = CaseAwarePath(gff_patch.destination)
            norm_file_path = norm_game_path / norm_file_path_rel
            local_path = norm_file_path.relative_to(norm_game_path)

            if capsule is None:
                self.log.add_note(
                    f"Patching '{gff_patch.filename}' in the '{local_path.parent}' folder.",
                )
            else:
                self.log.add_note(
                    f"Patching '{gff_patch.filename}' in the '{local_path}' archive.",
                )

            template = templates[gff_patch.filename] = read_gff(search.data)
            assert template is not None

            gff_patch.apply(template, memory, self.log)
            self.write(
                gff_filepath,
                gff_patch.filename,
                bytes_gff(template),
                replace=True,
            )

            self.log.complete_patch()

        # Apply changes to NSS files
        for nss_patch in config.patches_nss:
            capsule = None
            nss_output_filepath = self.output_path / nss_patch.destination
            if is_capsule_file(nss_patch.destination):
                capsule = Capsule(nss_output_filepath)

            nss_input_filepath = CaseAwarePath(self.mod_path, nss_patch.filename)
            nss = [BinaryReader.load_file(nss_input_filepath).decode(errors="ignore")]

            norm_game_path = installation.path()
            norm_file_path_rel = CaseAwarePath(nss_patch.destination)
            norm_file_path = norm_game_path / norm_file_path_rel
            local_path = norm_file_path.relative_to(norm_game_path)
            local_folder = local_path.parent

            if capsule is None:
                self.log.add_note(
                    f"Patching '{nss_patch.filename}' in the '{local_folder}' folder.",
                )
            else:
                self.log.add_note(
                    f"Patching '{nss_patch.filename}' in the '{local_path}' archive.",
                )

            self.log.add_note(f"Compiling '{nss_patch.filename}'")
            nss_patch.apply(nss, memory, self.log)

            data = bytes_ncs(compile_nss(nss[0], installation.game()))
            file_name, ext = nss_patch.filename.split(".", 1)

            self.write(
                nss_output_filepath,
                f"{file_name}." + ext.lower().replace("nss", "ncs"),
                data,
                nss_patch.replace_file,
            )

            self.log.complete_patch()

    def write(
        self,
        destination: CaseAwarePath,
        filename: str,
        data: bytes,
        replace: bool = False,
    ) -> None:
        resname, restype = ResourceIdentifier.from_path(filename)
        file_extension = destination.suffix
        if is_rim_file(destination.name):
            rim = read_rim(BinaryReader.load_file(destination)) if destination.exists() else RIM()
            if not rim.get(resname, restype) or replace:
                rim.set(resname, restype, data)
                write_rim(rim, destination)
        elif is_mod_file(destination.name):
            erf = (
                read_erf(BinaryReader.load_file(destination))
                if destination.exists()
                else ERF(ERFType.from_extension(file_extension))
            )
            if not erf.get(resname, restype) or replace:
                erf.set(resname, restype, data)
                write_erf(erf, str(destination))
        elif not destination.exists() or replace:
            BinaryWriter.dump(destination, data)
