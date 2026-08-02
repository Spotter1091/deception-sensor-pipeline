from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class EvidenceStep:
    """
    One step in the reconstructed session timeline.
    """

    step: int
    utc: str
    raw_locator: str
    observed_action: str
    interpretation: str
    confidence: str
    alternative: str


@dataclass(slots=True)
class SessionAnalysis:
    """
    Represents one replay-derived session analysis.
    """

    session_id: str
    sensor: str
    first_utc: str
    last_utc: str
    evidence_marker: str

    evidence_chain: list[EvidenceStep] = field(default_factory=list)

    intent_assessment: str = ""

    attack_mapping: list[str] = field(default_factory=list)

    indicators: list[str] = field(default_factory=list)

    defensive_actions: list[str] = field(default_factory=list)
