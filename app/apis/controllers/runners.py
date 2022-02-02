from __future__ import annotations

from app.types.runners import RunnerDefinition, RunnerFactory

runner_factory = RunnerFactory()


def get_runners() -> list[RunnerDefinition]:
    return runner_factory.get_runners()


def get_runner_by_name(name: str) -> RunnerDefinition:
    return runner_factory.get_runner_by_name(name)
