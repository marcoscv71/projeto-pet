from src.controllers.pet_lister_controller import PetListerController
from src.models.sqlite.entities.pets import PetsTable


class MockPetsRepository:
    def list_pets(self):
        return [
            PetsTable(name="Fluffy", type="cat", id=1),
            PetsTable(name="Max", type="dog", id=2),
        ]


def test_list_pets():
    controller = PetListerController(MockPetsRepository())
    response = controller.list_pets()

    expected_response = {
        "data": {
            "type": "pets",
            "count": 2,
            "attributes": [
                {"name": "Fluffy", "type": "cat"},
                {"name": "Max", "type": "dog"},
            ],
        }
    }

    assert response == expected_response
