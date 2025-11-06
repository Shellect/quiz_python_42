from sqlalchemy import Column, Integer, Text, String, ForeignKey, Boolean, DateTime, func
from sqlalchemy.orm import relationship

from src.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    group_id = Column(Integer, ForeignKey('groups.id'), nullable=True)
    is_admin=Column(Boolean, default=False)
    created_at=Column(DateTime(timezone=True), server_default=func.now())

    group = relationship("Group", back_populates="users")

class Group(Base):
    __tablename__ = "groups"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True, nullable=False)
    description = Column(String(255))
    created_at=Column(DateTime(timezone=True), server_default=func.now())

    users = relationship("User", back_populates="group")

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