from __future__ import annotations

import hashlib
from pathlib import Path

from pipeline.manifest.manifest_entry import ManifestEntry


class ManifestBuilder:
    """
    Builds SHA-256 manifest entries
    for generated artifacts.
    """

    ARTIFACTS = [
        "sessions.parquet",
        "clusters.json",
        "hash-ledger.csv",
        "iocs.csv",
        "stix-bundle.json",
        "replay-verification.json",
        "isolation-results.json",
        "continuity-record.md",
        "integrity-attestation.md",
        "session-analysis.md",
        "sigma-rules.yml",
        "suricata.rules",
        "assessment-manifest.json",
        "evidence-index.csv",
    ]

    def build(
        self,
        derived_directory: Path,
    ) -> list[ManifestEntry]:

        entries: list[ManifestEntry] = []

        for filename in self.ARTIFACTS:
            artifact = derived_directory / filename

            entries.append(
                ManifestEntry(
                    filename=filename,
                    sha256=self._sha256(artifact),
                )
            )

        return entries

    def _sha256(
        self,
        path: Path,
    ) -> str:

        digest = hashlib.sha256()

        with path.open("rb") as file:
            while chunk := file.read(8192):
                digest.update(chunk)

        return digest.hexdigest()
