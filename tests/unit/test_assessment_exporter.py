import json

from pipeline.assessment.assessment_builder import (
    AssessmentManifestBuilder,
)
from pipeline.assessment.assessment_exporter import (
    AssessmentManifestExporter,
)


def test_assessment_exporter(tmp_path):

    manifest = AssessmentManifestBuilder(
        commit="abc123",
        assigned_pack={},
        environment={"os": "Linux"},
        commands={},
        results={
            "public_tests": {
                "passed": 16,
                "failed": 0,
                "report": "",
            },
            "runtime_seconds": 10,
            "peak_memory_mb": 100,
            "output_hashes": {},
        },
        inputs=[],
        outputs=[],
        manual_preconditions=[],
        known_limitations=[],
    ).build()

    destination = tmp_path / "assessment-manifest.json"

    AssessmentManifestExporter().export(
        manifest,
        destination,
    )

    with destination.open(
        encoding="utf-8",
    ) as handle:
        data = json.load(handle)

    assert data["schema_version"] == "1.0"
    assert data["commit"] == "abc123"
    assert "results" in data
    assert "outputs" in data
