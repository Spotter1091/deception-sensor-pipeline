from pathlib import Path

from pipeline.detections.suricata_exporter import SuricataExporter
from pipeline.detections.suricata_rule import SuricataRule


def test_suricata_exporter(tmp_path: Path):

    rule = SuricataRule(
        sid=1000001,
        message="Replay activity",
        protocol="tcp",
        source="$EXTERNAL_NET",
        source_port="any",
        direction="->",
        destination="$HOME_NET",
        destination_port="22",
        options=[
            'msg:"Replay activity"',
            "sid:1000001",
            "rev:1",
        ],
    )

    destination = tmp_path / "suricata.rules"

    SuricataExporter().export(
        destination,
        [rule],
    )

    assert destination.exists()

    text = destination.read_text(
        encoding="utf-8",
    )

    assert "alert tcp" in text
    assert "sid:1000001" in text
