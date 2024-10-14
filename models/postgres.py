import psycopg2
import os
import logging

# TODO: Add test cases for each function

class Postgres:
    __host__: str
    __db__: str 
    __user__: str
    __port__: str
    
    def __init__(self):
        self.__host__ = os.getenv("PG_HOST") if os.getenv("PG_HOST") else "localhost"
        self.__db__ = os.getenv("PG_DB") if os.getenv("PG_DB") else "postgres"
        self.__user__ = os.getenv("PG_USER") if os.getenv("PG_USER") else "postgres"
        self.__port__ = os.getenv("PG_PORT") if os.getenv("PG_PORT") else "5432"
    
    def connect_to_postgres(self):
        try:
            conn = psycopg2.connect(
                database = self.__db__,
                user = self.__user__,
                host = self.__host__,
                port = self.__port__
            )
        except Exception as e:
            logging.exception("Failed to connect to {}: {}".format(self.__db__, e))
            raise
        return conn

if __name__ == "__main__":
    from dotenv import load_dotenv, find_dotenv
    load_dotenv(find_dotenv())
    conn=None
    try:
        conn = Postgres().connect_to_postgres()
        print("Connection established successfully.")
    except Exception:
        print("Failed to connect.")
    finally:
        conn.close() if conn else None