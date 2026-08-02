from __future__ import annotations

from pipeline.ioc.ioc import IOC
from pipeline.models.cluster import Cluster
from pipeline.models.payload import PayloadRecord
from pipeline.models.session import Session
from pipeline.session_analysis.session_analysis import (
    EvidenceStep,
    SessionAnalysis,
)


class SessionAnalysisBuilder:
    """
    Builds a replay-derived analytical report for one
    reconstructed session.
    """

    def build(
        self,
        *,
        session: Session,
        clusters: list[Cluster],
        iocs: list[IOC],
        payloads: list[PayloadRecord],
    ) -> SessionAnalysis:

        analysis = SessionAnalysis(
            session_id=session.session_id,
            sensor="Replay",
            first_utc=session.start_time.isoformat(),
            last_utc=session.end_time.isoformat(),
            evidence_marker="Replay",
        )

        # --------------------------------------------------
        # Infrastructure correlation
        # --------------------------------------------------

        cluster = next(
            (
                candidate
                for candidate in clusters
                if any(s.session_id == session.session_id for s in candidate.sessions)
            ),
            None,
        )

        # --------------------------------------------------
        # IOC correlation
        # --------------------------------------------------

        session_iocs = [
            indicator
            for indicator in iocs
            if (
                indicator.value == session.source_ip
                or any(
                    event.username == indicator.value
                    for event in session.events
                    if event.username
                )
            )
        ]

        # --------------------------------------------------
        # Payload correlation
        # --------------------------------------------------

        event_ids = {event.event_id for event in session.events}

        session_payloads = [
            payload for payload in payloads if payload.source_event in event_ids
        ]

        # --------------------------------------------------
        # Evidence chain
        # --------------------------------------------------

        for index, event in enumerate(session.events, start=1):
            actions: list[str] = [
                event.protocol.upper(),
            ]

            if event.username:
                actions.append(f"user={event.username}")

            if event.connection_id:
                actions.append(f"connection={event.connection_id}")

            if event.payload_sha256:
                actions.append("payload observed")

            analysis.evidence_chain.append(
                EvidenceStep(
                    step=index,
                    utc=event.sensor_time.isoformat(),
                    raw_locator=(f"{event.raw_file}:{event.raw_locator}"),
                    observed_action=", ".join(actions),
                    interpretation=(
                        "Replay event reconstructed from normalized telemetry."
                    ),
                    confidence="High",
                    alternative="None",
                )
            )

        # --------------------------------------------------
        # Intent assessment
        # --------------------------------------------------

        observations: list[str] = []

        protocols = sorted({event.protocol.upper() for event in session.events})

        if protocols:
            observations.append("Observed protocol(s): " + ", ".join(protocols))

        usernames = sorted(
            {event.username for event in session.events if event.username}
        )

        if usernames:
            observations.append("Credential activity observed.")

        if session_payloads:
            observations.append("Payload activity observed.")

        if cluster is not None:
            observations.append(
                f"Cluster {cluster.cluster_id} "
                f"contains "
                f"{cluster.session_count} "
                f"related session(s)."
            )

        if observations:
            analysis.intent_assessment = " ".join(observations)
        else:
            analysis.intent_assessment = (
                "No definitive operational intent "
                "could be established from the "
                "available replay evidence."
            )

        # --------------------------------------------------
        # ATT&CK mapping
        # --------------------------------------------------

        protocol_set = {event.protocol.lower() for event in session.events}

        if "telnet" in protocol_set:
            analysis.attack_mapping.append(
                "ATT&CK: T1021.001 - Remote Services: Telnet"
            )

        if "ssh" in protocol_set:
            analysis.attack_mapping.append("ATT&CK: T1021.004 - Remote Services: SSH")

        if session_payloads:
            analysis.attack_mapping.append("ATT&CK: T1105 - Ingress Tool Transfer")

        # --------------------------------------------------
        # Indicators
        # --------------------------------------------------

        for indicator in session_iocs:
            analysis.indicators.append(f"{indicator.indicator_type}: {indicator.value}")

        for payload in session_payloads:
            analysis.indicators.append(f"SHA256: {payload.sha256}")

        # --------------------------------------------------
        # Defensive recommendations
        # --------------------------------------------------

        analysis.defensive_actions.append("Retain replay evidence for forensic review.")

        if protocol_set:
            analysis.defensive_actions.append(
                "Deploy protocol-specific network detections."
            )

        if session_iocs:
            analysis.defensive_actions.append(
                "Monitor extracted indicators across security tooling."
            )

        if session_payloads:
            analysis.defensive_actions.append(
                "Verify payload quarantine and malware analysis workflow."
            )

        return analysis
