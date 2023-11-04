from abc import ABC, abstractmethod


class AbstractAntena(ABC):
    @abstractmethod
    def send_signal(self) -> str:
        pass
