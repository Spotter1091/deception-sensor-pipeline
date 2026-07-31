from __future__ import annotations

from typing import Iterable

from pipeline.models.cluster import Cluster


class STIXBuilder:
    """
    Builds STIX-like objects from clusters.

    We'll evolve this into a complete STIX 2.1 builder
    over the next milestones.
    """

    def build(
        self,
        clusters: Iterable[Cluster],
    ) -> list[dict]:

        return [
            self._cluster_indicator(cluster)
            for cluster in clusters
        ]

    def _cluster_indicator(
        self,
        cluster: Cluster,
    ) -> dict:

        return {
            "type": "indicator",
            "name": f"Cluster {cluster.cluster_id}",
            "pattern_type": "stix",
            "pattern": (
                f"[ipv4-addr:value = '{cluster.source_ip}']"
            ),
            "labels": [
                cluster.protocol,
            ],
            "description": (
                f"{cluster.session_count} sessions"
            ),
        }
