from __future__ import annotations

from pipeline.models.event import NormalizedEvent
from pipeline.models.session import Session


class ProvenanceTracker:
    """
    Maintains lineage from raw replay events to derived objects.
    """

    def event_to_record(
        self,
        event: NormalizedEvent,
    ) -> dict:

        return {
            "event_id": event.event_id,
            "raw_file": event.raw_file,
            "raw_locator": event.raw_locator,
        }

    def session_to_record(
        self,
        session: Session,
    ) -> dict:

        return {
            "session_id": session.session_id,
            "events": [self.event_to_record(event) for event in session.events],
        }
