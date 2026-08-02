from pipeline.detections.sigma_builder import SigmaBuilder


def test_sigma_builder():

    rules = SigmaBuilder().build(
        sessions=[],
        clusters=[],
        iocs=[],
        payloads=[],
    )

    assert rules == []
