"""Описать таблицы из lesson12/homework.sql при помощи sqlalchemy"""
import random

from sqlalchemy import (
    create_engine,
    MetaData,
    Column,
    ForeignKey,
    Boolean,
    Integer,
    String,
    UniqueConstraint
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine(
    'postgres://admin_alchemy:admin_alchemy@localhost:5432/alchemy'
)

metadata = MetaData()

BaseModel = declarative_base(bind=engine)


class User(BaseModel):
    __tablename__ = 'app_users'

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)

    def __repr__(self):
        return f'id={self.id} name={self.username}'


class Test(BaseModel):
    __tablename__ = 'tests'

    id = Column(Integer, primary_key=True)
    number = Column(Integer, nullable=False)
    text = Column(String, nullable=False)

    def __repr__(self):
        return f'id={self.id} number={self.number} test: {self.text}'


class Question(BaseModel):
    __tablename__ = 'questions'

    id = Column(Integer, primary_key=True)
    number = Column(Integer, nullable=False)
    text = Column(String, nullable=False)

    def __repr__(self):
        return f'id={self.id} number={self.number} question: {self.text}'


class TestQuestion(BaseModel):
    __tablename__ = 'tests_questions'
    __table_args__ = (UniqueConstraint('test_id', 'question_id'), )

    id = Column(Integer, primary_key=True)
    test_id = Column(ForeignKey('tests.id'), nullable=False)
    question_id = Column(ForeignKey('questions.id'), nullable=False)

    def __repr__(self):
        return f'id={self.id} test_id={self.test_id}' \
               f' question_id={self.question_id}'


class Answer(BaseModel):
    __tablename__ = 'answers'

    id = Column(Integer, primary_key=True)
    text = Column(String, nullable=False)
    is_correct = Column(Boolean, default=False)
    question_id = Column(ForeignKey('questions.id'), nullable=False)

    def __repr__(self):
        return f'id={self.id} answer={self.text} ' \
               f'is_correct={self.is_correct} question_id={self.question_id}'


class UserAnswer(BaseModel):
    __tablename__ = 'users_answers'
    __table_args__ = (UniqueConstraint('tests_questions_id', 'user_id'),)

    id = Column(Integer, primary_key=True)
    tests_questions_id = Column(ForeignKey('tests_questions.id'),
                                nullable=False)
    user_id = Column(ForeignKey('app_users.id'), nullable=False)
    answer_id = Column(ForeignKey('answers.id'), nullable=False)

    def __repr__(self):
        return f'id={self.id} tests_questions_id={self.tests_questions_id}' \
               f' user_id={self.user_id} answer_id={self.answer_id}'


BaseModel.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# users = [User(username=f'User {i}') for i in range(20)]
# session.add_all(users)
# session.commit()
# questions = [Question(number=random.randint(i, 5000),
#                       text=f'Text {i}') for i in range(300)]
# session.add_all(questions)
# session.commit()
# tests = [Test(number=i, text=f'Test {i}') for i in range(50)]
# session.add_all(tests)
# session.commit()
# answers = []
# questions_set = session.query(Question).all()
# for num, item in enumerate(questions_set, 1):
#     correct = random.randint(0, 3)
#     for j in range(4):
#         answers.append(Answer(
#             text=f'Answer {num * 4 - j}',
#             is_correct=correct == j,
#             question_id=item.id
#         )
#         )
# session.add_all(answers)
# session.commit()
# tests = session.query(Test).all()
# n = len(questions_set) // len(tests)
# tests_questions = []
# for num, test in enumerate(tests):
#     for i in range(n):
#         tests_questions.append(
#             TestQuestion(test_id=test.id,
#                          question_id=questions_set[n * num + i].id
#                          )
#         )
# session.add_all(tests_questions)
# session.commit()
# users_answer = []
# for user in session.query(User).all():
#     for test_question in session.query(TestQuestion).all():
#         answers_question = session.query(
#             Answer).filter_by(question_id=test_question.question_id).all()
#         users_answer.append(
#             UserAnswer(tests_questions_id=test_question.id,
#                        user_id=user.id,
#                        answer_id=answers_question[random.randint(0, 3)].id
#                        )
#         )
# session.add_all(users_answer)
# session.commit()
print(session.query(User).all())
print(session.query(Test).all())
print(session.query(Question).all())
print(session.query(TestQuestion).all())
print(session.query(Answer).all())
print(session.query(UserAnswer).all())
print(session.query(Question).filter_by(id=44).all())
print(session.query(Question).filter(Question.number < 500).all())
for user in session.query(User).all():
    true_answers = session.query(UserAnswer).filter(
        UserAnswer.answer_id == Answer.id,
        Answer.is_correct == 'True',
        UserAnswer.answer_id == user.id).all()
    print(f'name={user.username} \ttrue_answer={len(true_answers)}')
