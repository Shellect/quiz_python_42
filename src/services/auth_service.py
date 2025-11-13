# src/service/auth_service.py
import hashlib
import os
from http.client import HTTPException

from sqlalchemy.orm import Session

from src.database import get_db
from src.models.entities import User
from src.models.schemas import UserCreate, UserLogin
from fastapi import status, Depends

from src.services.session_manager import SessionManager


class AuthService:
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

    def create_user(self, db: Session, user: UserCreate):
        # check existing user
        existing_user = db.query(User).filter(
            User.email == user.email |
            User.username == user.username
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
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user

    async def authenticate_user(
            self,
            user_credentials: UserLogin,
            db: Session = Depends(get_db),
            session: SessionManager = Depends(SessionManager)
    ):
        user = db.query(User).filter(
            User.username == user_credentials.username
        ).first()

        if not user or not self.verify_password(
            user_credentials.password,
            user.password
        ):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                details="Invalid credentials"
            )

        session_data = {
            "user_id": user.id,
            "username": user.username,
            "is_admin": user.is_admin
        }

        # TODO: replace with singletone
        await session.create_session(session_data)
