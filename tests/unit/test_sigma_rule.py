from pipeline.detections.sigma_rule import SigmaRule


def test_sigma_rule_model():

    rule = SigmaRule(
        title="SSH Brute Force",
        identifier="SIGMA-001",
        description="Detect repeated SSH login failures.",
        status="experimental",
        logsource={"product": "linux"},
        detection={"selection": {}},
        level="high",
    )

    assert rule.identifier == "SIGMA-001"
    assert rule.level == "high"
    assert rule.tags == []
    assert rule.references == []
