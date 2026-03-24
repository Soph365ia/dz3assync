from fastapi import APIRouter, status, Depends, HTTPException, Response, Request
from fastapi.responses import JSONResponse
from schemas import UserRegistrationSchema
from schemas.users import UserInfoSchema, UserLoginSchema, AccessTokenSchema
from services import UserService
from dependency import CurrentUserDep

router = APIRouter(prefix= "/auth", tags=["auth"])

@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register_user(
    user: UserRegistrationSchema,
    service: UserService = Depends()
) -> UserInfoSchema:
    db_user = await service.create_user(user)
    return db_user

@router.post("/login", status_code=status.HTTP_200_OK)
async def login_user(
    response: Response,
    credentials: UserLoginSchema,
    service: UserService = Depends()
) -> AccessTokenSchema:
    token = await service.authenticate_user(credentials)
    response.set_cookie(key="access_token", value=token.access_token, httponly=True)
    return token

@router.get("/test")
async def test_auth(
    current_user: CurrentUserDep
):
    return JSONResponse({"username": current_user.username})