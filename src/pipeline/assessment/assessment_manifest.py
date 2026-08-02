from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class AssessmentManifest:
    """
    Machine-readable assessment submission manifest.
    """

    schema_version: str

    project_id: str

    variant: str

    candidate_binding: str

    assigned_pack: dict

    commit: str

    supported_environment: dict

    commands: dict

    results: dict

    inputs: list[str]

    outputs: list[str]

    manual_preconditions: list[str]

    known_limitations: list[str]
