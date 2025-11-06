# src/service/auth_service.py
import hashlib
import os

from sqlalchemy.orm import Session

from src.models.entities import User
from src.models.schemas import UserCreate


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
