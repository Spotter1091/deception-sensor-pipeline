from __future__ import annotations

import csv
from pathlib import Path

from pipeline.exporters.base import BaseExporter
from pipeline.ioc.ioc import IOC


class IOCCSVExporter(BaseExporter):
    """
    Export IOC records to CSV.
    """

    def export(
        self,
        output: Path,
        iocs: list[IOC],
    ) -> None:

        with output.open(
            "w",
            newline="",
            encoding="utf-8",
        ) as file:
            writer = csv.writer(file)

            writer.writerow(
                [
                    "indicator_type",
                    "value",
                    "first_seen",
                    "last_seen",
                    "source_count",
                    "confidence",
                ]
            )

            for ioc in iocs:
                writer.writerow(
                    [
                        ioc.indicator_type,
                        ioc.value,
                        ioc.first_seen.isoformat(),
                        ioc.last_seen.isoformat(),
                        ioc.source_count,
                        ioc.confidence,
                    ]
                )
