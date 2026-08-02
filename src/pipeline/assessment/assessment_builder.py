from __future__ import annotations

from pipeline.assessment.assessment_manifest import AssessmentManifest


class AssessmentManifestBuilder:
    """
    Builds the machine-readable assessment manifest.
    """

    def __init__(
        self,
        *,
        commit: str,
        assigned_pack: dict,
        environment: dict,
        commands: dict,
        results: dict,
        inputs: list[str],
        outputs: list[str],
        manual_preconditions: list[str],
        known_limitations: list[str],
        project_id: str = "SOC-A1",
        variant: str = "V1",
    ):
        self.commit = commit
        self.assigned_pack = assigned_pack
        self.environment = environment
        self.commands = commands
        self.results = results
        self.inputs = inputs
        self.outputs = outputs
        self.manual_preconditions = manual_preconditions
        self.known_limitations = known_limitations
        self.project_id = project_id
        self.variant = variant

    def build(
        self,
    ) -> AssessmentManifest:
        """
        Assemble the assessment manifest.
        """

        return AssessmentManifest(
            schema_version="1.0",
            project_id=self.project_id,
            variant=self.variant,
            candidate_binding="from-assigned-participant-pack",
            assigned_pack=self.assigned_pack,
            commit=self.commit,
            supported_environment=self.environment,
            commands=self.commands,
            results=self.results,
            inputs=self.inputs,
            outputs=self.outputs,
            manual_preconditions=self.manual_preconditions,
            known_limitations=self.known_limitations,
        )
