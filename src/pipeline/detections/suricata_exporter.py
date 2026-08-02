from __future__ import annotations

from pathlib import Path

from pipeline.detections.suricata_rule import SuricataRule


class SuricataExporter:
    """
    Exports generated Suricata IDS rules.

    Each SuricataRule becomes one rule in a .rules file.
    """

    def export(
        self,
        destination: Path,
        rules: list[SuricataRule],
    ) -> None:

        destination.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        with destination.open(
            "w",
            encoding="utf-8",
        ) as output:
            for rule in rules:
                options = "; ".join(rule.options)

                output.write(
                    f"alert {rule.protocol} "
                    f"{rule.source} {rule.source_port} "
                    f"{rule.direction} "
                    f"{rule.destination} {rule.destination_port} "
                    f"({options};)\n"
                )
