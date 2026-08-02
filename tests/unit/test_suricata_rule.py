from pipeline.detections.suricata_rule import SuricataRule


def test_suricata_rule():

    rule = SuricataRule(
        sid=1000001,
        message="Replay activity",
        protocol="tcp",
        source="$EXTERNAL_NET",
        source_port="any",
        direction="->",
        destination="$HOME_NET",
        destination_port="22",
    )

    assert rule.sid == 1000001
    assert rule.protocol == "tcp"
    assert rule.destination_port == "22"
    assert rule.options == []
