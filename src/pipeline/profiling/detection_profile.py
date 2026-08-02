from __future__ import annotations

from pydantic import BaseModel


class DetectionProfile(BaseModel):
    """
    Statistical summary of replay-derived evidence.

    Used to drive Sigma and Suricata generation.
    """

    total_events: int

    total_sessions: int

    total_clusters: int

    total_payloads: int

    total_iocs: int

    protocols: dict[str, int]

    destination_ports: dict[int, int]

    usernames: dict[str, int]

    ioc_types: dict[str, int]
