from __future__ import annotations

import argparse
import hashlib
import io
import os
from typing import TYPE_CHECKING

from pykotor.resource.formats.erf import read_erf
from pykotor.resource.formats.gff import GFFContent, read_gff
from pykotor.resource.formats.tlk import read_tlk
from pykotor.resource.formats.twoda import read_2da
from pykotor.tools.misc import is_erf_or_mod_file
from pykotor.tools.path import CaseAwarePath, PureWindowsPath
from pykotor.tslpatcher.diff.gff import DiffGFF
from pykotor.tslpatcher.diff.tlk import DiffTLK
from pykotor.tslpatcher.diff.twoda import Diff2DA

if TYPE_CHECKING:
    from pykotor.resource.formats.erf import ERFResource
    from pykotor.resource.formats.gff import GFF
    from pykotor.resource.formats.tlk import TLK


def log_output(*args, **kwargs) -> None:
    # Create an in-memory text stream
    buffer = io.StringIO()

    # Print to the in-memory stream
    print(*args, file=buffer, **kwargs)

    # Retrieve the printed content
    msg = buffer.getvalue()

    # Write the captured output to the file
    with args.output_log.open("a") as f:
        f.write(msg)

    # Print the captured output to console
    print(*args, **kwargs)  # noqa: T201


def compute_sha256(where: os.PathLike | str | bytes):
    """Compute the SHA-256 hash of the data."""
    if isinstance(where, bytes):
        return compute_sha256_from_bytes(where)
    if isinstance(where, (os.PathLike | str)):
        file_path = CaseAwarePath(where)
        return compute_sha256_from_path(file_path)
    return None


def compute_sha256_from_path(file_path: CaseAwarePath) -> str:
    """Compute the SHA-256 hash of a file."""
    sha256 = hashlib.sha256()

    with file_path.open("rb") as f:
        while True:
            data = f.read(65536)  # read in 64k chunks
            if not data:
                break
            sha256.update(data)

    return sha256.hexdigest()


def compute_sha256_from_bytes(data: bytes) -> str:
    """Compute the SHA-256 hash of bytes data."""
    sha256 = hashlib.sha256()
    sha256.update(data)
    return sha256.hexdigest()


def relative_path_from_to(src, dst) -> CaseAwarePath:
    src_parts = list(src.parts)
    dst_parts = list(dst.parts)

    common_length = next(
        (i for i, (src_part, dst_part) in enumerate(zip(src_parts, dst_parts)) if src_part != dst_part),
        len(src_parts),
    )
    # ".." for each diverging part of src, and then the remaining parts of dst
    rel_parts = [".."] * (len(src_parts) - common_length) + dst_parts[common_length:]
    return CaseAwarePath(*rel_parts)


def visual_length(s: str, tab_length=8) -> int:
    # Split the string at tabs, sum the lengths of the substrings,
    # and add the necessary spaces to account for the tab stops.
    parts = s.split("\t")
    vis_length = sum(len(part) for part in parts)
    for part in parts[:-1]:  # all parts except the last one
        vis_length += tab_length - (len(part) % tab_length)
    return vis_length


gff_types = [x.value.lower().strip() for x in GFFContent]


def diff_data(
    data1: bytes | os.PathLike | str,
    data2: bytes | os.PathLike | str,
    file1_rel: CaseAwarePath,
    file2_rel: CaseAwarePath,
    ext: str,
    resname: str | None = None,
) -> bool | None:
    where = PureWindowsPath(file1_rel.name, f"{resname}.{ext}") if resname else file1_rel.name

    if not data1 and data2:
        message = f"Cannot determine data for '{where}' in '{file1_rel}'"
        log_output(message)
        log_output(visual_length(message) * "-")
        return None
    if data1 and not data2:
        message = f"Cannot determine data for '{where}' in '{file2_rel}'"
        log_output(message)
        log_output(visual_length(message) * "-")
        return None
    if not data1 and not data2:
        message = f"No data for either resource: '{where}'"
        log_output(message)
        log_output(len(message) * "-")
        return True

    if not data1 or not data2:
        return None

    if ext in gff_types:
        gff1: GFF | None = read_gff(data1)
        gff2: GFF | None = read_gff(data2)
        if gff1 and not gff2:
            message = f"GFF resource missing in memory:\t'{file1_rel.parent / where}'"
            log_output(message)
            log_output(visual_length(message) * "-")
            return None
        if not gff1 and gff2:
            message = f"GFF resource missing in memory:\t'{file2_rel.parent / where}'"
            log_output(message)
            log_output(visual_length(message) * "-")
            return None
        if not gff1 and not gff2:
            message = f"Both GFF resources missing in memory:\t'{where}'"
            log_output(message)
            log_output(len(message) * "-")
            return None
        if gff1 and gff2:
            diff = DiffGFF(gff1, gff2, log_output)
            if not diff.is_same(current_path=where):
                message = f"^ '{where}': GFF is different ^"
                log_output(message)
                log_output("-" * len(message))
                return False
        return True

    if ext == "2da":
        twoda1 = read_2da(data1)
        twoda2 = read_2da(data2)
        if twoda1 and not twoda2:
            message = f"TSLPatcher 2DA resource missing in memory:\t'{file1_rel.parent / where}'"
            log_output(message)
            log_output(visual_length(message) * "-")
            return None
        if not twoda1 and twoda2:
            message = f"2DA resource missing in memory:\t'{file2_rel.parent / where}'"
            log_output(message)
            log_output(visual_length(message) * "-")
            return None
        if not twoda1 and not twoda2:
            message = f"Both 2DA resources missing in memory:\t'{where}'"
            log_output(message)
            log_output(len(message) * "-")
            return None
        if twoda1 and twoda2:
            diff = Diff2DA(twoda2, twoda1, log_output)
            if not diff.is_same():
                message = f"^ '{where}': 2DA is different ^"
                log_output(message)
                log_output("-" * len(message))
                return False
        return True

    if ext == "tlk":
        log_output(f"Loading TLK '{file1_rel.parent / where}'")
        tlk1: TLK = read_tlk(data1)
        log_output(f"Loading TLK '{file2_rel.parent / where}'")
        tlk2: TLK = read_tlk(data2)
        if tlk1 and not tlk2:
            message = f"TLK resource missing in memory:\t'{file1_rel.parent / where}'"
            log_output(message)
            log_output(len(message) * "-")
            return None
        if not tlk1 and tlk2:
            message = f"TLK resource missing in memory:\t'{file2_rel.parent / where}'"
            log_output(message)
            log_output(len(message) * "-")
            return None
        if not tlk1 and not tlk2:
            message = f"Both TLK resources missing in memory:\t'{where}'"
            log_output(message)
            log_output(len(message) * "-")
            return None
        if tlk1 and tlk2:
            diff = DiffTLK(tlk1, tlk2, log_output)
            if not diff.is_same():
                message = f"^ '{where}': TLK is different ^"
                log_output(message)
                log_output(len(message) * "-")
                return False
        return True

    if args.compare_hashes is True and compute_sha256(data1) != compute_sha256(data2):
        log_output(f"'{where}': SHA256 is different")
        return False
    return True


def diff_files(file1: os.PathLike | str, file2: os.PathLike | str) -> bool | None:
    c_file1 = CaseAwarePath(file1)
    c_file2 = CaseAwarePath(file2)
    c_file1_rel: CaseAwarePath = relative_path_from_to(c_file2, c_file1)
    c_file2_rel: CaseAwarePath = relative_path_from_to(c_file1, c_file2)
    is_same_result = True

    if not c_file1.exists():
        message = f"Missing file:\t{c_file1_rel}"
        log_output(message)
        log_output(visual_length(message) * "-")
        return None
    if not c_file2.exists():
        message = f"Missing file:\t{c_file2_rel}"
        log_output(message)
        log_output(visual_length(message) * "-")
        return None

    ext = c_file1_rel.suffix.lower()[1:]

    if is_erf_or_mod_file(c_file1_rel.name):
        try:
            file1_capsule = read_erf(file1)
        except ValueError as e:
            message = f"Could not load '{c_file1_rel}'. Reason: {e}"
            log_output(message)
            log_output(visual_length(message) * "-")
            return None
        try:
            file2_capsule = read_erf(file2)
        except ValueError as e:
            message = f"Could not load '{c_file2_rel}'. Reason: {e}"
            log_output(message)
            log_output(visual_length(message) * "-")
            return None

        capsule1_resources: dict[str, ERFResource] = {str(res.resref): res for res in file1_capsule}
        capsule2_resources: dict[str, ERFResource] = {str(res.resref): res for res in file2_capsule}

        # Identifying missing resources
        missing_in_capsule1 = capsule2_resources.keys() - capsule1_resources.keys()
        missing_in_capsule2 = capsule1_resources.keys() - capsule2_resources.keys()

        for resref in missing_in_capsule1:
            message = (
                f"Capsule1 resource missing\t{c_file1_rel}\t{resref}\t{capsule2_resources[resref].restype.extension.upper()}"
            )
            log_output(message)
            log_output(visual_length(message) * "-")

        for resref in missing_in_capsule2:
            message = (
                f"Capsule2 resource missing\t{c_file2_rel}\t{resref}\t{capsule1_resources[resref].restype.extension.upper()}"
            )
            log_output(message)
            log_output(visual_length(message) * "-")

        # Checking for differences
        common_resrefs = capsule1_resources.keys() & capsule2_resources.keys()  # Intersection of keys
        for resref in common_resrefs:
            res1: ERFResource = capsule1_resources[resref]
            res2: ERFResource = capsule2_resources[resref]
            ext = res1.restype.extension
            is_same_result = diff_data(res1.data, res2.data, c_file1_rel, c_file2_rel, ext, resref) and is_same_result
        return is_same_result
    return diff_data(file1, file2, c_file1_rel, c_file2_rel, ext)


def diff_directories(dir1: os.PathLike | str, dir2: os.PathLike | str) -> bool | None:
    c_dir1 = CaseAwarePath(dir1)
    c_dir2 = CaseAwarePath(dir2)

    message = f"Finding differences in the '{c_dir1.name}' folders..."
    log_output(message)
    log_output("-" * len(message))
    # Create sets of filenames for both directories
    files_path1 = {f.name.lower() for f in c_dir1.iterdir()}
    files_path2 = {f.name.lower() for f in c_dir2.iterdir()}

    # Merge both sets to iterate over unique filenames
    all_files = files_path1.union(files_path2)

    is_same_result = True
    for filename in all_files:
        is_same_result = diff_files(c_dir1 / filename, c_dir2 / filename) and is_same_result

    return is_same_result


def diff_installs(install_path1: os.PathLike | str, install_path2: os.PathLike | str) -> bool | None:
    install_path1 = CaseAwarePath(install_path1)
    install_path2 = CaseAwarePath(install_path2)
    log_output()
    log_output("Searching first install dir:", install_path1)
    log_output("Searching second install dir:", install_path2)
    log_output((max(len(str(install_path1)) + 29, len(str(install_path2)) + 30)) * "-")
    log_output()

    is_same_result = diff_files(install_path1.joinpath("dialog.tlk"), install_path2 / "dialog.tlk")
    override_path1: CaseAwarePath = install_path1.joinpath("Override")
    override_path2: CaseAwarePath = install_path2 / "Override"
    is_same_result = diff_directories(override_path1, override_path2) and is_same_result

    modules_path1: CaseAwarePath = install_path1.joinpath("Modules")
    modules_path2: CaseAwarePath = CaseAwarePath(install_path2, "Modules")
    return diff_directories(modules_path1, modules_path2) and is_same_result


def is_kotor_install_dir(path: os.PathLike | str) -> bool:
    c_path: CaseAwarePath = CaseAwarePath(path)
    return c_path.is_dir() and c_path.joinpath("chitin.key").exists()


def run_differ_from_args(path1: CaseAwarePath, path2: CaseAwarePath) -> bool | None:
    if not path1.exists():
        log_output(f"--path1='{path1}' does not exist on disk, cannot diff")
        return None
    if not path2.exists():
        log_output(f"--path2='{path2}' does not exist on disk, cannot diff")
        return None
    if is_kotor_install_dir(path1) and is_kotor_install_dir(path2):
        return diff_installs(path1, path2)
    if path1.is_dir() and path2.is_dir():
        return diff_directories(path1, path2)
    if path1.is_file() and path2.is_file():
        return diff_files(path1, path2)
    msg = f"--path1='{path1.name}' and --path2='{path2.name}' must be the same type"
    raise ValueError(msg)


parser = argparse.ArgumentParser(description="Finds differences between two KOTOR installations")
parser.add_argument("--path1", type=str, help="Path to the first K1/TSL install, file, or directory to diff.")
parser.add_argument("--path2", type=str, help="Path to the second K1/TSL install, file, or directory to diff.")
parser.add_argument("--output-log", type=str, help="Filepath of the desired output logfile")
parser.add_argument("--compare-hashes", type=bool, help="Compare hashes of any unsupported file/resource")

args, unknown = parser.parse_known_args()
while True:
    args.path1 = CaseAwarePath(
        args.path1
        or (unknown[0] if len(unknown) > 0 else None)
        or input("Path to the first K1/TSL install, file, or directory to diff: ")
        or "C:\\Program Files (x86)\\Steam\\steamapps\\common\\Knights of the Old Republic II",
    ).resolve()
    if args.path1.exists():
        break
    parser.print_help()
    args.path1 = None
while True:
    args.path2 = CaseAwarePath(
        args.path2
        or (unknown[1] if len(unknown) > 1 else None)
        or input("Path to the second K1/TSL install, file, or directory to diff: ")
        or "C:\\Program Files (x86)\\Steam\\steamapps\\common\\Knights of the Old Republic II - PyKotor",
    ).resolve()
    if args.path2.exists():
        break
    parser.print_help()
    args.path2 = None
while True:
    args.output_log = CaseAwarePath(
        args.output_log
        or (unknown[2] if len(unknown) > 2 else None)
        or input("Filepath of the desired output logfile: ")
        or "log_install_differ.log",
    ).resolve()
    if args.output_log.exists():
        break
    parser.print_help()
    args.output_log = None
args.compare_hashes = bool(args.compare_hashes)
log_output()
log_output(f"Using --path1='{args.path1}'")
log_output(f"Using --path2='{args.path2}'")
log_output(f"Using --output-log='{args.output_log}'")
log_output(f"Using --compare-hashes='{args.compare_hashes!s}'")

comparison: bool | None = run_differ_from_args(
    args.path1,
    args.path2,
)
if comparison is not None:
    log_output(
        f"'{relative_path_from_to(args.path2, args.path1)}'",
        " MATCHES " if comparison else " DOES NOT MATCH ",
        f"'{relative_path_from_to(args.path1, args.path2)}'",
    )
if comparison is None:
    log_output("Error during comparison")
