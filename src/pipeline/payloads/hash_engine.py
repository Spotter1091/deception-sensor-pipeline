from __future__ import annotations

from pipeline.models.event import NormalizedEvent
from pipeline.models.payload import PayloadRecord


class HashEngine:
    """
    Builds the Stage 6 payload hash ledger.
    """

    def build_hash_ledger(
        self,
        events: list[NormalizedEvent],
    ) -> list[PayloadRecord]:

        ledger = []

        for event in events:

            if not event.payload_sha256:
                continue

            ledger.append(
                PayloadRecord(
                    sha256=event.payload_sha256,
                    source_event=event.event_id,
                    protocol=event.protocol,
                    source_ip=event.source_ip,
                    payload_size=event.payload_size,
                )
            )

        return ledger
