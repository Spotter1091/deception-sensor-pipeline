from __future__ import annotations

from uuid import uuid4

from pipeline.ioc.ioc import IOC


class IndicatorBuilder:
    """
    Builds STIX Indicator objects from IOCs.
    """

    def build(
        self,
        ioc: IOC,
    ) -> dict:

        pattern = self._pattern(ioc)

        return {
            "type": "indicator",
            "spec_version": "2.1",
            "id": f"indicator--{uuid4()}",
            "created": ioc.first_seen.isoformat(),
            "modified": ioc.last_seen.isoformat(),
            "valid_from": ioc.first_seen.isoformat(),
            "name": ioc.value,
            "description": (f"{ioc.indicator_type} extracted from deception telemetry"),
            "pattern_type": "stix",
            "pattern": pattern,
            "confidence": ioc.confidence,
            "labels": [
                ioc.indicator_type,
            ],
        }

    def _pattern(
        self,
        ioc: IOC,
    ) -> str:

        match ioc.indicator_type:
            case "ip":
                return f"[ipv4-addr:value = '{ioc.value}']"

            case "username":
                return f"[user-account:account_login = '{ioc.value}']"

            case "sha256":
                return f"[file:hashes.'SHA-256' = '{ioc.value}']"

            case "command":
                return f"[process:command_line = '{ioc.value}']"

            case _:
                return f"[x-observable:value = '{ioc.value}']"
