# src/service/auth_service.py
import hashlib
import os
from http.client import HTTPException

from sqlalchemy.orm import Session

from src.database import get_db
from src.models.entities import User
from src.models.schemas import UserCreate, UserLogin
from fastapi import status, Depends

from src.services.sessions import get_session_manager, SessionManager


class AuthService:
    def __init__(
            self,
            db: Session = Depends(get_db),
            session_manager: SessionManager = Depends(get_session_manager)
    ):
        self.db = db
        self.session_manager = session_manager

    def hash_password(self, password: str) -> str:
        salt = os.urandom(32)
        key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100_000)
        return salt.hex() + key.hex()

    def verify_password(self, user_password: str, stored_password: str) -> bool:
        try:
            hashed_bytes = bytes.fromhex(stored_password)
            salt = hashed_bytes[:32]
            key = hashed_bytes[32:]
            computed_key = hashlib.pbkdf2_hmac(
                'sha256',
                user_password.encode('utf-8'),
                salt,
                100_000
            )
            return computed_key == key
        except (ValueError, IndexError):
            return False

    async def create_user(self, user: UserCreate):
        # check existing user
        existing_user = self.db.query(User).filter(
            (User.email == user.email) |
            (User.username == user.username)
        ).first()

        if existing_user:
            raise ValueError("User already exists")

        hashed_password = self.hash_password(user.password)
        db_user = User(
            username=user.username,
            email=user.email,
            password_hash=hashed_password,
            group_id=user.group_id
        )
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        await self.login(db_user)
        return db_user

    async def authenticate_user(self, user_credentials: UserLogin):
        user = self.db.query(User).filter(
            User.username == user_credentials.username
        ).first()

        if not user or not self.verify_password(
                user_credentials.password,
                user.password_hash
        ):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid credentials"
            )
        await self.login(user)
        return user

    async def login(self, user: User):
        await self.session_manager.update({
            "user_id": user.id,
            "username": user.username,
            "is_admin": user.is_admin
        })
