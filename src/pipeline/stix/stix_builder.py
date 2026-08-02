from __future__ import annotations

from collections.abc import Iterable

from pipeline.ioc.ioc import IOC
from pipeline.stix.bundle_builder import BundleBuilder
from pipeline.stix.indicator_builder import IndicatorBuilder


class STIXBuilder:
    """
    Build a complete STIX Bundle
    from extracted IOCs.
    """

    def __init__(self) -> None:

        self.indicator_builder = IndicatorBuilder()

        self.bundle_builder = BundleBuilder()

    def build(
        self,
        iocs: Iterable[IOC],
    ) -> dict:

        indicators = []

        for ioc in iocs:
            indicators.append(self.indicator_builder.build(ioc))

        return self.bundle_builder.build(indicators)
