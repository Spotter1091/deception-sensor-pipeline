from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from pipeline.exporters.base import BaseExporter


class JSONExporter(BaseExporter):
    """
    Writes JSON artifacts produced by the pipeline.
    """

    def export(
        self,
        output: Path,
        data: Any,
    ) -> None:

        with output.open(
            "w",
            encoding="utf-8",
        ) as outfile:
            json.dump(
                data,
                outfile,
                indent=2,
                default=str,
            )
