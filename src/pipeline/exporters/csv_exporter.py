from __future__ import annotations

import csv
from pathlib import Path

from pipeline.exporters.base import BaseExporter
from pipeline.models.payload import PayloadRecord


class CSVExporter(BaseExporter):
    """
    Writes payload ledger CSV files.
    """

    def export(
        self,
        output: Path,
        ledger: list[PayloadRecord],
    ) -> None:

        with output.open(
            "w",
            newline="",
            encoding="utf-8",
        ) as outfile:
            writer = csv.writer(outfile)

            writer.writerow(
                [
                    "sha256",
                    "event_id",
                    "protocol",
                    "source_ip",
                    "payload_size",
                ]
            )

            for payload in ledger:
                writer.writerow(
                    [
                        payload.sha256,
                        payload.source_event,
                        payload.protocol,
                        payload.source_ip,
                        payload.payload_size,
                    ]
                )
