from datetime import UTC, datetime

from pipeline.ioc.ioc import IOC
from pipeline.models.cluster import Cluster
from pipeline.models.event import NormalizedEvent
from pipeline.models.payload import PayloadRecord
from pipeline.models.session import Session
from pipeline.session_analysis.session_analysis_builder import (
    SessionAnalysisBuilder,
)


def test_session_analysis_builder():

    event = NormalizedEvent(
        event_id="evt-1",
        source_adapter="replay",
        sensor_time=datetime.now(UTC),
        normalized_time=datetime.now(UTC),
        protocol="tcp",
        source_ip="192.0.2.10",
        destination_ip="198.51.100.5",
        source_port=12345,
        destination_port=22,
        raw_file="honeypot-replay.jsonl",
        raw_locator="line:1",
        connection_id="conn-1",
        username="root",
        payload_sha256="deadbeef",
    )

    session = Session(
        session_id="session-1",
        protocol="tcp",
        connection_id="conn-1",
        source_ip="192.0.2.10",
        start_time=event.sensor_time,
        end_time=event.sensor_time,
        events=[event],
        event_count=1,
    )

    cluster = Cluster(
        cluster_id="cluster-1",
        protocol="tcp",
        source_ip="192.0.2.10",
        sessions=[session],
        session_count=1,
    )

    ioc = IOC(
        indicator_type="ip",
        value="192.0.2.10",
        first_seen=event.sensor_time,
        last_seen=event.sensor_time,
    )

    payload = PayloadRecord(
        sha256="deadbeef",
        source_event="evt-1",
        protocol="tcp",
        source_ip="192.0.2.10",
        payload_size=100,
    )

    analysis = SessionAnalysisBuilder().build(
        session=session,
        clusters=[cluster],
        iocs=[ioc],
        payloads=[payload],
    )

    assert analysis.session_id == "session-1"
    assert len(analysis.evidence_chain) == 1

    assert analysis.intent_assessment != ""
    assert "cluster-1" in analysis.intent_assessment

    assert "ip: 192.0.2.10" in analysis.indicators
    assert "SHA256: deadbeef" in analysis.indicators
