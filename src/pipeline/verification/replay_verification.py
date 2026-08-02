from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class ReplayVerification:
    """
    Documents the verification status of a reconstructed replay session.

    The supplied replay dataset preserves protocol metadata,
    timestamps, session identifiers, payload hashes, and byte counts,
    but does not preserve raw protocol byte streams.

    Therefore byte-for-byte reconstruction may not be possible.
    """

    verification: str

    session_reconstruction: bool

    byte_reconstruction: bool

    reason: str

    verified_fields: list[str] = field(default_factory=list)
