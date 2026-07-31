from __future__ import annotations

from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any


class BaseExporter(ABC):
    """
    Base class for all export formats.
    """

    @abstractmethod
    def export(
        self,
        output: Path,
        data: Any,
    ) -> None:
        """
        Write pipeline output.
        """
        raise NotImplementedError
