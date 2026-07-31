from __future__ import annotations

from pipeline.ioc.extractors.base import BaseIOCExtractor
from pipeline.ioc.ioc import IOC
from pipeline.models.event import NormalizedEvent


class CommandExtractor(BaseIOCExtractor):
    """
    Extract executed command indicators.
    """

    def extract(
        self,
        event: NormalizedEvent,
    ) -> IOC | None:

        command = event.metadata.get("command")

        if not command:
            return None

        return IOC(
            indicator_type="command",
            value=command,
            first_seen=event.sensor_time,
            last_seen=event.sensor_time,
            metadata={
                "protocol": event.protocol,
            },
        )
