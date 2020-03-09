"""
Описать для каждой таблицы из домашки(lesson12) класс,
который позволяет взаимодействовать с конткретной таблицей

Пример:
class User:
    ...
    def get_users(user_id=None, username=None):
        ...
    def create_users(*users_list):
        ...

class Test:
    ...

и тд
"""
import psycopg2
from psycopg2.extras import execute_values


class Table:
    @staticmethod
    def get_all(cursor, table):
        request = "SELECT * FROM %s;" % table
        cursor.execute(request)
        return cursor.fetchall()

    @staticmethod
    def del_all(cursor, table):
        cursor.execute("DELETE FROM %s;" % table)

    @staticmethod
    def get(cursor, id=None, column_name=None, column_param=None, table=None):
        request = None
        if id is not None:
            request = "SELECT * FROM %s WHERE id=%s;" % \
                      (table, id)
        elif column_param is not None:
            request = "SELECT * FROM %s WHERE %s='%s';" % \
                      (table, column_name, column_param)
        if request:
            cursor.execute(request)
        return cursor.fetchall()


class User(Table):
    __table__ = 'app_users'

    def __init__(self, name, user_id=None):
        self.name = name
        self.id = user_id

    @staticmethod
    def get_user(cursor, id=None, column='username',
                 username=None, table=None):
        result = Table.get(cursor, id, column, username, User.__table__)
        return User(result[0][1], result[0][0]) if result else None

    @staticmethod
    def create_users(cursor, *users_list):
        users_list = [(i,) for i in users_list]
        request = "INSERT INTO %s (username) VALUES " % User.__table__
        execute_values(cursor, request + "%s", users_list)

    @staticmethod
    def get_all(cursor, table=None):
        result = Table.get_all(cursor, User.__table__)
        if result:
            result = [User(name, user_id) for user_id, name in result]
        return result

    @staticmethod
    def __delete_user(cursor, user_id=None, username=None):
        request = None
        if user_id is not None:
            request = "DELETE FROM %s WHERE id='%s';" % \
                      (User.__table__, user_id)
        elif username is not None:
            request = "DELETE FROM %s WHERE username='%s';" % \
                      (User.__table__, username)
        if request:
            cursor.execute(request)

    @staticmethod
    def del_users_name(cursor, *users_list):
        for name in users_list:
            User.__delete_user(cursor, username=name)

    @staticmethod
    def del_all(cursor, table=None):
        Table.del_all(cursor, User.__table__)

    @staticmethod
    def del_users_id(cursor, *users_list):
        for user_id in users_list:
            User.__delete_user(cursor, user_id=user_id)

    def __repr__(self):
        return f'id={self.id} Name: {self.name}'


class Test(Table):
    __table__ = 'tests'

    def __init__(self, number, text, test_id=None):
        self.number = number
        self.text = text
        self.id = test_id

    @staticmethod
    def get_test(cursor, id=None, column='number', number=None, table=None):
        result = Table.get(cursor, id, column, number, Test.__table__)
        if result:
            result = [Test(number, text, id) for id, number, text in result]
        return result

    @staticmethod
    def get_all(cursor, table=None):
        result = Table.get_all(cursor, Test.__table__)
        if result:
            result = [Test(number, text, id) for id, number, text in result]
        return result

    @staticmethod
    def create_tests(cursor, *tests_list):
        tests_list = [(number, text) for number, text in tests_list]
        request = "INSERT INTO %s (number, text) VALUES " % Test.__table__
        execute_values(cursor, request + "%s", tests_list)

    @staticmethod
    def del_all(cursor, table=None):
        Table.del_all(cursor, Test.__table__)

    @staticmethod
    def __del_test_id(cursor, test_id=None):
        request = None
        if test_id is not None:
            request = "DELETE FROM %s WHERE id=%s;" % \
                      (Test.__table__, test_id)
        if request:
            cursor.execute(request)

    @staticmethod
    def del_tests_id(cursor, *tests_list):
        for test_id in tests_list:
            Test.__del_test_id(cursor, test_id)

    @staticmethod
    def del_tests_number(cursor, *tests_list):
        obj_test = []
        for test_number in tests_list:
            obj_test += Test.get_test(cursor, number=test_number)
        list_test_id = [item.id for item in obj_test]
        Test.del_tests_id(cursor, *list_test_id)

    def __repr__(self):
        return f'id={self.id} number={self.number} Test: {self.text}'


class Question(Table):
    __table__ = 'questions'

    def __init__(self, number, text, test_id=None):
        self.number = number
        self.text = text
        self.id = test_id

    @staticmethod
    def get_question(cursor, id=None, column='number',
                     number=None, table=None):
        result = Table.get(cursor, id, column, number, Question.__table__)
        if result:
            result = [Question(number, txt, id) for id, number, txt in result]
        return result

    @staticmethod
    def get_all(cursor, table=None):
        result = Table.get_all(cursor, Question.__table__)
        if result:
            result = [Question(number, txt, id) for id, number, txt in result]
        return result

    @staticmethod
    def create_questions(cursor, *questions_list):
        questions_list = [(number, text) for number, text in questions_list]
        request = "INSERT INTO %s (number, text) VALUES " % Question.__table__
        execute_values(cursor, request + "%s", questions_list)

    @staticmethod
    def del_all(cursor, table=None):
        Table.del_all(cursor, Question.__table__)

    @staticmethod
    def __del_question_id(cursor, question_id=None):
        request = None
        if question_id is not None:
            request = "DELETE FROM %s WHERE id=%s;" % \
                      (Question.__table__, question_id)
        if request:
            cursor.execute(request)

    @staticmethod
    def del_questions_id(cursor, *questions_list):
        for question_id in questions_list:
            Question.__del_question_id(cursor, question_id)

    @staticmethod
    def del_questions_number(cursor, *questions_list):
        obj_question = []
        for question_number in questions_list:
            obj_question += Question.get_question(cursor,
                                                  number=question_number)
        list_questions_id = [item.id for item in obj_question]
        Question.del_questions_id(cursor, *list_questions_id)

    def __repr__(self):
        return f'id={self.id} number={self.number} Question: {self.text}'


class TestsQuestion(Table):
    __table__ = 'tests_questions'

    def __init__(self, test_id, question_id, id=None):
        self.id = id
        self.test_id = test_id
        self.question_id = question_id

    @staticmethod
    def get_test_question(cursor, id=None, test_id=None, question_id=None):
        request = None
        if id is not None:
            request = "SELECT * FROM tests_questions WHERE id=%s;" % id
        elif test_id is not None and question_id is None:
            request = "SELECT * FROM tests_questions WHERE test_id=%s;" % \
                      test_id
        elif test_id is None and question_id is not None:
            request = "SELECT * FROM tests_questions WHERE question_id=%s;" % \
                      question_id
        elif test_id is not None and question_id is not None:
            request = "SELECT * FROM tests_questions WHERE test_id=%s" \
                      " AND question_id=%s;" % (test_id, question_id)
        if request:
            cursor.execute(request)
        result = cursor.fetchall()
        if result:
            result = [TestsQuestion(test_id, question_id, id) for
                      id, test_id, question_id in result]
        return result

    @staticmethod
    def get_all(cursor, table=None):
        result = Table.get_all(cursor, TestsQuestion.__table__)
        if result:
            result = [TestsQuestion(test_id, question_id, id) for
                      id, test_id, question_id in result]
        return result

    @staticmethod
    def create_tests_questions(cursor, *_list):
        _list = [(test_id, question_id) for test_id, question_id in _list]
        request = "INSERT INTO tests_questions (test_id, question_id) VALUES "
        execute_values(cursor, request + "%s", _list)

    @staticmethod
    def del_all(cursor, table=None):
        Table.del_all(cursor, TestsQuestion.__table__)

    @staticmethod
    def __del_test_question_id(cursor, id=None):
        request = None
        if id is not None:
            request = "DELETE FROM tests_questions WHERE id=%s;" % id
        if request:
            cursor.execute(request)

    @staticmethod
    def del_tests_questions_id(cursor, *list_id):
        for test_question_id in list_id:
            TestsQuestion.__del_test_question_id(cursor, test_question_id)

    def __repr__(self):
        return f'id={self.id} test_id={self.test_id} ' \
               f'question_id={self.question_id}'


class Answer(Table):
    __table__ = 'answers'

    def __init__(self, text, question_id, is_correct=None, id=None):
        self.id = id
        self.text = text
        self.question_id = question_id
        self.is_correct = is_correct

    @staticmethod
    def get_answer(cursor, id=None, is_correct=None, question_id=None):
        request = None
        if id is not None:
            request = "SELECT * FROM answers WHERE id=%s;" % id
        elif is_correct is not None and question_id is None:
            request = "SELECT * FROM answers WHERE is_correct=%s;" % is_correct
        elif is_correct is None and question_id is not None:
            request = "SELECT * FROM answers WHERE question_id=%s;" % \
                      question_id
        elif is_correct is not None and question_id is not None:
            request = "SELECT * FROM answers WHERE is_correct=%s AND " \
                      "question_id=%s;" % (is_correct, question_id)
        if request:
            cursor.execute(request)
        result = cursor.fetchall()
        if result:
            result = [Answer(text, question_id, is_correct, id) for
                      id, text, is_correct, question_id in result]
        return result

    @staticmethod
    def get_all(cursor, table=None):
        result = Table.get_all(cursor, Answer.__table__)
        if result:
            result = [Answer(text, question_id, is_correct, id) for
                      id, text, is_correct, question_id in result]
        return result

    @staticmethod
    def create_answers(cursor, *_list):
        _list = [(text, question_id, is_correct) for
                 text, question_id, is_correct in _list]
        request = "INSERT INTO answers (text, question_id, is_correct) VALUES "
        execute_values(cursor, request + "%s", _list)

    @staticmethod
    def del_all(cursor, table=None):
        Table.del_all(cursor, Answer.__table__)

    @staticmethod
    def __del_answer_id(cursor, id=None):
        request = None
        if id is not None:
            request = "DELETE FROM answers WHERE id=%s;" % id
        if request:
            cursor.execute(request)

    @staticmethod
    def del_answers_id(cursor, *list_id):
        for answer_id in list_id:
            Answer.__del_answer_id(cursor, answer_id)

    def __repr__(self):
        return f'id={self.id} answer={self.text} ' \
               f'is_correct={self.is_correct} question_id={self.question_id}'


class UserAnswer(Table):
    __table__ = 'users_answers'

    def __init__(self, tests_questions_id, user_id, answer_id, id=None):
        self.id = id
        self.tests_questions_id = tests_questions_id
        self.user_id = user_id
        self.answer_id = answer_id

    @staticmethod
    def get_user_answer(cursor, id=None, test_question_id=None, user_id=None):
        request = None
        if id is not None:
            request = "SELECT * FROM users_answers WHERE id=%s;" % id
        elif test_question_id is not None and user_id is None:
            request = "SELECT * FROM users_answers WHERE " \
                      "tests_questions_id=%s;" % test_question_id
        elif test_question_id is None and user_id is not None:
            request = "SELECT * FROM users_answers WHERE user_id=%s;" % user_id
        elif test_question_id is not None and user_id is not None:
            request = "SELECT * FROM users_answers WHERE " \
                      "tests_questions_id=%s AND " \
                      "user_id=%s;" % (test_question_id, user_id)
        if request:
            cursor.execute(request)
        result = cursor.fetchall()
        if result:
            result = [UserAnswer(tests_questions_id, user_id, answer_id, id)
                      for id, tests_questions_id, user_id, answer_id in result]
        return result

    @staticmethod
    def get_all(cursor, table=None):
        result = Table.get_all(cursor, UserAnswer.__table__)
        if result:
            result = [UserAnswer(tests_questions_id, user_id, answer_id, id)
                      for id, tests_questions_id, user_id, answer_id in result]
        return result

    @staticmethod
    def create_user_answer(cursor, *_list):
        _list = [(tests_questions_id, user_id, answer_id) for
                 tests_questions_id, user_id, answer_id in _list]
        request = "INSERT INTO users_answers (tests_questions_id, " \
                  "user_id, answer_id) VALUES "
        execute_values(cursor, request + "%s", _list)

    @staticmethod
    def del_all(cursor, table=None):
        Table.del_all(cursor, UserAnswer.__table__)

    @staticmethod
    def __del_user_answer_id(cursor, id=None):
        request = None
        if id is not None:
            request = "DELETE FROM users_answers WHERE id=%s;" % id
        if request:
            cursor.execute(request)

    @staticmethod
    def del_users_answers_id(cursor, *list_id):
        for user_answer_id in list_id:
            UserAnswer.__del_user_answer_id(cursor, user_answer_id)

    def __repr__(self):
        return f'id={self.id} tests_questions_id={self.tests_questions_id} ' \
               f'user_id={self.user_id} answer_id={self.answer_id}'


if __name__ == '__main__':
    connection = psycopg2.connect(
        dsn='postgres://admin_my_app:admin_my_app@localhost:5432/my_app'
    )
    cursor = connection.cursor()
    print(User.get_all(cursor))
    print(Test.get_all(cursor))
    print(Question.get_all(cursor))
    print(TestsQuestion.get_all(cursor))
    print(TestsQuestion.get_test_question(cursor, id=4))
    print(Answer.get_answer(cursor, is_correct=True, question_id=3))
    print(Answer.get_all(cursor))
    print(UserAnswer.get_all(cursor))
    connection.commit()
    connection.close()
