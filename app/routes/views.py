from __future__ import annotations
import json
import logging
from typing import Any
import yaml

from fastapi import APIRouter, Depends, HTTPException, Request

from app.apis.runners import get_runner_by_name, get_runners
from app.apis.workflows import get_workflow_by_name, post_workflow_from_body
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
    auth: Depends = Depends(get_current_user),
) -> dict[str, int]:
    return get_workflows(num)

@router.post("/workflows/{wf_name}", 
             tags=["workflows"], 
             openapi_extra={
                "requestBody": {
                    "content": {"application/x-yaml": {"schema": {"type": "string"}}},
                    "required": True,
                },
            },
)
async def post_workflow(
    wf_name: str,
    request: Request,
    # auth: Depends = Depends(get_current_user),
) -> Any:
    try:
        process = await post_workflow_from_body(wf_name, request)
        return json.dumps(process[1].tool, sort_keys=True, indent=2)
    except yaml.YAMLError:
        raise HTTPException(status_code=422, detail="Invalid YAML")
    except Exception as e:
        logging.exception(e)
        raise HTTPException(status_code=422, detail=e.__str__())

@router.get("/workflows/{wf_name}", tags=["workflows"], response_model=Any)
async def workflow_by_name(
    wf_name: str,
    # auth: Depends = Depends(get_current_user),
) -> Any:
    """Get the detail of a specific runner"""
    return get_workflow_by_name(wf_name)
