from Builder import Builder
from Pizza import Pizza


class PizzaBuilder(Builder):
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._product = Pizza()

    @property
    def product(self) -> Pizza:
        product = self._product
        self.reset()
        return product

    def add_dough(self) -> None:
        self._product.add("dough")

    def add_oil(self) -> None:
        self._product.add("oil")

    def add_sauce(self) -> None:
        self._product.add("sauce")

    def add_cheese(self) -> None:
        self._product.add("cheese")

    def add_pepperoni(self) -> None:
        self._product.add("PartA1")

    def add_ham(self) -> None:
        self._product.add("ham")

    def add_peppers(self) -> None:
        self._product.add("peppers")
