import psycopg2

class Postgres:

    def __init__(self, host, user, password, port, database):
        self.__host = host
        self.__user = user
        self.__password = password
        self.__port = port
        self.__database = database

        self.__create_connection()

    def __create_connection(self):
        self.__conn = psycopg2.connect(
            user=self.__user,
            password=self.__password,
            host=self.__host,
            port=self.__port,
            database=self.__database
        )

    @property
    def get_cursor(self):
        return self.__conn.cursor()

    def commit(self):
        self.__conn.commit()

    def close(self):
        self.__conn.close()

    def rollback(self):
        sef.__conn.rollback()