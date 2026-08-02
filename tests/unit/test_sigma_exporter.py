from pathlib import Path

from pipeline.detections.sigma_exporter import SigmaExporter
from pipeline.detections.sigma_rule import SigmaRule


def test_sigma_exporter(tmp_path: Path):

    rule = SigmaRule(
        title="Replay Source IP Activity",
        identifier="SIGMA-0001",
        description="Test rule",
        status="experimental",
        logsource={
            "category": "network_connection",
            "product": "linux",
        },
        detection={
            "selection": {
                "source_ip": [
                    "192.0.2.1",
                ],
            },
            "condition": "selection",
        },
        level="medium",
        tags=[
            "network",
        ],
        references=[
            "unit-test",
        ],
    )

    destination = tmp_path / "sigma-rules.yml"

    SigmaExporter().export(
        destination,
        [rule],
    )

    assert destination.exists()

    text = destination.read_text(
        encoding="utf-8",
    )

    assert "Replay Source IP Activity" in text
    assert "SIGMA-0001" in text
