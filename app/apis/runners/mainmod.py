from __future__ import annotations

from app.types.runners import RunnerFactory, Runner

runner_factory = RunnerFactory()

def get_runners() -> list[Runner]:
    return runner_factory.get_runners()
