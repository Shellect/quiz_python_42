from sqlalchemy import Column, Integer, Text, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from src.database import Base


class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)
    category_id = Column(Integer)
    question_text = Column(Text, nullable=False)

    options = relationship("QuestionOption", back_populates="question")


class QuestionOption(Base):
    __tablename__ = "question_options"

    id = Column(Integer, primary_key=True, index=True)
    question_id = Column(Integer, ForeignKey("questions.id", ondelete="CASCADE"))
    option_text = Column(String(255))
    is_correct = Column(Boolean, nullable=False, default=False)

    question = relationship("Question", back_populates="options")