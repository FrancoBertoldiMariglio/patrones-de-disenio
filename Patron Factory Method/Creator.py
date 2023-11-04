from __future__ import annotations
from abc import ABC, abstractmethod


class Creator(ABC):
    @abstractmethod
    def create_reader(self):
        pass

    def logica(self, path):

        product = self.create_reader()

        result = f"Creator: el resultado es {product.read(path)}"

        return result

class Product(ABC):
    @abstractmethod
    def read(self, file) -> str:
        pass


