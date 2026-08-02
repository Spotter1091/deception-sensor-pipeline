from __future__ import annotations

from pipeline.verification.replay_verification import ReplayVerification


class ReplayVerifier:
    """
    Verifies the level of reconstruction supported by the
    supplied replay dataset.

    This verifier intentionally does not fabricate protocol
    byte streams that are absent from the replay.
    """

    def verify(self) -> ReplayVerification:

        return ReplayVerification(
            verification="partial",
            session_reconstruction=True,
            byte_reconstruction=False,
            reason=(
                "The supplied replay dataset preserves protocol "
                "metadata, timestamps, session identifiers, byte "
                "counts and payload hashes, but does not preserve "
                "raw protocol payload bytes. Therefore byte-for-byte "
                "reconstruction cannot be performed."
            ),
            verified_fields=[
                "sensor_time",
                "connection_id",
                "protocol",
                "action",
                "username",
                "payload_sha256",
                "bytes",
            ],
        )
