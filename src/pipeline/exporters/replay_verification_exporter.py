from __future__ import annotations

import json
from dataclasses import asdict
from pathlib import Path

from pipeline.verification.replay_verification import ReplayVerification


class ReplayVerificationExporter:
    """
    Writes replay verification results.
    """

    def export(
        self,
        verification: ReplayVerification,
        output_file: Path,
    ) -> None:

        output_file.write_text(
            json.dumps(
                asdict(verification),
                indent=2,
            ),
            encoding="utf-8",
        )
