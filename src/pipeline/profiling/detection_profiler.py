from __future__ import annotations

from collections import Counter

from pipeline.ioc.ioc import IOC
from pipeline.models.cluster import Cluster
from pipeline.models.event import NormalizedEvent
from pipeline.models.payload import PayloadRecord
from pipeline.models.session import Session
from pipeline.profiling.detection_profile import DetectionProfile


class DetectionProfiler:
    """
    Produces a statistical summary of replay evidence.
    """

    def build(
        self,
        *,
        events: list[NormalizedEvent],
        sessions: list[Session],
        clusters: list[Cluster],
        payloads: list[PayloadRecord],
        iocs: list[IOC],
    ) -> DetectionProfile:

        protocols: Counter[str] = Counter()
        destination_ports: Counter[int] = Counter()
        usernames: Counter[str] = Counter()
        ioc_types: Counter[str] = Counter()

        for event in events:
            protocols[event.protocol] += 1

            if event.destination_port is not None:
                destination_ports[event.destination_port] += 1

            if event.username:
                usernames[event.username] += 1

        for indicator in iocs:
            ioc_types[indicator.indicator_type] += 1

        return DetectionProfile(
            total_events=len(events),
            total_sessions=len(sessions),
            total_clusters=len(clusters),
            total_payloads=len(payloads),
            total_iocs=len(iocs),
            protocols=dict(protocols),
            destination_ports=dict(destination_ports),
            usernames=dict(usernames),
            ioc_types=dict(ioc_types),
        )
