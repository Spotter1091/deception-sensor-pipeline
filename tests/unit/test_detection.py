from pipeline.detections.detection import Detection


def test_detection_model():

    detection = Detection(
        title="SSH Brute Force",
        description="Multiple failed SSH logins.",
        source="Replay",
        detection_type="sigma",
        level="high",
    )

    assert detection.title == "SSH Brute Force"
    assert detection.level == "high"
    assert detection.references == []
    assert detection.tags == []
    assert detection.iocs == []
