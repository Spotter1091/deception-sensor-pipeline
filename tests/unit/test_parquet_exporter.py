from datetime import UTC, datetime

from pipeline.exporters.parquet_exporter import ParquetExporter
from pipeline.models.session import Session


def test_export_parquet(tmp_path):

    session = Session(
        session_id="abc",
        protocol="telnet",
        source_ip="10.0.0.1",
        start_time=datetime.now(UTC),
        end_time=datetime.now(UTC),
        events=[],
        event_count=0,
    )

    outfile = tmp_path / "sessions.parquet"

    ParquetExporter().export(
        outfile,
        [session],
    )

    assert outfile.exists()
