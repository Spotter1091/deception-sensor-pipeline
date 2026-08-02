from __future__ import annotations

from pydantic import BaseModel


class ContinuityRecord(BaseModel):
    """
    Documents engineering continuity between
    assessment stages.
    """

    previous_stage_commit: str
    reused_component: str

    consumed_interface: str
    backward_compatible_extension: str

    provenance_evidence: str

    migration_record: str

    next_stage_handoff: str
