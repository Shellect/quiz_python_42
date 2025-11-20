from fastapi import APIRouter, Depends

from src.models.schemas import UserLogin, UserCreate
from src.services.auth_service import AuthService
from src.services.sessions import SessionManager, get_session_manager

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/login")
def login_user(
        user_login: UserLogin,
        auth_service: AuthService = Depends(AuthService)
):
    return auth_service.authenticate_user(user_login)

@router.post("/register")
def register_user(
        user_credentials: UserCreate,
        auth_service: AuthService = Depends(AuthService)
):
    return auth_service.create_user(user_credentials)


@router.get("/session_data")
def session_data(session_manager: SessionManager = Depends(get_session_manager)):
    return session_manager.get_data()