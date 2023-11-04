from __future__ import annotations
from abc import ABC, abstractmethod


class AbstractFactory(ABC):
    @abstractmethod
    def create_antena(self) -> AbstractProductA:
        pass

    @abstractmethod
    def create_switch(self) -> AbstractProductB:
        pass
