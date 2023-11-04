from AbstractFactory import AbstractFactory
from ConcreteTPLinkFactory import ConcreteTPLinkFactory
from ConcreteUbiquitiFactory import ConcreteUbiquitiFactory

def client_code(factory: AbstractFactory) -> None:
    antena = factory.create_antena()
    switch = factory.create_switch()

    print(f"{antena.send_signal()}")
    print(f"{switch.do_switching()}", end="")

    if type(factory) is ConcreteUbiquitiFactory:
        print(f"{switch.do_switching_shared(antena)}", end="")

if __name__ == "__main__":

    print("Client: usando la fabrica TP-Link:")
    client_code(ConcreteTPLinkFactory())

    print("\n")

    print("Client: usando la fabrica Ubiquiti:")
    client_code(ConcreteUbiquitiFactory())