from abc import ABC, abstractmethod
from AbstractAntena import AbstractAntena


class AbstractSwitch(ABC):
    @abstractmethod
    def do_switching(self) -> str:
        pass

    @abstractmethod
    def do_switching_shared(self, collaborator: AbstractAntena):
        pass