from datetime import UTC, datetime

from pipeline.models.event import NormalizedEvent


def test_create_normalized_event():

    event = NormalizedEvent(
        event_id="1",
        source_adapter="replay",
        sensor_time=datetime.now(UTC),
        normalized_time=datetime.now(UTC),
        protocol="ssh",
        source_ip="1.1.1.1",
        destination_ip="2.2.2.2",
        raw_file="honeypot-replay.jsonl",
        raw_locator="line:1",
    )

    assert event.protocol == "ssh"
    assert event.source_ip == "1.1.1.1"
