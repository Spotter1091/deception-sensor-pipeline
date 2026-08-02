from __future__ import annotations

from pydantic import BaseModel


class SubmissionMetadata(BaseModel):
    """
    Metadata describing the assessment submission.
    """

    intern_code: str
    variant: str
    evidence_marker: str
    signed_name: str
    assistance: str
