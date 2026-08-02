from __future__ import annotations

import json
from dataclasses import asdict
from pathlib import Path

from pipeline.isolation.isolation_result import (
    IsolationResult,
)


class IsolationExporter:
    """
    Writes isolation results to JSON.
    """

    def export(
        self,
        output_file: Path,
        results: list[IsolationResult],
    ) -> None:

        output_file.write_text(
            json.dumps(
                [asdict(result) for result in results],
                indent=2,
            ),
            encoding="utf-8",
        )
