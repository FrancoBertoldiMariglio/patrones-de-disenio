from AbstractAntena import AbstractAntena


class ConcreteAntenaUbiquiti(AbstractAntena):
    def send_signal(self) -> str:
        return "Estoy enviando señal con una antena Ubiquiti."