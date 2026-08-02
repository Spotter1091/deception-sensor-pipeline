from __future__ import annotations

from datetime import UTC, datetime

from pipeline.integrity.submission_metadata import (
    SubmissionMetadata,
)


class IntegrityBuilder:
    """
    Builds the integrity attestation document
    required for assessment submission.
    """

    def build(
        self,
        metadata: SubmissionMetadata,
    ) -> str:

        timestamp = (
            datetime.now(UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z")
        )

        return f"""# Integrity Attestation

Intern code: {metadata.intern_code}
Variant: {metadata.variant}
Evidence marker: {metadata.evidence_marker}

I attest that I performed the submitted work on the assigned authorized
artifacts or lab. I have declared material assistance below and can reproduce
the work during artifact check. I did not alter raw evidence, fabricate tool
output, rewrite commit history, share restricted artifacts, or cross scope.

Assistance and tools used:
{metadata.assistance}

Signed name: {metadata.signed_name}
UTC date/time: {timestamp}
"""
