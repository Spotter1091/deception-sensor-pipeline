from pathlib import Path

from pipeline.adapters.replay_adapter import ReplayAdapter


def test_create_adapter():

    adapter = ReplayAdapter(
        Path("tests/fixtures/sample.jsonl")
    )

    assert adapter.replay_file.name == "sample.jsonl"
