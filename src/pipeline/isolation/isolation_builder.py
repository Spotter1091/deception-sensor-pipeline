from __future__ import annotations

from pipeline.isolation.isolation_result import IsolationResult
from pipeline.models.payload import PayloadRecord


class IsolationBuilder:
    """
    Builds the isolation report for quarantined payloads.

    Payloads are never executed. Isolation is documented
    using metadata only.
    """

    def build(
        self,
        payloads: list[PayloadRecord],
    ) -> list[IsolationResult]:

        report: list[IsolationResult] = []

        for payload in payloads:
            report.append(
                IsolationResult(
                    payload_sha256=payload.sha256,
                    source_event=payload.source_event,
                    protocol=payload.protocol,
                    source_ip=payload.source_ip,
                    size_bytes=payload.payload_size or 0,
                    quarantined=True,
                    executed=False,
                    status="isolated",
                )
            )

        return report
