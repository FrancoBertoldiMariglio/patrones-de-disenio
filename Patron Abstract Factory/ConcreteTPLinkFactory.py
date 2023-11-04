from AbstractFactory import AbstractFactory
from AbstractAntena import AbstractAntena
from AbstractSwitch import AbstractSwitch
from ConcreteAntenaTPLink import ConcreteAntenaTPLink
from ConcreteSwitchTPLink import ConcreteSwitchTPLink


class ConcreteTPLinkFactory(AbstractFactory):
    def create_antena(self) -> AbstractAntena:
        return ConcreteAntenaTPLink()

    def create_switch(self) -> AbstractSwitch:
        return ConcreteSwitchTPLink()
