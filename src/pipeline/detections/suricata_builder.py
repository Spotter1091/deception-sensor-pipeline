from __future__ import annotations

from pipeline.detections.suricata_rule import SuricataRule
from pipeline.ioc.ioc import IOC
from pipeline.models.cluster import Cluster
from pipeline.models.payload import PayloadRecord
from pipeline.models.session import Session


class SuricataBuilder:
    """
    Builds replay-derived Suricata IDS rules.
    """

    def build(
        self,
        sessions: list[Session],
        clusters: list[Cluster],
        iocs: list[IOC],
        payloads: list[PayloadRecord],
    ) -> list[SuricataRule]:

        rules: list[SuricataRule] = []

        seen: set[tuple[str, str]] = set()

        sid = 1000001

        for session in sessions:
            key = (
                session.protocol,
                session.source_ip,
            )

            if key in seen:
                continue

            seen.add(key)

            rules.append(
                SuricataRule(
                    sid=sid,
                    message=("Replay source activity"),
                    protocol=session.protocol.lower(),
                    source=session.source_ip,
                    source_port="any",
                    direction="->",
                    destination="$HOME_NET",
                    destination_port="any",
                    options=[
                        f'msg:"Replay activity from {session.source_ip}"',
                        "flow:established,to_server",
                        f"sid:{sid}",
                        "rev:1",
                    ],
                )
            )

            sid += 1

        return rules
