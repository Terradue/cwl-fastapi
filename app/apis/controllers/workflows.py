from __future__ import annotations

workflow_factory = WorkflowFactory()


def get_workflows() -> list[RunnerDefinition]:
    return workflow_factory.get_workflows()


def get_workflow_by_name(name: str) -> RunnerDefinition:
    client = redis.Redis(host="localhost", port=6379, db=0)
