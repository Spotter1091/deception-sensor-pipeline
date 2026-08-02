from datetime import UTC, datetime

from pipeline.ioc.ioc import IOC
from pipeline.stix.stix_builder import STIXBuilder


def test_build_indicator():

    ioc = IOC(
        indicator_type="ip",
        value="203.0.113.5",
        first_seen=datetime.now(UTC),
        last_seen=datetime.now(UTC),
        source_count=1,
        confidence=50,
        metadata={},
    )

    bundle = STIXBuilder().build([ioc])

    assert bundle["type"] == "bundle"

    assert bundle["spec_version"] == "2.1"

    assert len(bundle["objects"]) == 1

    indicator = bundle["objects"][0]

    assert indicator["type"] == "indicator"

    assert indicator["pattern"] == ("[ipv4-addr:value = '203.0.113.5']")

    assert indicator["labels"] == [
        "ip",
    ]
