# src/service/auth_service.py
import hashlib
import os


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
