from fastapi import APIRouter

router = APIRouter(prefix="/api/auth", tags=["auth"])

@router.post("/register")
def register():
    pass

@router.post("/login")
def login():
    pass