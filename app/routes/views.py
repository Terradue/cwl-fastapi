from __future__ import annotations

from fastapi import APIRouter, Depends

from app.apis.runners.mainmod import get_runners
from app.apis.api_b.mainmod import main_func as main_func_b
from app.core.auth import get_current_user

router = APIRouter()


@router.get("/runners", tags=["runners"])
async def runners(
    # auth: Depends = Depends(get_current_user),
) -> dict[str, int]:
    return get_runners()


@router.get("/api_b/{num}", tags=["api_b"])
async def view_b(
    num: int,
    auth: Depends = Depends(get_current_user),
) -> dict[str, int]:
    return main_func_b(num)
