from Builder import Builder


class Director:
    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None:
        self._builder = builder

    def simple_pizza(self) -> None:
        self.builder.add_dough()
        self.builder.add_sauce()
        self.builder.add_oil()
        self.builder.add_cheese()

    def spicy_pizza(self) -> None:
        self.builder.add_dough()
        self.builder.add_sauce()
        self.builder.add_cheese()
        self.builder.add_pepperoni()

    def complete_pizza(self) -> None:
        self.builder.add_dough()
        self.builder.add_sauce()
        self.builder.add_oil()
        self.builder.add_cheese()
        self.builder.add_ham()
        self.builder.add_peppers()
