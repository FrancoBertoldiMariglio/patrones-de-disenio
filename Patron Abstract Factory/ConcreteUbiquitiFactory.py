from AbstractFactory import AbstractFactory
from AbstractAntena import AbstractAntena
from AbstractSwitch import AbstractSwitch
from ConcreteAntenaUbiquiti import ConcreteAntenaUbiquiti
from ConcreteSwitchUbiquiti import ConcreteSwitchUbiquiti


class ConcreteUbiquitiFactory(AbstractFactory):
    def create_antena(self) -> AbstractAntena:
        return ConcreteAntenaUbiquiti()

    def create_switch(self) -> AbstractSwitch:
        return ConcreteSwitchUbiquiti()