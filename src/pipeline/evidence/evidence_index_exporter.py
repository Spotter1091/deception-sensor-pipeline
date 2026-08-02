from __future__ import annotations

import csv
from pathlib import Path

from pipeline.evidence.evidence_claim import EvidenceClaim


class EvidenceIndexExporter:
    """
    Writes evidence-index.csv.
    """

    def export(
        self,
        output: Path,
        claims: list[EvidenceClaim],
    ) -> None:

        with output.open(
            "w",
            newline="",
            encoding="utf-8",
        ) as handle:
            writer = csv.DictWriter(
                handle,
                fieldnames=list(EvidenceClaim.model_fields.keys()),
            )

            writer.writeheader()

            for claim in claims:
                writer.writerow(claim.model_dump())
