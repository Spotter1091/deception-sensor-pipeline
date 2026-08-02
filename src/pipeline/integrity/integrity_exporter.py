from __future__ import annotations

from pathlib import Path


class IntegrityExporter:
    """
    Writes the integrity attestation document.
    """

    def export(
        self,
        output: Path,
        document: str,
    ) -> None:

        output.write_text(
            document,
            encoding="utf-8",
        )
