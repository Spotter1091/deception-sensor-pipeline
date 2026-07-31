from pathlib import Path

from pipeline.adapters.replay_adapter import ReplayAdapter
from pipeline.clustering.cluster_engine import ClusterEngine
from pipeline.payloads.hash_engine import HashEngine
from pipeline.sessionization.session_engine import SessionEngine


def test_pipeline():

    replay = Path("replay/raw/honeypot-replay.jsonl")

    adapter = ReplayAdapter(replay)

    events = list(adapter.events())

    sessions = SessionEngine().build_sessions(events)

    clusters = ClusterEngine().build_clusters(sessions)

    ledger = HashEngine().build_hash_ledger(events)

    assert len(events) > 0
    assert len(sessions) > 0
    assert len(clusters) > 0
    assert isinstance(ledger, list)
