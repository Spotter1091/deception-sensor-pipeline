from pathlib import Path

from pipeline.adapters.replay_adapter import ReplayAdapter


def main() -> None:
    replay = Path("replay/raw/honeypot-replay.jsonl")

    adapter = ReplayAdapter(replay)

    for index, event in enumerate(adapter.events(), start=1):
        print(event)

        if index == 5:
            break


if __name__ == "__main__":
    main()
