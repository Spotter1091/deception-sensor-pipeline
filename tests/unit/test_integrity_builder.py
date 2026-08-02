from pipeline.integrity.integrity_builder import IntegrityBuilder
from pipeline.integrity.submission_metadata import (
    SubmissionMetadata,
)


def test_integrity_builder():

    metadata = SubmissionMetadata(
        intern_code="UBI-2026-0187",
        variant="A6",
        evidence_marker="UBI-A6-4BA080E6A156",
        signed_name="Adedayo",
        assistance="Python, ChatGPT",
    )

    document = IntegrityBuilder().build(metadata)

    assert "Integrity Attestation" in document
    assert "UBI-2026-0187" in document
    assert "A6" in document
    assert "Adedayo" in document
    assert "Python, ChatGPT" in document
