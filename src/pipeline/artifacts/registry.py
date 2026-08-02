from __future__ import annotations

from typing import Any

from pipeline.exporters.csv_exporter import CSVExporter
from pipeline.exporters.ioc_csv_exporter import IOCCSVExporter
from pipeline.exporters.json_exporter import JSONExporter
from pipeline.exporters.parquet_exporter import ParquetExporter
from pipeline.exporters.stix_exporter import STIXExporter


class ExportRegistry:
    """
    Registry of every artifact exporter.

    Adding a new exporter should require
    only one additional registration.
    """

    def __init__(self) -> None:

        json_exporter = JSONExporter()

        self._exporters: list[tuple[Any, str]] = [
            (CSVExporter(), "hash-ledger.csv"),
            (json_exporter, "clusters.json"),
            (json_exporter, "isolation-results.json"),
            (ParquetExporter(), "sessions.parquet"),
            (STIXExporter(), "stix-bundle.json"),
            (IOCCSVExporter(), "iocs.csv"),
        ]

    @property
    def exporters(self) -> list[tuple[Any, str]]:
        return self._exporters
