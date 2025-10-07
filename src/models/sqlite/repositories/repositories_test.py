import pytest

from src.models.sqlite.settings.connection import db_connection_handler

from .people_repository import PeopleRepository
from .pets_repository import PetsRepository

# db_connection_handler.connect_to_db()


@pytest.mark.skip(reason="Not a real test, just for demonstration")
def test_list_pets():
    repo = PetsRepository(db_connection_handler)
    response = repo.list_pets()
    print(response)


@pytest.mark.skip(reason="Not a real test, just for demonstration")
def test_delete_pet():
    name = "Coco"

    repo = PetsRepository(db_connection_handler)
    repo.delete_pets(name)


@pytest.mark.skip(reason="Not a real test, just for demonstration")
def test_insert_person():
    first_name = "John"
    last_name = "Doe"
    age = 30
    pet_id = 2

    repo = PeopleRepository(db_connection_handler)
    repo.insert_person(first_name, last_name, age, pet_id)


@pytest.mark.skip(reason="Not a real test, just for demonstration")
def test_get_person():
    repo = PeopleRepository(db_connection_handler)
    person = repo.get_person(1)
    print()
    print(person)
