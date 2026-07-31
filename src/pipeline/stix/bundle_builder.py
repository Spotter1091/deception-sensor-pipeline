from __future__ import annotations

from uuid import uuid4


class BundleBuilder:
    """
    Build a STIX 2.1 Bundle.
    """

    def build(
        self,
        objects: list[dict],
    ) -> dict:

        return {
            "type": "bundle",
            "id": f"bundle--{uuid4()}",
            "spec_version": "2.1",
            "objects": objects,
        }
