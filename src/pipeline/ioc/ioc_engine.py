from __future__ import annotations

from pipeline.ioc.extractors.command import CommandExtractor
from pipeline.ioc.extractors.ip import IPExtractor
from pipeline.ioc.extractors.sha256 import SHA256Extractor
from pipeline.ioc.extractors.username import UsernameExtractor
from pipeline.ioc.ioc import IOC
from pipeline.models.event import NormalizedEvent


class IOCEngine:
    """
    Extract Indicators of Compromise (IOCs)
    from normalized events.
    """

    def extract(
        self,
        events: list[NormalizedEvent],
    ) -> list[IOC]:
        """
        Build IOC objects from replay events.
        """

        ioc_map: dict[tuple[str, str], IOC] = {}

        for event in events:

            for ioc in self._extract_all(event):

                key = (ioc.indicator_type, ioc.value)

                existing = ioc_map.get(key)

                if existing is None:
                    ioc_map[key] = ioc

                else:
                    existing.last_seen = event.sensor_time
                    existing.source_count += 1

        return list(ioc_map.values())


    def _extract_all(
        self,
        event: NormalizedEvent,
    ) -> list[IOC]:

        iocs: list[IOC] = []

        
        for extractor in self.extractors:

            indicator = extractor.extract(event)

            if indicator is not None:
                iocs.append(indicator)


        return iocs

    
    def __init__(self) -> None:

        self.extractors = [
            IPExtractor(),
            UsernameExtractor(),
            SHA256Extractor(),
            CommandExtractor(),
    ]
