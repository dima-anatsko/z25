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


class User:
    def __init__(self, cursor):
        self.cursor = cursor

    def get_all(self):
        self.cursor.execute("SELECT * FROM app_users;")
        return self.cursor.fetchall()

    def get_user(self, user_id=None, username=None):
        result = None
        if user_id is not None:
            self.cursor.execute(
                "SELECT * FROM app_users WHERE id=%s;", (user_id, )
            )
            result = self.cursor.fetchall()
        elif username is not None:
            self.cursor.execute(
                "SELECT * FROM app_users WHERE username=%s;", (username, )
            )
            result = self.cursor.fetchall()
        return result

    def create_users(self, *users_list):
        users_list = [(i, ) for i in users_list]
        execute_values(
            self.cursor,
            "INSERT INTO app_users (username) VALUES %s;",
            users_list
        )


if __name__ == '__main__':
    connection = psycopg2.connect(
        dsn='postgres://admin_my_app:admin_my_app@localhost:5432/my_app'
    )
    cursor = connection.cursor()
    user_db = User(cursor)
    # user_db.create_users('Vasja', 'Petja', 'Valera')
    print(user_db.get_all())

    connection.commit()

    connection.close()
