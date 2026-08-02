from __future__ import annotations

from pathlib import Path

from pipeline.continuity.continuity_record import (
    ContinuityRecord,
)


class ContinuityExporter:
    """
    Writes the continuity record.
    """

    def export(
        self,
        output: Path,
        record: ContinuityRecord,
    ) -> None:

        output.write_text(
            f"""# Continuity Record

## 1. Previous-stage Commit and Reused Component

**Previous-stage commit**

{record.previous_stage_commit}

**Exact component reused**

{record.reused_component}

---

## 2. Interface Consumed and Backward-compatible Extension

**Interface consumed**

{record.consumed_interface}

**Backward-compatible extension**

{record.backward_compatible_extension}

---

## 3. Provenance Continuity

{record.provenance_evidence}

---

## 4. Migration Record

{record.migration_record}

---

## 5. Next-stage Handoff

{record.next_stage_handoff}
""",
            encoding="utf-8",
        )
