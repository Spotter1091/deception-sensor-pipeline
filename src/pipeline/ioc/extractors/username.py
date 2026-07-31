from __future__ import annotations

from pipeline.ioc.extractors.base import BaseIOCExtractor
from pipeline.ioc.ioc import IOC
from pipeline.models.event import NormalizedEvent


class UsernameExtractor(BaseIOCExtractor):
    """
    Extract username indicators.
    """

    def extract(
        self,
        event: NormalizedEvent,
    ) -> IOC | None:

        if not event.username:
            return None

        return IOC(
            indicator_type="username",
            value=event.username,
            first_seen=event.sensor_time,
            last_seen=event.sensor_time,
            metadata={
                "protocol": event.protocol,
            },
        )
