from __future__ import annotations

from pathlib import Path
from typing import Any

from pipeline.exporters.stix_exporter import STIXExporter
from pipeline.exporters.csv_exporter import CSVExporter
from pipeline.exporters.json_exporter import JSONExporter
from pipeline.exporters.parquet_exporter import ParquetExporter


class ExportRegistry:
    """
    Registry of every artifact exporter.

    Adding a new exporter should require
    only one additional registration.
    """

    def __init__(self) -> None:
        self._exporters: list[tuple[Any, str]] = [
            (CSVExporter(), "hash-ledger.csv"),
            (JSONExporter(), "clusters.json"),
            (ParquetExporter(), "sessions.parquet"),
            (STIXExporter(), "stix-bundle.json"),
        ]

    @property
    def exporters(self) -> list[tuple[Any, str]]:
        return self._exporters
