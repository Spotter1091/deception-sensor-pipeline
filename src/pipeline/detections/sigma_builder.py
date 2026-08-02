from __future__ import annotations

from pipeline.detections.sigma_rule import SigmaRule
from pipeline.ioc.ioc import IOC
from pipeline.models.cluster import Cluster
from pipeline.models.payload import PayloadRecord
from pipeline.models.session import Session


class SigmaBuilder:
    """
    Builds Sigma detection rules from replay-derived
    analytical outputs.
    """

    def build(
        self,
        sessions: list[Session],
        clusters: list[Cluster],
        iocs: list[IOC],
        payloads: list[PayloadRecord],
    ) -> list[SigmaRule]:

        rules: list[SigmaRule] = []

        # Collect source IPs from reconstructed sessions.
        source_ips = {session.source_ip for session in sessions if session.source_ip}

        if source_ips:
            rules.append(
                SigmaRule(
                    title="Replay Source IP Activity",
                    identifier="SIGMA-0001",
                    description=(
                        "Detect activity originating from "
                        "source IPs observed in replay-derived sessions."
                    ),
                    status="experimental",
                    logsource={
                        "category": "network_connection",
                        "product": "linux",
                    },
                    detection={
                        "selection": {
                            "source_ip": sorted(source_ips),
                        },
                        "condition": "selection",
                    },
                    level="medium",
                    tags=[
                        "network",
                        "replay",
                    ],
                    references=[
                        "Derived from replay session analysis.",
                    ],
                )
            )

        return rules
