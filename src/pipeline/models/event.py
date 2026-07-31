from __future__ import annotations

from datetime import datetime
from typing import Any

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

    connection_id: str | None = None

    # ---------- Network ----------

    protocol: str

    source_ip: str
    source_port: int | None = None

    destination_ip: str = "unknown"
    destination_port: int | None = None

    # ---------- Credentials ----------

    username: str | None = None
    password: str | None = None

    # ---------- Payload ----------

    payload_sha256: str | None = None
    payload_md5: str | None = None
    payload_size: int | None = None

    quarantine_path: str | None = None

    # ---------- Provenance ----------

    raw_file: str

    raw_locator: str

    # ---------- Enrichment ----------

    attack_technique: str | None = None

    reputation: str | None = None

    # ---------- Metadata ----------

    metadata: dict[str, Any] = Field(default_factory=dict)
