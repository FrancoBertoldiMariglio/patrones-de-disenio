from AbstractAntena import AbstractAntena


class ConcreteAntenaTPLink(AbstractAntena):
    def send_signal(self) -> str:
        return "Estoy enviando señal con una antena TPLink."