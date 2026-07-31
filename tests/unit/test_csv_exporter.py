from pathlib import Path

from pipeline.exporters.csv_exporter import CSVExporter
from pipeline.models.payload import PayloadRecord


def test_export_csv(tmp_path: Path):

    ledger = [

        PayloadRecord(
            sha256="deadbeef",
            source_event="1",
            protocol="http",
            source_ip="8.8.8.8",
            payload_size=123,
        )

    ]

    outfile = tmp_path / "ledger.csv"

    exporter = CSVExporter()

    exporter.export(outfile, ledger)

    assert outfile.exists()

    text = outfile.read_text()

    assert "deadbeef" in text
