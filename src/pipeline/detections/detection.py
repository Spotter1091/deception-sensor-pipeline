from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class Detection:
    """
    Common detection representation generated from
    replay-derived normalized events.
    """

    title: str

    description: str

    source: str

    detection_type: str

    level: str

    references: list[str] = field(default_factory=list)

    tags: list[str] = field(default_factory=list)

    iocs: list[str] = field(default_factory=list)
