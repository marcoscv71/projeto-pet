from sqlalchemy import create_engine


class DBConnectionHandler:
    def __init__(self) -> None:
        self.__conection_string = "sqlite:///storage.db"
        self.__engine = None

    def connect_to_db(self):
        self.__engine = create_engine(self.__conection_string)

    def get_engine(self):
        return self.__engine


db_connection_handler = DBConnectionHandler()
