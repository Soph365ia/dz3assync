from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from api.test_async import router as test_router
from api import auth_router, posts_router


common_router = APIRouter()
common_router.include_router(auth_router)
common_router.include_router(posts_router)
common_router.include_router(test_router)
@common_router.get("/")
def root():
    return JSONResponse({"Hello": "World"}, status_code = status.HTTP_200_OK)


