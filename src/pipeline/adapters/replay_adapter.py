from __future__ import annotations

import json
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

from pipeline.adapters.base import BaseAdapter
from pipeline.models.event import NormalizedEvent


class ReplayAdapter(BaseAdapter):
    def __init__(self, replay_file: Path):
        self.replay_file = replay_file

    def events(self):
        with self.replay_file.open(
            "r",
            encoding="utf-8",
        ) as infile:
            for line in infile:
                if not line.strip():
                    continue

                record = json.loads(line)

                yield self._normalize(record)

    def _normalize(
        self,
        record: dict[str, Any],
    ) -> NormalizedEvent:

        sensor_time = datetime.fromisoformat(
            record["sensor_time"].replace("Z", "+00:00")
        )

        return NormalizedEvent(
            event_id=record["event_id"],
            schema_version=record["schema_version"],
            source_adapter="replay",
            sensor_time=sensor_time,
            normalized_time=datetime.now(UTC),
            connection_id=record.get("connection_id"),
            protocol=record["protocol"],
            source_ip=record["source_ip"],
            source_port=record.get("source_port"),
            destination_ip="unknown",
            destination_port=record.get("destination_port"),
            username=record.get("username"),
            payload_sha256=record.get("payload_sha256"),
            payload_size=record.get("bytes"),
            raw_file=str(self.replay_file),
            raw_locator=record["event_id"],
            metadata={
                "action": record.get("action"),
                "command": record.get("command"),
                "credential_fingerprint": record.get("credential_fingerprint"),
                "marker": record.get("marker"),
            },
        )
