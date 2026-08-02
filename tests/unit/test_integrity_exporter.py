from pathlib import Path

from pipeline.integrity.integrity_exporter import (
    IntegrityExporter,
)


def test_integrity_exporter(
    tmp_path: Path,
):

    output = tmp_path / "integrity-attestation.md"

    IntegrityExporter().export(
        output,
        "# Test Document",
    )

    assert output.exists()

    assert output.read_text(encoding="utf-8") == "# Test Document"
