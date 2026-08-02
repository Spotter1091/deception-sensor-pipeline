from __future__ import annotations

from abc import ABC, abstractmethod

from pipeline.ioc.ioc import IOC
from pipeline.models.event import NormalizedEvent


class BaseIOCExtractor(ABC):
    """
    Base class for IOC extractors.
    """

    @abstractmethod
    def extract(
        self,
        event: NormalizedEvent,
    ) -> IOC | None:
        """
        Return an IOC if one can be extracted.
        """
        raise NotImplementedError
