from __future__ import annotations

from collections import defaultdict

from pipeline.models.cluster import Cluster
from pipeline.models.session import Session


class ClusterEngine:
    """
    Groups related sessions into infrastructure clusters.
    """

    def build_clusters(
        self,
        sessions: list[Session],
    ) -> list[Cluster]:

        grouped = defaultdict(list)

        for session in sessions:

            username = None

            for event in session.events:
                if event.username:
                    username = event.username
                    break

            key = (
                session.protocol,
                session.source_ip,
                username,
            )

            grouped[key].append(session)

        clusters = []

        for (
            protocol,
            source_ip,
            username,
        ), grouped_sessions in grouped.items():

            cluster = Cluster(
                cluster_id=f"{protocol}:{source_ip}:{username}",

                protocol=protocol,

                source_ip=source_ip,

                username=username,

                sessions=grouped_sessions,

                session_count=len(grouped_sessions),
            )

            clusters.append(cluster)

        return clusters

    def serialize(
        self,
        clusters: list[Cluster],
    ) -> list[dict]:

        return [
            cluster.model_dump(mode="json")
            for cluster in clusters
        ]
