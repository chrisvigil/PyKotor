from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional, Union

from pykotor.resource.formats.gff import GFF, GFFFieldType, GFFList, GFFStruct
from pykotor.tools.path import PureWindowsPath

if TYPE_CHECKING:
    import os

fieldtype_to_fieldname: dict[GFFFieldType, str] = {
    GFFFieldType.UInt8: "Byte",
    GFFFieldType.Int8: "Char",
    GFFFieldType.UInt16: "Word",
    GFFFieldType.Int16: "Short",
    GFFFieldType.UInt32: "DWORD",
    GFFFieldType.Int32: "Int",
    GFFFieldType.Int64: "Int64",
    GFFFieldType.Single: "Float",
    GFFFieldType.Double: "Double",
    GFFFieldType.String: "ExoString",
    GFFFieldType.ResRef: "ResRef",
    GFFFieldType.LocalizedString: "ExoLocString",
    GFFFieldType.Vector3: "Position",
    GFFFieldType.Vector4: "Orientation",
    GFFFieldType.Struct: "Struct",
    GFFFieldType.List: "List",
}


MAX_CHARS_BEFORE_NEWLINE_FORMAT = 50


def format_text(value) -> str:
    text = str(value)
    if "\n" in text or len(text) > MAX_CHARS_BEFORE_NEWLINE_FORMAT:
        return f'"""\n{text}\n"""'
    return f"'{text}'"


class DiffGFF:
    def __init__(self, old: GFF, new: GFF, log_func=print):
        self.old: GFF = old
        self.new: GFF = new
        self.log = log_func

    def is_same(
        self,
        old_struct: GFFStruct | None = None,
        new_struct: GFFStruct | None = None,
        current_path: PureWindowsPath | os.PathLike | str | None = None,
    ) -> bool:
        current_path = PureWindowsPath(current_path or "GFFRoot")
        old_struct = old_struct or self.old.root
        new_struct = new_struct or self.new.root

        if len(old_struct) != len(new_struct):  # sourcery skip: class-extract-method
            self.log(f"GFFStruct: number of fields have changed at '{current_path}': '{len(old_struct)}' --> '{len(new_struct)}'")
            self.log()
            is_same_result = False

        # Create dictionaries for both old and new structures
        old_dict: dict[str, tuple[GFFFieldType, Any]] = {
            label or f"gffstruct({idx})": (ftype, value) for idx, (label, ftype, value) in enumerate(old_struct)
        }
        new_dict: dict[str, tuple[GFFFieldType, Any]] = {
            label or f"gffstruct({idx})": (ftype, value) for idx, (label, ftype, value) in enumerate(new_struct)
        }

        # Union of labels from both old and new structures
        all_labels = set(old_dict.keys()) | set(new_dict.keys())

        is_same_result = True

        for label in all_labels:
            child_path = current_path / str(label)
            old_ftype, old_value = old_dict.get(label, (None, None))
            new_ftype, new_value = new_dict.get(label, (None, None))
            old_ftype_name = fieldtype_to_fieldname.get(old_ftype, old_ftype)  # type: ignore[fallback val already defined]
            new_ftype_name = fieldtype_to_fieldname.get(new_ftype, new_ftype)  # type: ignore[fallback val already defined]

            # Check for missing fields/values in either structure
            if old_ftype is None or old_value is None:
                self.log(
                    f"Extra '{new_ftype_name}' field found at '{child_path}': {format_text(new_value)}",
                )
                is_same_result = False
                continue
            if new_value is None or new_ftype is None:
                self.log(
                    f"Missing '{old_ftype_name}' field at '{child_path}': {format_text(old_value)}",
                )
                is_same_result = False
                continue

            # Check if field types have changed
            if old_ftype != new_ftype:
                self.log(
                    f"Field type is different at '{child_path}': '{old_ftype_name}'-->'{new_ftype_name}'",
                )
                is_same_result = False
                continue

            # Compare values depending on their types
            if old_ftype == GFFFieldType.Struct:
                if old_value.struct_id != new_value.struct_id:
                    self.log(f"Struct ID is different at '{child_path}': '{old_value.struct_id}'-->'{new_value.struct_id}'")
                    is_same_result = False

                if not self.is_same(old_value, new_value, child_path):
                    is_same_result = False
                    continue

            elif old_ftype == GFFFieldType.List:
                if not self._output_diff_from_two_lists(old_value, new_value, child_path):
                    is_same_result = False
                    continue

            elif old_value != new_value:
                self.log(f"Field '{old_ftype_name}' is different at '{child_path}': {format_text(old_value)}-vvv->{format_text(new_value)}")
                is_same_result = False
                continue

        return is_same_result

    def _output_diff_from_two_lists(self, old_gff_list: GFFList, new_gff_list: GFFList, current_path: PureWindowsPath) -> bool:
        is_same_result = True

        if len(old_gff_list) != len(new_gff_list):
            self.log(f"GFFList counts have changed at '{current_path}': '{len(old_gff_list)}' --> '{len(new_gff_list)}'")
            self.log()
            is_same_result = False

        old_set, new_set = dict(enumerate(old_gff_list)), dict(enumerate(new_gff_list))

        # Detect unique items in both lists
        unique_to_old: set[int] = old_set.keys() - new_set.keys()
        unique_to_new: set[int] = new_set.keys() - old_set.keys()

        for list_index in unique_to_old:
            struct = old_set[list_index]
            self.log(f"Missing GFFStruct at '{current_path / str(list_index)}' with struct ID '{struct.struct_id}'")
            self.log("Contents of old struct:")
            for label, field_type, field_value in struct:
                self.log(fieldtype_to_fieldname.get(field_type, field_type), f"{label}: {format_text(field_value)}")
            self.log()
            is_same_result = False

        for list_index in unique_to_new:
            struct = new_set[list_index]
            self.log(f"Extra GFFStruct at '{current_path / str(list_index)}' with struct ID '{struct.struct_id}'")
            self.log("Contents of new struct:")
            for label, field_type, field_value in struct:
                self.log(fieldtype_to_fieldname.get(field_type, field_type), f"{label}: {format_text(field_value)}")
            self.log()
            is_same_result = False

        # For items present in both lists
        common_items = old_set.keys() & new_set.keys()
        for list_index in common_items:
            old_child: GFFStruct = old_set[list_index]
            new_child: GFFStruct = new_set[list_index]
            if not self.is_same(old_child, new_child, current_path / str(list_index)):
                is_same_result = False

        return is_same_result
