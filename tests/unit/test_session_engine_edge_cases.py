from __future__ import annotations

from datetime import datetime

from pipeline.models.event import NormalizedEvent
from pipeline.payloads.hash_engine import HashEngine
from pipeline.sessionization.session_engine import SessionEngine


def make_event(
    *,
    event_id: str,
    connection_id: str,
    protocol: str,
    source_ip: str,
    timestamp: str,
    payload_sha256: str | None = None,
) -> NormalizedEvent:

    t = datetime.fromisoformat(timestamp.replace("Z", "+00:00"))

    return NormalizedEvent(
        event_id=event_id,
        source_adapter="replay",
        sensor_time=t,
        normalized_time=t,
        connection_id=connection_id,
        protocol=protocol,
        source_ip=source_ip,
        raw_file="sample.jsonl",
        raw_locator=event_id,
        payload_sha256=payload_sha256,
    )


def test_out_of_order_events():

    events = [
        make_event(
            event_id="2",
            connection_id="abc",
            protocol="ssh",
            source_ip="1.1.1.1",
            timestamp="2026-01-01T00:00:10Z",
        ),
        make_event(
            event_id="1",
            connection_id="abc",
            protocol="ssh",
            source_ip="1.1.1.1",
            timestamp="2026-01-01T00:00:00Z",
        ),
    ]

    sessions = SessionEngine().build_sessions(events)

    assert len(sessions) == 1

    assert sessions[0].events[0].event_id == "1"

    assert sessions[0].events[1].event_id == "2"


def test_client_reconnect_same_connection():

    events = [
        make_event(
            event_id="1",
            connection_id="xyz",
            protocol="telnet",
            source_ip="2.2.2.2",
            timestamp="2026-01-01T00:00:00Z",
        ),
        make_event(
            event_id="2",
            connection_id="xyz",
            protocol="telnet",
            source_ip="2.2.2.2",
            timestamp="2026-01-01T00:05:00Z",
        ),
    ]

    sessions = SessionEngine().build_sessions(events)

    assert len(sessions) == 1


def test_protocol_change_creates_new_session():

    events = [
        make_event(
            event_id="1",
            connection_id="shared",
            protocol="ssh",
            source_ip="3.3.3.3",
            timestamp="2026-01-01T00:00:00Z",
        ),
        make_event(
            event_id="2",
            connection_id="shared",
            protocol="telnet",
            source_ip="3.3.3.3",
            timestamp="2026-01-01T00:00:01Z",
        ),
    ]

    sessions = SessionEngine().build_sessions(events)

    assert len(sessions) == 2


def test_repeated_credentials_remain_same_session():

    events = [
        make_event(
            event_id="1",
            connection_id="login",
            protocol="ssh",
            source_ip="4.4.4.4",
            timestamp="2026-01-01T00:00:00Z",
        ),
        make_event(
            event_id="2",
            connection_id="login",
            protocol="ssh",
            source_ip="4.4.4.4",
            timestamp="2026-01-01T00:00:05Z",
        ),
    ]

    sessions = SessionEngine().build_sessions(events)

    assert len(sessions) == 1

    assert sessions[0].event_count == 2


def test_hash_engine_is_deterministic():

    events = [
        make_event(
            event_id="1",
            connection_id="hash",
            protocol="ssh",
            source_ip="5.5.5.5",
            timestamp="2026-01-01T00:00:00Z",
            payload_sha256="abc123",
        ),
    ]

    engine = HashEngine()

    first = engine.build_hash_ledger(events)

    second = engine.build_hash_ledger(events)

    assert first == second
