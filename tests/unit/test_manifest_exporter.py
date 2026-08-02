from pathlib import Path

from pipeline.manifest.manifest_entry import ManifestEntry
from pipeline.manifest.manifest_exporter import ManifestExporter


def test_manifest_exporter(
    tmp_path: Path,
):

    output = tmp_path / "manifest.sha256"

    entries = [
        ManifestEntry(
            filename="demo.txt",
            sha256="a" * 64,
        ),
    ]

    ManifestExporter().export(
        output,
        entries,
    )

    assert output.exists()

    text = output.read_text()

    assert "demo.txt" in text

    assert ("a" * 64) in text
