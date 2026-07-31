from pathlib import Path

from pipeline.adapters.replay_adapter import ReplayAdapter


def test_adapter_initializes():

    replay = Path("replay/raw/honeypot-replay.jsonl")

    adapter = ReplayAdapter(replay)

    assert adapter.replay_file == replay
