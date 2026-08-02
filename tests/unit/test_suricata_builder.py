from pipeline.detections.suricata_builder import SuricataBuilder


def test_suricata_builder():

    rules = SuricataBuilder().build(
        sessions=[],
        clusters=[],
        iocs=[],
        payloads=[],
    )

    assert isinstance(rules, list)
    assert rules == []
