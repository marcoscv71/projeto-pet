from sqlalchemy.orm.exc import NoResultFound

from src.models.sqlite.entities.people import PeopleTable
from src.models.sqlite.entities.pets import PetsTable
from src.models.sqlite.interfaces.people_repository import PeopleRepositoryInterface


class PeopleRepository(PeopleRepositoryInterface):
    def __init__(self, db_connection: str) -> None:
        self.__db_connection = db_connection

    def insert_person(
        self, first_name: str, last_name: str, age: int, pet_id: int
    ) -> None:
        with self.__db_connection as conn:
            try:
                person_data = PeopleTable(
                    first_name=first_name, last_name=last_name, age=age, pet_id=pet_id
                )
                conn.session.add(person_data)
                conn.session.commit()
            except Exception as e:
                conn.session.rollback()
                raise e

    def get_person(self, person_id: int) -> PeopleTable | None:
        with self.__db_connection as conn:
            try:
                person = (
                    conn.session.query(PeopleTable)
                    .outerjoin(PetsTable, PetsTable.id == PeopleTable.pet_id)
                    .filter(PeopleTable.id == person_id)
                    .with_entities(
                        PeopleTable.first_name,
                        PeopleTable.last_name,
                        PetsTable.name.label("pet_name"),
                        PetsTable.type.label("pet_type"),
                    )
                    .one()
                )
                return person
            except NoResultFound:
                return None
