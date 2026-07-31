from datetime import UTC, datetime

from pipeline.models.event import NormalizedEvent
from pipeline.sessionization.session_engine import SessionEngine


def test_build_single_session():

    engine = SessionEngine()

    events = [
        NormalizedEvent(
            event_id="1",
            schema_version="1",
            source_adapter="replay",
            sensor_time=datetime(2026, 7, 1, 0, 0, tzinfo=UTC),
            normalized_time=datetime.now(UTC),
            connection_id="abc",
            protocol="telnet",
            source_ip="1.1.1.1",
            source_port=1234,
            destination_ip="unknown",
            destination_port=23,
            raw_file="replay.jsonl",
            raw_locator="1",
        ),
        NormalizedEvent(
            event_id="2",
            schema_version="1",
            source_adapter="replay",
            sensor_time=datetime(2026, 7, 1, 0, 1, tzinfo=UTC),
            normalized_time=datetime.now(UTC),
            connection_id="abc",
            protocol="telnet",
            source_ip="1.1.1.1",
            source_port=1234,
            destination_ip="unknown",
            destination_port=23,
            raw_file="replay.jsonl",
            raw_locator="2",
        ),
    ]

    sessions = engine.build_sessions(events)

    assert len(sessions) == 1
    assert sessions[0].event_count == 2
    assert sessions[0].connection_id == "abc"
