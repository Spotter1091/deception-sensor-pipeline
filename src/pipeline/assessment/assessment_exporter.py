from __future__ import annotations

import json
from dataclasses import asdict
from pathlib import Path

from pipeline.assessment.assessment_manifest import (
    AssessmentManifest,
)


class AssessmentManifestExporter:
    """
    Writes the assessment manifest to disk.
    """

    def export(
        self,
        manifest: AssessmentManifest,
        destination: Path,
    ) -> None:

        destination.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        with destination.open(
            "w",
            encoding="utf-8",
        ) as handle:
            json.dump(
                asdict(manifest),
                handle,
                indent=2,
            )
            handle.write("\n")
