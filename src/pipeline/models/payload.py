from __future__ import annotations

from pydantic import BaseModel


class PayloadRecord(BaseModel):
    """
    Represents a quarantined payload reference.

    No binary is ever executed.
    """

    sha256: str

    source_event: str

    protocol: str

    source_ip: str

    payload_size: int | None = None
