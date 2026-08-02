from __future__ import annotations

import json
from pathlib import Path


class STIXExporter:
    """
    Writes STIX bundles to disk.
    """

    def export(
        self,
        output_file: Path,
        bundle: list[dict],
    ) -> None:

        with output_file.open(
            "w",
            encoding="utf-8",
        ) as outfile:
            json.dump(
                bundle,
                outfile,
                indent=2,
            )
