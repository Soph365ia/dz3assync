from fastapi import APIRouter
import asyncio

router = APIRouter(prefix="/test", tags=["async-test"])

@router.get("/slow")
async def slow_endpoint(delay: int = 2):
    """
    Тестовый ендпоинт
    """
    await asyncio.sleep(delay)
    return {"delay_seconds": delay, "status": "completed"}
