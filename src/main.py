from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from src.database import get_db
from src.middleware import session_middleware
from src.models.entities import Question, QuestionOption
from src.routers import auth

app = FastAPI()

app.include_router(auth.router)
app.middleware("http")(session_middleware)

@app.get("/question")
def get_question(db: Session = Depends(get_db)):
    try:
        question = db.query(Question).first()
        answers = db.query(QuestionOption).filter(
            QuestionOption.question_id == question.id
        )
        answers_texts = [answer.option_text for answer in answers]

        return {
            "question": question.question_text,
            "answers": answers_texts
        }
    except:
        return {"status": "error"}
