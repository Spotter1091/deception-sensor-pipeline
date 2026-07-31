from pipeline.models.cluster import Cluster
from pipeline.stix.stix_builder import STIXBuilder


def test_build_indicator():

    cluster = Cluster(
        cluster_id="cluster-1",
        protocol="telnet",
        source_ip="203.0.113.5",
        session_count=7,
    )

    bundle = STIXBuilder().build([cluster])

    assert len(bundle) == 1

    indicator = bundle[0]

    assert indicator["type"] == "indicator"

    assert indicator["pattern"] == (
        "[ipv4-addr:value = '203.0.113.5']"
    )

    assert indicator["labels"] == [
        "telnet",
    ]
