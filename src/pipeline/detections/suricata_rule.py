from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class SuricataRule:
    """
    Represents one generated Suricata IDS rule.
    """

    sid: int

    message: str

    protocol: str

    source: str

    source_port: str

    direction: str

    destination: str

    destination_port: str

    options: list[str] = field(default_factory=list)
