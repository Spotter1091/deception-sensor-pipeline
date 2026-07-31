from __future__ import annotations

from datetime import datetime
from typing import Any

from pydantic import BaseModel, Field


class IOC(BaseModel):
    """
    Represents one Indicator of Compromise extracted
    from replay or live deception telemetry.
    """

    indicator_type: str

    value: str

    first_seen: datetime
    last_seen: datetime

    source_count: int = 1

    confidence: int = 50

    metadata: dict[str, Any] = Field(default_factory=dict)
