from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from src.database import get_db
from src.middleware import session_middleware
from src.models.entities import Question, QuestionOption
from src.models.schemas import UserLogin, UserCreate
from src.routers import auth
from src.services.auth_service import AuthService
from src.services.sessions import SessionManager, get_session_manager

app = FastAPI()

app.include_router(auth.router)
app.middleware("http")(session_middleware)

@app.get("/question")
def get_question(db: Session = Depends(get_db)):
    try:
        question = db.query(Question).first()
        answers = db.query(QuestionOption).filter(QuestionOption.question_id == question.id)
        answers_texts = [answer.option_text for answer in answers]

        return {
            "question": question.question_text,
            "answers": answers_texts
        }
    except:
        return {"status": "error"}

@app.post("/login")
async def login_user(
        user_login: UserLogin,
        auth_service: AuthService = Depends(AuthService)
):
    return await auth_service.authenticate_user(user_login)

@app.post("/register")
async def register_user(
        user_credentials: UserCreate,
        auth_service: AuthService = Depends(AuthService)
):
    return await auth_service.create_user(user_credentials)


@app.get("/session_data")
async def session_data(session_manager: SessionManager = Depends(get_session_manager)):
    return await session_manager.get_data()