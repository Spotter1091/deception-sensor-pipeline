from __future__ import annotations

from pydantic import BaseModel


class EvidenceClaim(BaseModel):
    """
    Represents one row in evidence-index.csv.
    """

    claim_id: str
    report_section: str
    claim: str
    artifact_path: str
    exact_locator: str
    collection_time_utc: str
    sha256: str
    proves: str
    does_not_prove: str
    confidence: str
    alternative_considered: str
    disposition: str
