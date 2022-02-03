from __future__ import annotations

from typing import Any

from app.types.workflow import WorkflowFactory

workflow_factory = WorkflowFactory()


def get_workflows_ids() -> list[str]:
    return workflow_factory.get_workflows()


def get_workflow_by_name(name: str) -> Any:
    return workflow_factory.get_workflow_by_name(name)
