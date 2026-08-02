from __future__ import annotations

from pathlib import Path

from pipeline.artifacts.registry import ExportRegistry
from pipeline.stix.stix_builder import STIXBuilder


class ArtifactManager:
    """
    Coordinates every artifact produced
    by the pipeline.
    """

    def __init__(
        self,
        output_directory: Path,
    ) -> None:

        self.output_directory = output_directory

        self.output_directory.mkdir(
            exist_ok=True,
        )

        self.registry = ExportRegistry()

    def export_all(
        self,
        *,
        ledger,
        clusters,
        iocs,
        sessions,
        isolation,
    ) -> None:

        stix_bundle = STIXBuilder().build(iocs)

        for exporter, filename in self.registry.exporters:
            output = self.output_directory / filename

            if filename == "hash-ledger.csv":
                exporter.export(output, ledger)

            elif filename == "sessions.parquet":
                exporter.export(output, sessions)

            elif filename == "clusters.json":
                exporter.export(output, clusters)

            elif filename == "isolation-results.json":
                exporter.export(output, isolation)

            elif filename == "stix-bundle.json":
                exporter.export(output, stix_bundle)

            elif filename == "iocs.csv":
                exporter.export(output, iocs)
