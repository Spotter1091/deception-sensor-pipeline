from pathlib import Path

from pipeline.manifest.manifest_builder import ManifestBuilder


def test_manifest_builder(tmp_path: Path):

    artifacts = [
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

    for filename in artifacts:
        (tmp_path / filename).write_text(
            "test",
            encoding="utf-8",
        )

    builder = ManifestBuilder()

    entries = builder.build(tmp_path)

    assert len(entries) == 14

    for entry in entries:
        assert len(entry.sha256) == 64
        assert entry.filename in artifacts
