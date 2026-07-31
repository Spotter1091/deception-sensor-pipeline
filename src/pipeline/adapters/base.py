from abc import ABC, abstractmethod
from collections.abc import Iterator


from pipeline.models.event import NormalizedEvent


class BaseAdapter(ABC):
    """
    Base class for all ingestion adapters.
    """

    @abstractmethod
    def events(self) -> Iterator[NormalizedEvent]:
        """
        Yield normalized events one at a time.
        """
        raise NotImplementedError
