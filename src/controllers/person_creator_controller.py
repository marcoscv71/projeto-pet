import re

from src.models.sqlite.interfaces.people_repository import PeopleRepositoryInterface


class PersonCreatorController:
    def __init__(self, people_repository: PeopleRepositoryInterface):
        self.__people_repository = people_repository

    def create(self, person_data: dict) -> dict:
        first_name = person_data.get("first_name")
        last_name = person_data.get("last_name")
        age = person_data.get("age")
        pet_id = person_data.get("pet_id")

        self.__validate_first_and_last_name(first_name, last_name)
        self.__insert_person_in_db(first_name, last_name, age, pet_id)
        formated_response = self.__format_response(person_data)

        return formated_response

    def __validate_first_and_last_name(self, first_name: str, last_name: str) -> None:
        # Expressao regular para caracteres nao validos
        non_valid_characters = re.compile(r"[^a-zA-Z]")

        if non_valid_characters.search(first_name) or non_valid_characters.search(
            last_name
        ):
            raise Exception("First name and last name must contain only letters.")

    def __insert_person_in_db(
        self, first_name: str, last_name: str, age: int, pet_id: int
    ) -> None:
        self.__people_repository.insert_person(first_name, last_name, age, pet_id)

    def __format_response(self, person_data: dict) -> dict:
        return {"data": {"type": "Person", "count": 1, "attributes": person_data}}
