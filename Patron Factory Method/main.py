from Creator import Creator
from CSVFileReaderFactory import CSVFileReaderFactory
from JSONFileReaderFactory import JSONFileReaderFactory
from XMLFileReaderFactory import XMLFileReaderFactory


def cliente(creator: Creator, path) -> None:
    print(f"Client: No se que clase creadora estoy usando pero funciona.\n"
          f"{creator.logica('path')}", end="")


if __name__ == '__main__':

    cliente(CSVFileReaderFactory(), "hola mundo CSV")

    print('\n')

    cliente(JSONFileReaderFactory(), "hola mundo JSON")

    print('\n')

    cliente(XMLFileReaderFactory(), "hola mundo XML")
