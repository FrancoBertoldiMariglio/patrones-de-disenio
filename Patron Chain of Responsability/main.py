from Handler import Handler
from Firefighter import Firefighter
from Policeman import Policeman
from Medic import Medic


def client(handler: Handler) -> None:

    for item in ["Ladron", "Fuego", "Paciente"]:
        result = handler.handle(item)
        if result:
            print(f"  {result}", end="")
        else:
            print(f"  No se hizo nada con {item}", end="")

if __name__ == '__main__':
    firefighter = Firefighter()
    policeman = Policeman()
    medic = Medic()

    firefighter.set_next(policeman).set_next(medic)

    print("Chain: Bombero > Policia > Medico")
    client(firefighter)
    print("\n")

    print("Subchain: Policia > Medico")
    client(policeman)
    print("\n")
