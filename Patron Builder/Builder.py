from __future__ import annotations
from abc import ABC, abstractmethod


class Builder(ABC):

    @property
    @abstractmethod
    def product(self) -> None:
        pass

    @abstractmethod
    def add_dough(self) -> None:
        pass

    @abstractmethod
    def add_oil(self) -> None:
        pass

    @abstractmethod
    def add_sauce(self) -> None:
        pass

    @abstractmethod
    def add_cheese(self) -> None:
        pass

    @abstractmethod
    def add_dough(self) -> None:
        pass

    @abstractmethod
    def add_oil(self) -> None:
        pass

    @abstractmethod
    def add_sauce(self) -> None:
        pass

    @abstractmethod
    def add_cheese(self) -> None:
        pass

    @abstractmethod
    def add_pepperoni(self) -> None:
        pass

    @abstractmethod
    def add_ham(self) -> None:
        pass

    @abstractmethod
    def add_peppers(self) -> None:
        pass
    def add_pepperoni(self) -> None:
        pass

    @abstractmethod
    def add_ham(self) -> None:
        pass

    @abstractmethod
    def add_peppers(self) -> None:
        pass
