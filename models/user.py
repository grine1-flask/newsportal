from config import mysql


class User(object):

    @staticmethod
    def register(login, password, email, regdate, status) -> None:
        connection = mysql.get_db()
        cursor = mysql.get_db().cursor() #створюєм курсор
        sql_qwery = """
            insert into users (login, password, email, regdate, status)
            values (%s, %s, %s, %s, %s)
        """
        cursor.execute(sql_qwery, (login, password, email, regdate, status))
        connection.commit()
        cursor.close()
        connection.close()

    @staticmethod
    def login() -> None:
        pass