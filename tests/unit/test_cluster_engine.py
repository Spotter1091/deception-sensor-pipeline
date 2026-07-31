from datetime import UTC, datetime

from pipeline.clustering.cluster_engine import ClusterEngine
from pipeline.models.event import NormalizedEvent
from pipeline.models.session import Session


def test_single_cluster():

    event = NormalizedEvent(
        event_id="1",
        schema_version="1",
        source_adapter="replay",

        sensor_time=datetime.now(UTC),
        normalized_time=datetime.now(UTC),

        protocol="telnet",

        source_ip="10.0.0.1",

        destination_ip="unknown",

        username="root",

        raw_file="replay.jsonl",
        raw_locator="1",
    )

    session = Session(
        session_id="abc",

        protocol="telnet",

        source_ip="10.0.0.1",

        start_time=event.sensor_time,
        end_time=event.sensor_time,

        events=[event],

        event_count=1,
    )

    engine = ClusterEngine()

    clusters = engine.build_clusters([session])

    assert len(clusters) == 1
    assert clusters[0].session_count == 1
    assert clusters[0].username == "root"
