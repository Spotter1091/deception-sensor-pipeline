from __future__ import annotations

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
            "name": ioc.value,
            "pattern_type": "stix",
            "pattern": pattern,
            "description": (
                f"{ioc.indicator_type} indicator"
            ),
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
                return (
                    f"[ipv4-addr:value = '{ioc.value}']"
                )

            case "username":
                return (
                    f"[user-account:account_login = '{ioc.value}']"
                )

            case "sha256":
                return (
                    "[file:hashes.'SHA-256' = "
                    f"'{ioc.value}']"
                )

            case "command":
                return (
                    "[process:command_line = "
                    f"'{ioc.value}']"
                )

            case _:
                return (
                    f"[x-observable:value = '{ioc.value}']"
                )
