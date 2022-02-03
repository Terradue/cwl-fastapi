from __future__ import annotations
from typing import Any

from fastapi import APIRouter, Depends

from app.apis.runners import get_runner_by_name, get_runners
from app.apis.workflows import get_workflow_by_name
from app.core.auth import get_current_user
from app.types.runners import RunnerDefinition

router = APIRouter()


@router.get("/runners", tags=["runners"], response_model=list[RunnerDefinition])
async def runners(
    # auth: Depends = Depends(get_current_user),
) -> list[RunnerDefinition]:
    """Get the available runners of this instance"""
    return get_runners()


@router.get("/runners/{name}", tags=["runners"], response_model=RunnerDefinition)
async def runner_by_name(
    name: str,
    # auth: Depends = Depends(get_current_user),
) -> RunnerDefinition:
    """Get the detail of a specific runner"""
    return get_runner_by_name(name)


@router.get("/workflows", tags=["workflows"])
async def jobs(
    num: int,
    auth: Depends = Depends(get_current_user),
) -> dict[str, int]:
    return get_workflows(num)

@router.get("/workflows/{name}", tags=["workflows"], response_model=Any)
async def workflow_by_name(
    name: str,
    # auth: Depends = Depends(get_current_user),
) -> Any:
    """Get the detail of a specific runner"""
    return get_workflow_by_name(name)
