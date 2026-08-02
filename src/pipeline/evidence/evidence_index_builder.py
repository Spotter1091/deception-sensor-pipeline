from __future__ import annotations

import hashlib
from datetime import UTC, datetime
from pathlib import Path

from pipeline.evidence.evidence_claim import EvidenceClaim


class EvidenceIndexBuilder:
    """
    Builds the evidence-index.csv required
    for assessment submission.
    """

    ARTIFACTS = [
        {
            "filename": "sessions.parquet",
            "claim_id": "C-001",
            "section": "Session Reconstruction",
        },
        {
            "filename": "clusters.json",
            "claim_id": "C-002",
            "section": "Attack Clustering",
        },
        {
            "filename": "hash-ledger.csv",
            "claim_id": "C-003",
            "section": "Payload Analysis",
        },
        {
            "filename": "iocs.csv",
            "claim_id": "C-004",
            "section": "IOC Extraction",
        },
        {
            "filename": "stix-bundle.json",
            "claim_id": "C-005",
            "section": "Threat Intelligence",
        },
        {
            "filename": "replay-verification.json",
            "claim_id": "C-006",
            "section": "Replay Verification",
        },
        {
            "filename": "session-analysis.md",
            "claim_id": "C-007",
            "section": "Session Analysis",
        },
        {
            "filename": "sigma-rules.yml",
            "claim_id": "C-008",
            "section": "Detection Engineering",
        },
        {
            "filename": "suricata.rules",
            "claim_id": "C-009",
            "section": "Detection Engineering",
        },
        {
            "filename": "continuity-record.md",
            "claim_id": "C-010",
            "section": "Reproducibility",
        },
        {
            "filename": "integrity-attestation.md",
            "claim_id": "C-011",
            "section": "Integrity",
        },
    ]

    def build(
        self,
        derived_directory: Path,
    ) -> list[EvidenceClaim]:

        claims: list[EvidenceClaim] = []

        for spec in self.ARTIFACTS:
            artifact = derived_directory / spec["filename"]
            claims.append(self._build_claim(artifact, spec))

        return claims

    def _sha256(
        self,
        path: Path,
    ) -> str:
        """
        Calculate the SHA-256 hash of an artifact.
        """

        digest = hashlib.sha256()

        with path.open("rb") as handle:
            while chunk := handle.read(8192):
                digest.update(chunk)

        return digest.hexdigest()

    def _collection_time(
        self,
        path: Path,
    ) -> str:
        """
        Return the artifact modification time.

        This approximates the collection time
        for generated pipeline artifacts.
        """

        return datetime.fromtimestamp(
            path.stat().st_mtime,
            UTC,
        ).isoformat()

    def _build_claim(
        self,
        artifact: Path,
        spec: dict[str, str],
    ) -> EvidenceClaim:
        filename = spec["filename"]
        return EvidenceClaim(
            claim_id=spec["claim_id"],
            report_section=spec["section"],
            claim=self._claim_text(filename),
            artifact_path=str(artifact),
            exact_locator="Entire artifact",
            collection_time_utc=self._collection_time(artifact),
            sha256=self._sha256(artifact),
            proves=self._proves(filename),
            does_not_prove=self._does_not_prove(filename),
            confidence="high",
            alternative_considered=self._alternative(filename),
            disposition=self._disposition(filename),
        )

    def _claim_text(
        self,
        filename: str,
    ) -> str:
        mapping = {
            "sessions.parquet": (
                "Replay events were reconstructed into normalized attack sessions."
            ),
            "clusters.json": (
                "Sessions sharing common characteristics were clustered."
            ),
            "hash-ledger.csv": ("Unique payload hashes were extracted."),
            "iocs.csv": ("Indicators of Compromise were extracted."),
            "stix-bundle.json": ("Indicators were exported as a STIX 2.1 bundle."),
            "replay-verification.json": (
                "Replay reconstruction capability was verified."
            ),
            "session-analysis.md": (
                "Representative reconstructed attack session was documented."
            ),
            "sigma-rules.yml": ("Detection logic was exported as Sigma rules."),
            "suricata.rules": (
                "Detection logic was exported as Suricata IDS signatures."
            ),
            "continuity-record.md": (
                "Pipeline reproducibility and execution continuity were documented."
            ),
            "integrity-attestation.md": (
                "Submission integrity and reproducibility were attested."
            ),
        }
        return mapping[filename]

    def _proves(
        self,
        filename: str,
    ) -> str:
        mapping = {
            "sessions.parquet": (
                "Demonstrates that normalized events were grouped"
                " into reproducible attack sessions."
            ),
            "clusters.json": (
                "Shows that related sessions were clustered using"
                " shared characteristics."
            ),
            "hash-ledger.csv": (
                "Demonstrates that payloads were fingerprinted using SHA-256 hashes."
            ),
            "iocs.csv": (
                "Shows that observable indicators were extracted"
                " from normalized telemetry."
            ),
            "stix-bundle.json": (
                "Demonstrates that extracted indicators were"
                " exported in STIX 2.1 format."
            ),
            "replay-verification.json": (
                "Shows which replay reconstruction capabilities"
                " were successfully verified."
            ),
            "session-analysis.md": (
                "Documents the evidence supporting reconstructed session membership."
            ),
            "sigma-rules.yml": (
                "Shows generated detection rules for portable SIEM deployment."
            ),
            "suricata.rules": ("Shows generated IDS detection signatures."),
            "continuity-record.md": (
                "Documents reproducible execution of the analysis pipeline."
            ),
            "integrity-attestation.md": (
                "Documents integrity controls applied during submission generation."
            ),
        }
        return mapping[filename]

    def _does_not_prove(
        self,
        filename: str,
    ) -> str:
        mapping = {
            "sessions.parquet": ("Does not establish attacker attribution or intent."),
            "clusters.json": (
                "Does not prove clustered sessions originated"
                " from the same threat actor."
            ),
            "hash-ledger.csv": ("Does not establish that a payload is malicious."),
            "iocs.csv": ("Does not confirm compromise in another environment."),
            "stix-bundle.json": ("Does not validate indicator reputation."),
            "replay-verification.json": (
                "Does not reconstruct payload bytes absent from the source replay."
            ),
            "session-analysis.md": ("Does not independently prove attacker identity."),
            "sigma-rules.yml": (
                "Does not demonstrate detection effectiveness in production."
            ),
            "suricata.rules": ("Does not prove successful IDS deployment."),
            "continuity-record.md": (
                "Does not independently validate analytical conclusions."
            ),
            "integrity-attestation.md": (
                "Does not independently prove authenticity of source evidence."
            ),
        }
        return mapping[filename]

    def _alternative(
        self,
        filename: str,
    ) -> str:
        mapping = {
            "sessions.parquet": (
                "Individual events could have been analyzed independently."
            ),
            "clusters.json": ("Each session could have been investigated separately."),
            "hash-ledger.csv": (
                "Payloads could have been referenced only by filename."
            ),
            "iocs.csv": ("Indicators could have been identified manually."),
            "stix-bundle.json": (
                "Indicators could have been distributed in CSV format only."
            ),
            "replay-verification.json": (
                "Replay capability could have been described manually."
            ),
            "session-analysis.md": (
                "Only raw session records could have been supplied."
            ),
            "sigma-rules.yml": (
                "Detection logic could have remained embedded in source code."
            ),
            "suricata.rules": ("Detection signatures could have been omitted."),
            "continuity-record.md": (
                "Execution steps could have remained undocumented."
            ),
            "integrity-attestation.md": (
                "Integrity controls could have remained implicit."
            ),
        }
        return mapping[filename]

    def _disposition(
        self,
        filename: str,
    ) -> str:
        mapping = {
            "sessions.parquet": (
                "Retained session reconstruction because it preserves event chronology."
            ),
            "clusters.json": (
                "Retained clustering because it supports attack-pattern analysis."
            ),
            "hash-ledger.csv": (
                "Retained cryptographic hashes as canonical payload identifiers."
            ),
            "iocs.csv": (
                "Retained automated IOC extraction because it is reproducible."
            ),
            "stix-bundle.json": (
                "Retained STIX because it enables interoperability"
                " with threat intelligence platforms."
            ),
            "replay-verification.json": (
                "Retained replay verification to document"
                " supported reconstruction guarantees."
            ),
            "session-analysis.md": (
                "Retained detailed session documentation to support evidence review."
            ),
            "sigma-rules.yml": ("Retained Sigma export for SIEM portability."),
            "suricata.rules": (
                "Retained Suricata signatures for IDS interoperability."
            ),
            "continuity-record.md": (
                "Retained continuity record to support reproducible assessment."
            ),
            "integrity-attestation.md": (
                "Retained integrity attestation to document submission controls."
            ),
        }
        return mapping[filename]
