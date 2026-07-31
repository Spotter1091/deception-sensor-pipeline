from __future__ import annotations

from datetime import datetime
from typing import Any, Optional

from pydantic import BaseModel, Field


class NormalizedEvent(BaseModel):
    """
    Canonical normalized event consumed by the Stage 6 pipeline.

    Every adapter (sealed replay or live T-Pot export)
    must emit this structure.
    """

    # ---------- Identity ----------

    event_id: str
    schema_version: str = "1.0"
    source_adapter: str

    # ---------- Time ----------

    sensor_time: datetime
    normalized_time: datetime

    # ---------- Session ----------

    connection_id: Optional[str] = None

    # ---------- Network ----------

    protocol: str

    source_ip: str
    source_port: Optional[int] = None

    destination_ip: str = "unknown"
    destination_port: Optional[int] = None

    # ---------- Credentials ----------

    username: Optional[str] = None
    password: Optional[str] = None

    # ---------- Payload ----------

    payload_sha256: Optional[str] = None
    payload_md5: Optional[str] = None
    payload_size: Optional[int] = None

    quarantine_path: Optional[str] = None

    # ---------- Provenance ----------

    raw_file: str

    raw_locator: str

    # ---------- Enrichment ----------

    attack_technique: Optional[str] = None

    reputation: Optional[str] = None

    # ---------- Metadata ----------

    metadata: dict[str, Any] = Field(default_factory=dict)
