from abc import ABC, abstractmethod


class PetListerControllerInterface(ABC):
    @abstractmethod
    def list_pets(self) -> dict:
        pass
