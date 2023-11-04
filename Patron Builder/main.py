from Director import Director
from PizzaBuilder import PizzaBuilder


if __name__ == "__main__":

    director = Director()
    builder = PizzaBuilder()
    director.builder = builder

    print("Pizza basica: ")
    director.simple_pizza()
    builder.product.list_parts()

    print("\n")

    print("Pizza completa: ")
    director.complete_pizza()
    builder.product.list_parts()

    print("\n")

    print("Pizza customizada: ")
    builder.add_oil()
    builder.add_sauce()
    builder.add_ham()
    builder.product.list_parts()