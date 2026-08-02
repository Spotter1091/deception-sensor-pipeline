from pipeline.continuity.continuity_builder import (
    ContinuityBuilder,
)


def test_continuity_builder():

    record = ContinuityBuilder().build()

    assert "Stage 5 codebase" in record.previous_stage_commit

    assert record.reused_component == "None."

    assert "pipeline.main" in record.consumed_interface

    assert "manifest.sha256" in record.provenance_evidence
