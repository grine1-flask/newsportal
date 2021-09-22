from config import mysql


class Article(object):

    @staticmethod
    def add_article(title, about, content, image, publish, user_id, status):
        connection = mysql.get_db()
        cursor = mysql.get_db().cursor()  # створюєм курсор
        sql_query = """
            insert into news (title, about, content, image, publish, user_id, status)
            values (%s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(sql_query, (title, about, content, image, publish, user_id, status))
        connection.commit()
        cursor.close()
        connection.close()


    @staticmethod
    def get_all_article() -> list:
        connection = mysql.get_db()
        cursor = mysql.get_db().cursor()  # створюєм курсор
        sql_qwery = """
                    select * from news
                """
        cursor.execute(sql_qwery)
        result = cursor.fetchall()
        cursor.close()
        connection.close()
        return result