from __future__ import annotations

from collections import defaultdict

from pipeline.models.event import NormalizedEvent
from pipeline.models.session import Session


class SessionEngine:
    """
    Groups normalized events into protocol sessions.
    """

    def build_sessions(
        self,
        events: list[NormalizedEvent],
    ) -> list[Session]:

        grouped: dict[
            tuple[str | None, str, str],
            list[NormalizedEvent],
        ] = defaultdict(list)

        # Group events
        for event in events:

            key = (
                event.connection_id,
                event.source_ip,
                event.protocol,
            )

            grouped[key].append(event)

        sessions: list[Session] = []

        # Build Session objects
        for session_events in grouped.values():

            session_events.sort(key=lambda e: e.sensor_time)

            first = session_events[0]
            last = session_events[-1]

            sessions.append(
                Session(
                    session_id=(first.connection_id or first.event_id),
                    protocol=first.protocol,
                    connection_id=first.connection_id,
                    source_ip=first.source_ip,
                    start_time=first.sensor_time,
                    end_time=last.sensor_time,
                    events=session_events,
                    event_count=len(session_events),
                )
            )

        return sessions
