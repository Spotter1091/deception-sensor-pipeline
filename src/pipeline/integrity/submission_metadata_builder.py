from __future__ import annotations

from pipeline.integrity.submission_metadata import (
    SubmissionMetadata,
)


class SubmissionMetadataBuilder:
    """
    Builds submission metadata used across
    assessment deliverables.
    """

    def build(
        self,
    ) -> SubmissionMetadata:

        return SubmissionMetadata(
            intern_code="UBI-2026-0187",
            variant="A6",
            evidence_marker="UBI-A6-4BA080E6A156",
            signed_name="Adedayo",
            assistance=(
                "Python 3.13, PyArrow, DuckDB, "
                "Pydantic, ChatGPT (architecture guidance, "
                "debugging, explanations, and code review)"
            ),
        )
