from __future__ import annotations

from pathlib import Path

from pipeline.session_analysis.session_analysis import SessionAnalysis


class SessionAnalysisExporter:
    """
    Exports one replay-derived session analysis using the
    assessment markdown template.
    """

    def export(
        self,
        destination: Path,
        analysis: SessionAnalysis,
    ) -> None:

        destination.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        with destination.open(
            "w",
            encoding="utf-8",
        ) as output:
            output.write("# Honeypot Session Analysis\n\n")

            output.write(f"Session ID: {analysis.session_id}\n")
            output.write(f"Sensor / honeypot: {analysis.sensor}\n")
            output.write(
                f"First / last UTC event: {analysis.first_utc} → {analysis.last_utc}\n"
            )
            output.write(f"Assigned evidence marker: {analysis.evidence_marker}\n\n")

            output.write("## Evidence chain\n\n")

            output.write(
                "| Step | UTC | Raw artifact + locator | "
                "Observed action | Interpretation | "
                "Confidence | Alternative |\n"
            )

            output.write("|---|---|---|---|---|---|---|\n")

            for step in analysis.evidence_chain:
                output.write(
                    f"| {step.step} "
                    f"| {step.utc} "
                    f"| {step.raw_locator} "
                    f"| {step.observed_action} "
                    f"| {step.interpretation} "
                    f"| {step.confidence} "
                    f"| {step.alternative} |\n"
                )

            output.write("\n## Intent assessment\n\n")
            output.write(analysis.intent_assessment)
            output.write("\n\n")

            output.write("## ATT&CK mapping\n\n")

            if analysis.attack_mapping:
                for item in analysis.attack_mapping:
                    output.write(f"- {item}\n")
            else:
                output.write("No ATT&CK mapping derived from replay evidence.\n")

            output.write("\n## Indicator handling\n\n")

            if analysis.indicators:
                for indicator in analysis.indicators:
                    output.write(f"- {indicator}\n")
            else:
                output.write("No additional indicators recorded.\n")

            output.write("\n## Defensive action\n\n")

            if analysis.defensive_actions:
                for action in analysis.defensive_actions:
                    output.write(f"- {action}\n")
            else:
                output.write("No defensive recommendation generated.\n")
