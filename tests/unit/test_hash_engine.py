from datetime import UTC, datetime

from pipeline.models.event import NormalizedEvent
from pipeline.payloads.hash_engine import HashEngine


def test_hash_ledger():

    event = NormalizedEvent(
        event_id="1",
        schema_version="1",
        source_adapter="replay",
        sensor_time=datetime.now(UTC),
        normalized_time=datetime.now(UTC),
        protocol="http",
        source_ip="8.8.8.8",
        destination_ip="unknown",
        payload_sha256="deadbeef",
        payload_size=512,
        raw_file="replay.jsonl",
        raw_locator="1",
    )

    engine = HashEngine()

    ledger = engine.build_hash_ledger([event])

    assert len(ledger) == 1

    assert ledger[0].sha256 == "deadbeef"
