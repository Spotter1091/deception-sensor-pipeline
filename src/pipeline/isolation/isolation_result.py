from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class IsolationResult:
    """
    Records the quarantine status of an observed payload.

    Payloads are never executed. They are handled only by
    cryptographic hash and metadata.
    """

    payload_sha256: str

    source_event: str

    protocol: str

    source_ip: str

    size_bytes: int

    quarantined: bool

    executed: bool

    status: str
