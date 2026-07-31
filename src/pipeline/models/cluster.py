from __future__ import annotations

from pydantic import BaseModel, Field

from pipeline.models.session import Session


class Cluster(BaseModel):
    """
    Represents a group of related sessions.
    """

    cluster_id: str

    protocol: str

    source_ip: str

    username: str | None = None

    sessions: list[Session] = Field(default_factory=list)

    session_count: int = 0
