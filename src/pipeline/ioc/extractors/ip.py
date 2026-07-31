from __future__ import annotations

from pipeline.ioc.extractors.base import BaseIOCExtractor
from pipeline.ioc.ioc import IOC
from pipeline.models.event import NormalizedEvent


class IPExtractor(BaseIOCExtractor):
    """
    Extract source IP indicators.
    """

    def extract(
        self,
        event: NormalizedEvent,
    ) -> IOC:

        return IOC(
            indicator_type="ip",
            value=event.source_ip,
            first_seen=event.sensor_time,
            last_seen=event.sensor_time,
            metadata={
                "protocol": event.protocol,
            },
        )
