from pipeline.assessment.assessment_builder import (
    AssessmentManifestBuilder,
)


def test_assessment_builder():

    manifest = AssessmentManifestBuilder(
        commit="abc123",
        assigned_pack={},
        environment={"os": "Linux"},
        commands={"build": "make analyze"},
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
        inputs=["input.jsonl"],
        outputs=["output.json"],
        manual_preconditions=[],
        known_limitations=[],
    ).build()

    assert manifest.schema_version == "1.0"
    assert manifest.commit == "abc123"
    assert manifest.project_id == "SOC-A1"
    assert manifest.variant == "V1"
    assert manifest.outputs == ["output.json"]
    assert manifest.candidate_binding == ("from-assigned-participant-pack")
