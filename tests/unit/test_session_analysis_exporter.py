from pathlib import Path

from pipeline.session_analysis.session_analysis import (
    EvidenceStep,
    SessionAnalysis,
)
from pipeline.session_analysis.session_analysis_exporter import (
    SessionAnalysisExporter,
)


def test_session_analysis_exporter(tmp_path: Path):

    analysis = SessionAnalysis(
        session_id="session-1",
        sensor="Replay",
        first_utc="2026-01-01T00:00:00Z",
        last_utc="2026-01-01T00:05:00Z",
        evidence_marker="Replay",
    )

    analysis.evidence_chain.append(
        EvidenceStep(
            step=1,
            utc="2026-01-01T00:00:00Z",
            raw_locator="line:1",
            observed_action="SSH connection",
            interpretation="Replay event",
            confidence="High",
            alternative="None",
        )
    )

    destination = tmp_path / "session-analysis.md"

    SessionAnalysisExporter().export(
        destination,
        analysis,
    )

    assert destination.exists()

    text = destination.read_text(
        encoding="utf-8",
    )

    assert "Honeypot Session Analysis" in text
    assert "session-1" in text
    assert "SSH connection" in text
