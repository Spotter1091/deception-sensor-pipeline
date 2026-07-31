from pathlib import Path

from typing import Iterator

import json

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

                record = json.loads(line)

                yield self._normalize(record)

    def _normalize(
        self,
        record: dict,
    ) -> NormalizedEvent:
        """
        Convert one replay record into
        a NormalizedEvent.
        """

        raise NotImplementedError


class ReplayAdapter:
    """
    Streams Stage 6 replay events from a JSONL file.
    """

    def __init__(self, replay_file: Path):
        self.replay_file = replay_file

    def events(self) -> Iterator[NormalizedEvent]:
        raise NotImplementedError
