from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field

from pipeline.models.event import NormalizedEvent


class Session(BaseModel):
    """
    Represents one reconstructed protocol session.

    A session contains one or more normalized events that belong
    to the same network conversation.
    """

    # ---------- Identity ----------

    session_id: str

    # ---------- Classification ----------

    protocol: str

    connection_id: Optional[str] = None

    source_ip: str

    # ---------- Timing ----------

    start_time: datetime

    end_time: datetime

    # ---------- Contents ----------

    events: list[NormalizedEvent] = Field(default_factory=list)

    # ---------- Derived ----------

    event_count: int = 0
