from sqlalchemy.orm.exc import NoResultFound

from src.models.sqlite.entities.pets import PetsTable
from src.models.sqlite.interfaces.pets_repository import PetsRepositoryInterface


class PetsRepository(PetsRepositoryInterface):
    def __init__(self, db_connection) -> None:
        self.__db_connection = db_connection

    def list_pets(self) -> list[PetsTable]:
        with self.__db_connection as conn:
            try:
                pets = conn.session.query(PetsTable).all()
                return pets
            except NoResultFound:
                return []

    def delete_pets(self, name: str) -> None:
        with self.__db_connection as conn:
            try:
                conn.session.query(PetsTable).filter(PetsTable.name == name).delete()
                conn.session.commit()
            except Exception as e:
                conn.session.rollback()
                raise e
