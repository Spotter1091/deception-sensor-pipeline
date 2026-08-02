from __future__ import annotations

from pydantic import BaseModel


class ManifestEntry(BaseModel):
    """
    Represents one line in manifest.sha256.
    """

    filename: str
    sha256: str
