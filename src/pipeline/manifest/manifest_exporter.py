from __future__ import annotations

from pathlib import Path

from pipeline.manifest.manifest_entry import ManifestEntry


class ManifestExporter:
    """
    Exports manifest.sha256.
    """

    def export(
        self,
        output: Path,
        entries: list[ManifestEntry],
    ) -> None:

        with output.open(
            "w",
            encoding="utf-8",
        ) as file:
            for entry in entries:
                file.write(f"{entry.sha256}  {entry.filename}\n")
