from __future__ import annotations

from pipeline.ioc.extractors.base import BaseIOCExtractor
from pipeline.ioc.ioc import IOC
from pipeline.models.event import NormalizedEvent


class SHA256Extractor(BaseIOCExtractor):
    """
    Extract SHA-256 payload indicators.
    """

    def extract(
        self,
        event: NormalizedEvent,
    ) -> IOC | None:

        if not event.payload_sha256:
            return None

        return IOC(
            indicator_type="sha256",
            value=event.payload_sha256,
            first_seen=event.sensor_time,
            last_seen=event.sensor_time,
            metadata={
                "protocol": event.protocol,
            },
        )
