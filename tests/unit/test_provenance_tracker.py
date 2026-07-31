from datetime import UTC, datetime

from pipeline.models.event import NormalizedEvent
from pipeline.models.session import Session
from pipeline.provenance.provenance_tracker import ProvenanceTracker


def test_session_lineage():

    event = NormalizedEvent(
        event_id="1",
        schema_version="1",
        source_adapter="replay",

        sensor_time=datetime.now(UTC),
        normalized_time=datetime.now(UTC),

        protocol="telnet",

        source_ip="1.1.1.1",

        destination_ip="unknown",

        raw_file="replay.jsonl",
        raw_locator="line-42",
    )

    session = Session(
        session_id="abc",
        protocol="telnet",

        source_ip="1.1.1.1",

        start_time=event.sensor_time,
        end_time=event.sensor_time,

        events=[event],

        event_count=1,
    )

    tracker = ProvenanceTracker()

    lineage = tracker.session_to_record(session)

    assert lineage["session_id"] == "abc"
    assert lineage["events"][0]["raw_locator"] == "line-42"
