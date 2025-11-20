# routers/user.py
from datetime import datetime

from fastapi import APIRouter, Request, Depends, HTTPException
from starlette.status import HTTP_404_NOT_FOUND, HTTP_401_UNAUTHORIZED

from src.models.schemas import UserResponse
from src.services.sessions import SessionManager, get_session_manager

router = APIRouter()


@router.get(
    "/user",
    response_model=UserResponse,
    responses={
        200: {"description": "User data retrieved successfully"},
        401: {"description": "User not authenticated"},
        404: {"description": "User session not found"}
    }
)
async def get_current_user(
        request: Request,
        session_manager: SessionManager = Depends(get_session_manager)
) -> UserResponse:
    session = await session_manager.get_data()
    if not session:
        raise HTTPException(
            status_code=HTTP_404_NOT_FOUND,
            detail="Session not found"
        )
    session_data = session.session_data
    if not session_data.get("is_authenticated"):
        raise HTTPException(
            status_code=HTTP_401_UNAUTHORIZED,
            detail="User not authenticated"
        )

    await session_manager.update({
        "last_activity": datetime.now().isoformat()
    })

    return UserResponse(
        id=session_data.get("id"),
        username=session_data.get("username"),
        email=session_data.get("email"),
        is_authenticated=True,
        created_at=session_data.get("created_at"),
        last_activity=session_data.get("last_activity")
    )
