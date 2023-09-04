from __future__ import annotations

import os
import platform
import re
from pathlib import Path, PurePosixPath, PureWindowsPath
from typing import Self

from pykotor.common.misc import Game


class CaseAwarePath(Path):
    _flavour = PureWindowsPath._flavour if os.name == "nt" else PurePosixPath._flavour  # type: ignore pylint: disable-all

    def __new__(cls, *args, **kwargs):
        # Check if all arguments are already CaseAwarePath instances
        if all(isinstance(arg, CaseAwarePath) for arg in args):
            return super().__new__(cls, *args, **kwargs)
        # Build a path string from args
        path_str = os.path.join(*args)  # noqa: PTH118

        # Apply fix_path_formatting function
        fixed_path_str = CaseAwarePath._fix_path_formatting(path_str)

        # Create a new Path object with the fixed path
        return super().__new__(cls, fixed_path_str)

    def __truediv__(self, key) -> Self:
        """Uses divider operator to combine two paths.

        Args:
        ----
            self (undefined):
            key (undefined):

        """
        if not isinstance(key, CaseAwarePath):
            key = CaseAwarePath._fix_path_formatting(str(key))
        return CaseAwarePath(super().__truediv__(key))

    def __rtruediv__(self, key) -> Self:
        """Uses divider operator to combine two paths.

        Args:
        ----
            self (undefined):
            key (undefined):

        """
        if not isinstance(key, CaseAwarePath):
            key = CaseAwarePath._fix_path_formatting(str(key))
        return CaseAwarePath(super().__rtruediv__(key))

    def __getattr__(self, name):
        """Ensures that any parent method that uses our CaseAwarePath is automatically resolved to a case-sensitive path on Unix systems."""
        # Walk the MRO to find the method in superclass
        for cls in type(self).mro()[
            1:
        ]:  # Skip the first class itself, start with parents
            if hasattr(cls, name):
                attr = getattr(cls, name)
                break
        else:
            msg = f"'{type(self).__name__}' object has no attribute '{name}'"
            raise AttributeError(msg)

        # Check if the attr is a descriptor (data or method descriptor)
        if hasattr(attr, "__get__"):
            # Use the descriptor's __get__ method to bind it to the instance
            resolved_attr = attr.__get__(self, type(self))

            # Check if the resolved attribute is callable (method)
            if callable(resolved_attr):

                def method_wrapper(*args, **kwargs):
                    resolved_path = (
                        self if os.name == "nt" or self.exists() else self.resolve()
                    )
                    # Bind the method back to the resolved_path
                    bound_method = attr.__get__(resolved_path, type(resolved_path))
                    return bound_method(*args, **kwargs)

                return method_wrapper
            else:
                # It's a data descriptor, return the value
                return resolved_attr
        else:
            # It's a regular attribute
            return attr

    def joinpath(self, *args) -> Self:
        new_path = self
        for arg in args:
            new_path /= arg
        return new_path

    def resolve(self, strict=False) -> Self:
        new_path: Self = self
        if os.name != "nt" and not self.exists():
            new_path = self._get_case_sensitive_path()
        return super(CaseAwarePath, new_path).resolve(strict)

    def _get_case_sensitive_path(self) -> Self:
        parts = list(self.parts)
        i = 0

        for i in range(1, len(parts)):
            base_path = CaseAwarePath(*parts[:i])
            next_path = base_path / parts[i]

            if not next_path.is_dir() and base_path.is_dir():
                existing_items = [
                    item
                    for item in base_path.iterdir()
                    if (i == len(parts) - 1 or not item.is_file()) and item.exists()
                ]
                parts[i] = self._find_closest_match(parts[i], existing_items)

            elif not next_path.exists():
                return base_path.joinpath(*parts[i:])

        return CaseAwarePath(*parts)

    def _find_closest_match(self, target, candidates: list[Self]) -> str:
        max_matching_chars = -1
        closest_match = target
        for candidate in candidates:
            matching_chars = CaseAwarePath._get_matching_characters_count(
                candidate.name,
                target,
            )
            if matching_chars > max_matching_chars:
                max_matching_chars = matching_chars
                closest_match = candidate.name
        return closest_match

    @staticmethod
    def _get_matching_characters_count(str1: str, str2: str) -> int:
        matching_count = 0
        for i in range(min(len(str1), len(str2))):
            # don't consider a match if any char in the paths are not case-insensitive matches.
            if str1[i].lower() != str2[i].lower():
                return -1

            # increment matching count if case-sensitive match at this char index succeeds
            if str1[i] == str2[i]:
                matching_count += 1

        return matching_count

    @staticmethod
    def _fix_path_formatting(str_path: str) -> str:
        if not str_path.strip():
            return str_path

        formatted_path = str_path.replace("\\", os.sep).replace("/", os.sep)

        if os.altsep is not None:
            formatted_path = formatted_path.replace(os.altsep, os.sep)

        # For Unix-like paths
        formatted_path = re.sub(r"/{2,}", "/", formatted_path)

        # For Windows paths
        formatted_path = re.sub(r"\\{2,}", "\\\\", formatted_path)

        return formatted_path.rstrip(os.sep)


def locate_game_path(game: Game):
    locations = {
        "Windows": {
            Game.K1: [
                CaseAwarePath(r"C:\Program Files\Steam\steamapps\common\swkotor"),
                CaseAwarePath(r"C:\Program Files (x86)\Steam\steamapps\common\swkotor"),
                CaseAwarePath(r"C:\Program Files\LucasArts\SWKotOR"),
                CaseAwarePath(r"C:\Program Files (x86)\LucasArts\SWKotOR"),
                CaseAwarePath(r"C:\GOG Games\Star Wars - KotOR"),
            ],
            Game.K2: [
                CaseAwarePath(
                    r"C:\Program Files\Steam\steamapps\common\Knights of the Old Republic II",
                ),
                CaseAwarePath(
                    r"C:\Program Files (x86)\Steam\steamapps\common\Knights of the Old Republic II",
                ),
                CaseAwarePath(r"C:\Program Files\LucasArts\SWKotOR2"),
                CaseAwarePath(r"C:\Program Files (x86)\LucasArts\SWKotOR2"),
                CaseAwarePath(r"C:\GOG Games\Star Wars - KotOR2"),
            ],
        },
        "Darwin": {
            Game.K1: [
                CaseAwarePath(
                    "~/Library/Application Support/Steam/steamapps/common/swkotor/Knights of the Old Republic.app/Contents/Assets",
                ),
            ],
            Game.K2: [
                CaseAwarePath(
                    "~/Library/Application Support/Steam/steamapps/common/Knights of the Old Republic II/Knights of the Old Republic II.app/Contents/Assets",
                ),
            ],
        },
        "Linux": {
            Game.K1: [
                CaseAwarePath("~/.local/share/Steam/common/SteamApps/swkotor"),
                CaseAwarePath("~/.local/share/Steam/common/steamapps/swkotor"),
                CaseAwarePath("~/.local/share/Steam/common/swkotor"),
            ],
            Game.K2: [
                CaseAwarePath(
                    "~/.local/share/Steam/common/SteamApps/Knights of the Old Republic II",
                ),
                CaseAwarePath(
                    "~/.local/share/Steam/common/steamapps/Knights of the Old Republic II",
                ),
                CaseAwarePath(
                    "~/.local/share/Steam/common/Knights of the Old Republic II",
                ),
            ],
        },
    }

    potential = locations[platform.system()][game]
    return next((path for path in potential if path.exists()), None)
