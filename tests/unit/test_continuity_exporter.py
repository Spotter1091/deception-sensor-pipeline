from pathlib import Path

from pipeline.continuity.continuity_exporter import (
    ContinuityExporter,
)
from pipeline.continuity.continuity_record import (
    ContinuityRecord,
)


def test_continuity_exporter(
    tmp_path: Path,
):

    output = tmp_path / "continuity-record.md"

    record = ContinuityRecord(
        previous_stage_commit="Stage 5 codebase",
        reused_component="None.",
        consumed_interface="pipeline.main",
        backward_compatible_extension="None",
        provenance_evidence="manifest.sha256",
        migration_record="No incompatible changes.",
        next_stage_handoff="Assessment package",
    )

    ContinuityExporter().export(
        output,
        record,
    )

    assert output.exists()

    text = output.read_text(encoding="utf-8")

    assert "Previous-stage commit" in text

    assert "Next-stage Handoff" in text
