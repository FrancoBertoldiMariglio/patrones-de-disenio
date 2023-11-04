from AbstractSwitch import AbstractSwitch
from AbstractAntena import AbstractAntena


class ConcreteSwitchTPLink(AbstractSwitch):
    def do_switching(self) -> str:
        return "Estoy conmutando con un switch TPLink."

    def do_switching_shared(self, collaborator: AbstractAntena):
        return f"Estoy conmutando con un switch Ubiquiti y tambien {collaborator.send_signal()}"
