from __future__ import annotations

import csv
import io
import json
from typing import Optional

from pykotor.resource.formats.twoda.twoda_data import TwoDA
from pykotor.resource.type import TARGET_TYPES, SOURCE_TYPES, ResourceReader, ResourceWriter


class TwoDAJSONReader(ResourceReader):
    def __init__(
            self,
            source: SOURCE_TYPES,
            offset: int = 0,
            size: int = 0
    ):
        super().__init__(source, offset, size)
        data = self._reader.read_bytes(self._reader.size()).decode()
        self._json = json.loads(data)
        self._twoda: Optional[TwoDA] = None

    def load(
            self,
            auto_close: bool = True
    ) -> TwoDA:
        self._twoda = TwoDA()

        for row in self._json['rows']:
            row_label = row["_id"]
            del row["_id"]

            for header in row:
                if header not in self._twoda.get_headers():
                    self._twoda.add_column(header)

            self._twoda.add_row(row_label, row)

        if auto_close:
            self._reader.close()

        return self._twoda


class TwoDAJSONWriter(ResourceWriter):
    def __init__(
            self,
            twoda: TwoDA,
            target: TARGET_TYPES
    ):
        super().__init__(target)
        self._twoda: TwoDA = twoda
        self._json = {"rows": []}

    def write(
            self,
            auto_close: bool = True
    ) -> None:
        for row in self._twoda:
            json_row = {"_id": row.label()}
            self._json["rows"].append(json_row)
            for header in self._twoda.get_headers():
                json_row[header] = row.get_string(header)

        json_dump = json.dumps(self._json, indent=4)
        self._writer.write_bytes(json_dump.encode())

        if auto_close:
            self._writer.close()
