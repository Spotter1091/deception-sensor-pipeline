from __future__ import annotations

from abc import ABC, abstractmethod
from pathlib import Path


class BaseExporter(ABC):
    """
    Base class for all export formats.
    """

    @abstractmethod
    def export(
        self,
        output: Path,
    ) -> None:
        """
        Write pipeline output.
        """
        raise NotImplementedError
