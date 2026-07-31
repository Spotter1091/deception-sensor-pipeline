from __future__ import annotations

from pathlib import Path

import pyarrow as pa
import pyarrow.parquet as pq

from pipeline.exporters.base import BaseExporter
from pipeline.models.session import Session


class ParquetExporter(BaseExporter):
    """
    Exports sessions into Apache Parquet format.
    """

    def export(
        self,
        output: Path,
        sessions: list[Session],
    ) -> None:

        rows = []

        for session in sessions:

            rows.append(
                {
                    "session_id": session.session_id,
                    "protocol": session.protocol,
                    "source_ip": session.source_ip,
                    "start_time": session.start_time,
                    "end_time": session.end_time,
                    "event_count": session.event_count,
                }
            )

        table = pa.Table.from_pylist(rows)

        pq.write_table(table, output)
