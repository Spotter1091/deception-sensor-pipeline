from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class SigmaRule:
    """
    Represents a Sigma detection rule generated
    from replay-derived normalized events.
    """

    title: str

    identifier: str

    description: str

    status: str

    logsource: dict

    detection: dict

    level: str

    tags: list[str] = field(default_factory=list)

    references: list[str] = field(default_factory=list)
