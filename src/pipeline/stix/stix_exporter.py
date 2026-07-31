from __future__ import annotations

import json
from pathlib import Path


class STIXExporter:
    """
    Writes STIX bundles to disk.
    """

    def export(
        self,
        output: Path,
        bundle: dict,
    ) -> None:

        output.write_text(
            json.dumps(
                bundle,
                indent=2,
            )
        )

