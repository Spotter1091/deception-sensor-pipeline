from pathlib import Path

from pipeline.adapters.replay_adapter import ReplayAdapter
from pipeline.artifacts.artifact_manager import ArtifactManager
from pipeline.clustering.cluster_engine import ClusterEngine
from pipeline.ioc.ioc_engine import IOCEngine
from pipeline.payloads.hash_engine import HashEngine
from pipeline.provenance.provenance_tracker import ProvenanceTracker
from pipeline.sessionization.session_engine import SessionEngine


def main() -> None:

    replay = Path("replay/raw/honeypot-replay.jsonl")

    adapter = ReplayAdapter(replay)

    print("[1/5] Reading replay...")

    events = list(adapter.events())

    print(f"Loaded {len(events):,} events")

    print("[2/5] Building sessions...")

    sessions = SessionEngine().build_sessions(events)

    print(f"Built {len(sessions):,} sessions")

    print("[3/5] Building clusters...")

    cluster_engine = ClusterEngine()

    clusters = cluster_engine.build_clusters(sessions)

    print(f"Built {len(clusters):,} clusters")

    print("[4/5] Building payload ledger...")

    ledger = HashEngine().build_hash_ledger(events)
    
    print("[4.5/5] Extracting IOCs...")

    iocs = IOCEngine().extract(events)

    print(f"Extracted {len(iocs):,} unique IP indicators")
	
    output_dir = Path("derived")

    output_dir.mkdir(
        exist_ok=True,
    )

    ArtifactManager(
        output_directory=Path("derived"),
    ).export_all(
        ledger=ledger,
        clusters=clusters,
        sessions=sessions,
        iocs=iocs,
    )

    print("Artifacts exported.")

    print("Exported sessions.parquet")

    print("Exported clusters.json")

    print(f"Recorded {len(ledger):,} payload hashes")

    print("[5/5] Building provenance...")

    tracker = ProvenanceTracker()

    if sessions:
        tracker.session_to_record(sessions[0])

    print("Pipeline completed successfully.")


if __name__ == "__main__":
    main()
