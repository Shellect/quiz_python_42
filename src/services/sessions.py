import json
import os
from datetime import datetime
from fastapi import Request, HTTPException
from redis import Redis, RedisError, from_url, ConnectionError
from typing import Dict, Any, Optional


class Session:
    def __init__(self, session_id: str, session_data: Dict[str, Any]):
        self.session_data = session_data
        self.session_id = session_id


class SessionManager:
    session_id: str
    request: Request
    redis_client: Optional[Redis]

    def __init__(self, request: Request):
        self.request = request
        self.redis_client = None
        self.session_id = request.state.session_id

    def init(self):
        try:
            self.redis_client = from_url(
                os.getenv("REDIS_URL"),
                encoding="utf-8",
                decode_responses=True
            )
            if not self.redis_client.ping():
                raise HTTPException(status_code=500, detail="Session storage unavailable")
        except ConnectionError as e:
            print(f"Redis connection error: {e}")
            raise HTTPException(status_code=500, detail="Session storage unavailable")

    def create_session(self) -> Optional[Session]:
        return self.save({
            "created_at": datetime.now().isoformat(),
            "last_activity": datetime.now().isoformat(),
            "is_authenticated": False,
            "user_agent": self.request.headers.get('user-agent'),
            "ip_address": self.request.client.host
        })

    def save(self, session_data: Dict[str, Any]):
        try:
            self.redis_client.setex(
                f"session:{self.session_id}",
                3600,
                json.dumps(session_data)
            )
            return Session(self.session_id, session_data)
        except RedisError:
            return None

    def get_data(self) -> Optional[Session]:
        try:
            data = self.redis_client.get(f"session:{self.session_id}")
            if data:
                return Session(self.session_id, json.loads(data))
            return self.create_session()
        except RedisError:
            return None

    def update(self, data: Dict[str, Any]) -> Optional[Session]:
        current_session = self.get_data()
        if current_session:
            current_session.session_data.update(data)
            self.save(current_session.session_data)
            return current_session
        return None


def get_session_manager(request: Request) -> SessionManager:
    session_manager = SessionManager(request)
    session_manager.init()
    return session_manager
